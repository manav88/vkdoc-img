import numpy as np
from flask import Flask, request, render_template, flash, redirect
from PIL import Image
from keras.applications.efficientnet import EfficientNetB0
from keras import models, layers
from werkzeug.utils import secure_filename
import os

def modelEfficientNetB0():
    model = models.Sequential()
    model.add(EfficientNetB0(include_top = False, weights = "imagenet", input_shape=(100,100, 3)))
    model.add(layers.GlobalAveragePooling2D())
    model.add(layers.Dense(2, activation = "sigmoid"))
    return model
 
model = modelEfficientNetB0()
model.load_weights('./_model3_.h5')

ALLOWED_EXTENSIONS = {"jpg", "png", "jpeg"}

if not os.path.exists('./static/test'):
    os.makedirs('./static/test')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.secret_key = "test"
app.config['UPLOAD_FOLDER'] = "./static/test"

@app.route('/', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            IMG = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            IMG = IMG.resize((100, 100))
            IMG = np.array(IMG)
            IMG = np.true_divide(IMG, 255)
            IMG = IMG.reshape(-1,100, 100,3)
            predictions = model.predict(IMG)
            prediction_class = np.argmax(predictions, axis=-1)
            classes = ['Non Malignant (No Cancer)','Malignant']
            predicted_class = classes[prediction_class[0]]
            res_val = 'Our Prediction says that it is {}.'.format(predicted_class.lower())
            return render_template('index.html', result=res_val)
        else:
            return "File Type not supported!"

    return render_template('index.html')