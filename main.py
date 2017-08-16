__author__ = 'Krat0S'

from flask import Flask
from common.constants import news
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/get_news/")
def get_news():
    return news


if __name__ == "__main__":
    app.run()
