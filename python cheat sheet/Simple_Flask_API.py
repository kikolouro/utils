from flask_cors import CORS
from flask import Flask, request
from flask import Flask, request, render_template, send_from_directory
import os
app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'

#RENDER HTML TEMPLATE
@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')

#DOWNLOADS
@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, 'downloads/')
    return send_from_directory(uploads, filename, as_attachment=True)