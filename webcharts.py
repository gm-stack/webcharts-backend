#!/usr/bin/env python
import os, sys
from flask import *
import logging
application = app = Flask(__name__)
localpath = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, localpath)
logging.basicConfig(stream=sys.stderr)

@app.route("/")
def index():
	return render_template("webcomic.html")