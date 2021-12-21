from flask_cors import CORS
import markdown
import markdown.extensions.fenced_code
from flask import Flask, request, render_template, send_from_directory
import os
from decouple import config
from flask_basicauth import BasicAuth
app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'

# CLOSE PROD SITE, OPEN IN DEV MODE
if config('ENVIRONMENT') != 'DEV':
    app.config['BASIC_AUTH_USERNAME'] = config('BASIC_AUTH_USERNAME')
    app.config['BASIC_AUTH_PASSWORD'] = config('BASIC_AUTH_PASSWORD')
    app.config['BASIC_AUTH_FORCE'] = True
    basic_auth = BasicAuth(app)
app.config.update(TEMPLATES_AUTO_RELOAD = True)

#RENDER HTML TEMPLATE
@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')

#DOWNLOADS
@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, 'downloads/')
    return send_from_directory(uploads, filename, as_attachment=True)

# READ MARKDOWN FILES AS HTML
@app.route('/documentacaodns', methods=['GET'])
def documentacaodns():

    readme_file = open("documentacao/dns.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code", "codehilite"]
    )
    formatter = HtmlFormatter(style="monokai",full=True,cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    return md_css_string + md_template_string