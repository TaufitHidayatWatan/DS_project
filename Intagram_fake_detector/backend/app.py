from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

LABEL = ['Akun Ini Asli', 'Akun Ini Fake!!!']
columns = ['profile pic', 'name==username', 'description length', 'external URL', 'private', '#posts', '#followers', '#follows']
with open("pipeline.pkl", "rb") as f:
    model_instagram = pickle.load(f)

@app.route("/")
def homepage():
    return "<h1>Backend Fake Instragram Account Detector </h1>"

@app.route("/instagram", methods=["GET", "POST"])
def instrgram_inference():
    if request.method == 'POST':
        data = request.json
        new_data = [data['profile pic'],
                    data['name==username'],
                    data['description length'],
                    data['external URL'],
                    data['private'],
                    data['#posts'],
                    data['#followers'],
                    data['#follows']]
        new_data = pd.DataFrame([new_data], columns=columns)
        print('new_data:', new_data)
        res = model_instagram.predict(new_data)
        print('res:', res)
        response = {'code':200, 'status':'OK',
                    'result':{'prediction': str(res[0]),
                              'classes': LABEL[res[0]]}}
        return jsonify(response)
    return "Silahkan gunakan method post untuk mengakses model instagram"


