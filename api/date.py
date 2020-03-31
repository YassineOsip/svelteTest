from flask import Flask


app = Flask(__name__)


@app.route(r'/')
def index():
    return "hello world"