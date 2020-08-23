# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:40:17 2020

@author: Anirban
"""

from flask import Flask, render_template

# Define a flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)