# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

#新分頁
@app.route("/test/path")
def new_Path():
    return "Hello World /test/path!"

if __name__ == '__main__':
    app.run(debug=True)
