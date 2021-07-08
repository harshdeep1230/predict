


import numpy as np
import pickle
import pandas as pd
from flask import Flask, request
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
pickle_in = open("finalized_model.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
  weight=request.form['weight']
  length1=request.form['length1'] 
  length2=request.form['length2'] 
  length3=request.form['length3'] 
  height=request.form['height'] 
  width=request.form['width']
  prediction = classifier.predict([[weight,length1,length2,length3,height,width]])
  return render_template('index.html', prediction_text='fish type  {}'.format(prediction) )
    
    


if __name__=='__main__':
    app.run()
