import os
import sys
import sys
import requests
from  flask import flask, redirect, request, session
from dotenv import load_dotenv

app = flask(__name__)

@app.route('/')

def hello():
        return "Hello World"


if __name__ == '__main__':
    app.run()