from sklearn.tree import DecisionTreeClassifier as dc
from sklearn.externals import joblib
from flask import Flask, request, jsonify
import json

import os

app = Flask("__name__")


@app.route('/', methods=['POST'])
def get_user():
    try:
        age = request.json['age']
        gender = request.json['gender']
        model = dc()
        model = joblib.load('music-recommender.joblib')
        predictions = model.predict([[int(age), int(gender)]])

        return jsonify({'result': str(predictions[0]), 'status': 500})
    except:
        return jsonify({'id': 'faile', 'status': 200})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '5000'), debug=True)
