import os
import cv2 as cv
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Tensorflow init
physical_devices = tf.config.experimental.list_physical_devices('CPU')

# App init
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './volume/uploads'

global predictionModel
predictionModel = tf.keras.models.load_model('./volume/model')

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg']

def processImage(img):
	h, w = img.shape[:2]
	margin = min(w, h)
	crop_img = img[0:margin, 0:margin]
	res = cv.resize(crop_img, (224, 224), interpolation = cv.INTER_CUBIC)
	return res

@app.route('/api/upload', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		return jsonify({'error':'file is missing'})
	file = request.files['file']
	if file.filename == '':
		return jsonify({'error':'no image selected for uploading'})
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		img = cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		cropedImg = processImage(img)
		cropedImg = np.expand_dims(cropedImg, axis=0)
		return jsonify(str(np.argmax(predictionModel.predict(cropedImg))))
	else:
		return jsonify({'error':'allowed image types are -> png, jpg, jpeg'})



if __name__ == '__main__':
	app.run()
