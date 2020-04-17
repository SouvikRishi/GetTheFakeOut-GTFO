from flask import Flask, jsonify, request
from FakeNewsDetector import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        text = some_json['NewsText']
        tag, fake_news, related_news = CheckNews(text)
        return jsonify({'Tag' : tag, 'Clarify_Fake_news': fake_news, 'More info': related_news}),201
    else:
        return jsonify({"about":"This is reponsible for News Check"})

@app.route('/urlCheck', methods=['GET','POST'])
def urlCheck():
    if (request.method == 'POST'):
        some_json = request.get_json()
        url = some_json['URL']
        urlCheckResult = SiteTagger(url)
        return jsonify({'URL_Result' : urlCheckResult}),201
    else:
        return jsonify({"about":"This is reponsible for Url Check"})


if __name__ == '__main__':
    app.run(port=5001,debug=False)

