import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [str(x) for x in request.form.values()]
    # print(features[0])
    # print(features[1])

    res1 = requests.post('http://localhost:5001/', json={"NewsText": features[1]})
    res2 = requests.post('http://localhost:5001/urlCheck', json={"URL": features[0]})

    if res2.ok:
        res_dict_url = res2.json()
        URL_Tag = res_dict_url['URL_Result']
        # print(URL_Tag)
        if URL_Tag=="Not a Trusted Site":
            return render_template('predictionsBadURL.html')

    if res1.ok:
        res_dict = res1.json()
        Tag = res_dict['Tag']
        if Tag =="Fake News!":

            Contents = res_dict['Clarify_Fake_news'].split('\n\n')
            Contents = Contents[1:-1]
            ContentsStructured =[]
            # print(Contents)
            for Content in Contents:
                ContentList = Content.split('\n')
                ContentList[2] = ContentList[2].replace("To know more click on this link: ",'')

                ContentsStructured.append(ContentList)
            # print(ContentsStructured)
            return render_template('predictions.html', lines = ContentsStructured)

        else:
            return render_template('predictionsTrue.html')



if __name__ == "__main__":
    app.run(port=1000, debug=True)