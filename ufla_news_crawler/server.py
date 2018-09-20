from flask import Flask
from get_news import get_news
app = Flask(__name__)

@app.route('/get_news')
def getNews():
    response = app.response_class(
        response=get_news(),
        status=200,
        mimetype='application/json'
    )
    return response