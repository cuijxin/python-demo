#!/usr/bin/python
#coding=utf8
"""
# Author: cuijx
# Created Time : 2019-07-01 14:22:22

# File Name: read-env-app.py
# Description:

"""

import os
import yaml

from flask import Flask, jsonify



app = Flask(__name__)

@app.route("/")
def index():
    current_path = os.path.abspath(os.path.dirname(__file__))
    print(current_path)
    print(current_path + '/conf/')
    with open(current_path + '/conf/' + 'config.yaml', 'r') as f:
        temp = yaml.load(f.read())
        TOKEN = temp['ENVIRONMENT']['TOKEN']
        LANGUAGE = temp['ENVIRONMENT']['LANGUAGE']
        return jsonify(token=TOKEN, lang=LANGUAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
