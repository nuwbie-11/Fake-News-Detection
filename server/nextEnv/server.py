from flask import Flask, jsonify, request
from flask_cors import CORS
import os

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# instance
app = Flask(__name__)
CORS(app)

    
def getUtils():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_filename = os.path.join(script_dir, 'linear.pkl')
    vector_fileName = os.path.join(script_dir, 'vector.pkl')
    
    model = pickle.load(open(model_filename,'rb'))
    vector = pickle.load(open(vector_fileName,'rb'))
    
    return (model,vector)

def preProcess(text):
    tempText=[]
    
    for sentences in ([text]):
        sentence = re.sub(r'[^\w\s]','',sentences)
        tempText.append(' '.join(token.lower() for token in str(sentence).split() if token not in stopwords.words('english')))
        
    return tempText
    
@app.route("/predictNews",methods=["POST"])
def predictNews():
    try:
        if request.method == "POST":
            text = request.form["article"]
        
        if text:
            text = preProcess(text)
            model,vector = getUtils()
            text = vector.transform(text)
            
            prediction = model.predict(text)
            
            response = "Real News" if prediction == 0 else "Fake News"

            return jsonify({
                'isSucess':True,
                'message':response
                })
    except :
        return jsonify({
            'isSucess': False,
            'message':"response"
        })
    



if __name__ == '__main__':
    app.run(debug=True,port=8080)