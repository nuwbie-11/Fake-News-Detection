from flask import Flask, jsonify, request
from flask_cors import CORS
import os

import sklearn
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# instance
app = Flask(__name__)

CORS(app)


@app.route("/test",methods=['GET'])
def returnHome():
    return jsonify({
        'message':"Fetched From Server"
    })

@app.route("/testPredict",methods=["POST"])
def Predict():
    
    
    if request.method == "POST":
        text = request.form["article"]
    
    print(f"Your Form : {text}")
    
    
    # Get the absolute path to the directory containing your script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_filename = os.path.join(script_dir, 'linear.pkl')
    vector_fileName = os.path.join(script_dir, 'vector.pkl')
    

    
    tempText=[]
    
    for sentences in ([text]):
        sentence = re.sub(r'[^\w\s]','',sentences)
        tempText.append(' '.join(token.lower() for token in str(sentence).split() if token not in stopwords.words('english')))
    
    model = pickle.load(open(model_filename,'rb'))
    vector = pickle.load(open(vector_fileName,'rb'))
    
    text = vector.transform(tempText)
    
    prediction = model.predict(text)
    print(f"Result : {prediction}")
    if prediction == 0:
        response = "Real News"
    else:
        response = "Fake News"
    return jsonify({
        'message':response
    })


if __name__ == '__main__':
    app.run(debug=True,port=8080)