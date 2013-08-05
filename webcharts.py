#!/usr/bin/env python
import os, sys
from flask import *
import MySQLdb, MySQLdb.cursors
import configparser
import logging
application = app = Flask(__name__)
localpath = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, localpath)
logging.basicConfig(stream=sys.stderr)
config = configparser.ConfigParser()
config.read(os.path.join(app.root_path,"settings.conf"))

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
@app.route("/comic/<comicnum>")
def index(comicnum=None):
	g.cursor.execute("select count(*) as count from webcharts")
	numcomics = g.cursor.fetchone()['count']
	thiscomic = numcomics - 1
	if comicnum:
		thiscomic = comicnum
	g.cursor.execute("select `id`,`title`,`filename` from webcharts where id=%(id)s", {'id': thiscomic})
	res = g.cursor.fetchone()
	return render_template("webcomic.html", comic=res, numcomics=numcomics)