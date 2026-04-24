import numpy as np 
#import tensorflow as tf

from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing import image 
import os 
import sys
import glob
import re

from werkzeug.utils import secure_filename
# decodnig of the class
from tensorflow.keras.applications.vgg19 import decode_predictions
#flask unit
from flask import Flask, redirect, url_for, request, render_template

#define flask app
app=Flask(__name__)
model_path='vgg19.h5'

# load model 
model=load_model(model_path) 

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html') 

@app.route('/predict', methods=['GET','POST'])
def upload():
    if request.method=="POST":
        # get file from post 
        f=request.files['file']
        basepath=os.path.dirname(__file__)
        file_path=os.path.join(
            basepath, 'uploads', secure_filename(f.filename)
        )
        f.save(file_path)


        #preprocessing of the image 
        img=image.load_img(file_path, target_size=(224,224))
        img_array=image.img_to_array(img)
        img_array=np.expand_dims(img_array,axis=0)
       


        #here is we are doing prediction 
        prediction=model.predict(img_array)
        
        #decodings
        decoded=decode_predictions(prediction,top=1)

        predicted_label=decoded[0][0][1]
        confidence=decoded[0][0][2]*100
        result=f"{predicted_label}({confidence:.2f}%)"

        prediction=model.predict(img_array)
        return render_template("index.html",prediction=result)
     
if __name__ =="__main__":
    app.run(debug=True)





