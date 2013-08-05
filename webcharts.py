#!/usr/bin/env python
import os, sys
from flask import *
import MySQLdb, MySQLdb.cursors
import ConfigParser
import logging
application = app = Flask(__name__)
localpath = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, localpath)
logging.basicConfig(stream=sys.stderr)
config = ConfigParser.ConfigParser()
config.read(app.root_path + "/settings.conf")

@app.before_request
def before_request():
	g.conn = MySQLdb.connect(host=config.get("mysql","host"), 
				user=config.get("mysql","user"), 
				passwd=config.get("mysql","pass"), 
				db=config.get("mysql","db"), 
				cursorclass=MySQLdb.cursors.DictCursor, 
				charset='utf8')
	g.cursor = g.conn.cursor()

@app.route("/")
def index():
	return "test" #render_template("webcomic.html")