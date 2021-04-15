import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = './volume/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
		#
		# Here code that will preprocess the image and push it to the model
		# Send result from the model back to the app
		#
		return jsonify({'message':'image successfully uploaded'})
	else:
		return jsonify({'error':'allowed image types are -> png, jpg, jpeg'})


if __name__ == '__main__':
	# Loading the model
	app.run(debug=True)
