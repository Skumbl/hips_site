#Package import
import datetime
import os
import pathlib
import threading
import time

from flask import (Flask, Response, flash, make_response, redirect,
                   render_template, request, send_file, send_from_directory,
                   url_for)
from hips_hack.stenography import decode, encode
from werkzeug.utils import secure_filename

#initialise app
app = Flask(__name__)

app.secret_key = "super secret key that takes us places, HackViolet 2023 HIPS"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = os.path.join(APP_ROOT,'images/')
ALLOWED_EXTENSIONS = {'png'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



#decorator for homepage 
@app.route('/' )
def index():
    return render_template('index.html',
                           PageTitle = "Landing page", decrypted_message='')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#These functions will run when POST method is used.
@app.route('/', methods = ["POST"] )
def plot_png():
    #gathering file from form
    uploaded_file = request.files['txt_file']
    
    #making sure its not empty
    if uploaded_file.filename != '':
        filename = ''
        target   = os.path.join(APP_ROOT,'images/')
        if uploaded_file and allowed_file(uploaded_file.filename):
            flash('Working....')
            filename    = secure_filename(uploaded_file.filename)
            destination = ''.join([target, filename])
            uploaded_file.save(destination)
            if request.form['submit_form'] == 'Encode':
                data2encode = request.form['etext']
                encodedFileName = filename.split('.')[0]
                encodedFileName = ''.join([encodedFileName, '_encoded.png'])
                encodedName     = ''.join([target, encodedFileName])
                try:
                    encode(destination, data2encode, encodedName)
                except:
                    flash('File too large')
                    filename = 'warning.png'
                    target   = os.path.join(APP_ROOT,filename)
                    return send_file(target, mimetype = 'image/png')
                thread = threading.Thread(target=removeOld, args=(filename, encodedFileName))
                thread.start()
                return redirect(url_for('download_', name=encodedFileName)) #mimetype = 'image/png'))
            if request.form['submit_form'] == 'Decode':
                decodedText = decode(destination)
                thread      = threading.Thread(target=removeOld, args=(filename,))
                thread.start()
                return render_template('index.html',
                        PageTitle = "Landing page", decrypted_message=decodedText)
            
        else:
            flash('file not allowed')
            filename = 'warning.png'
            target   = os.path.join(APP_ROOT,filename)
            return send_file(target, mimetype = 'image/png')

    #This just reloads the page if no file is selected and the user tries to POST. 
    else:
        return render_template('index.html',
                        PageTitle = "Landing page", decrypted_message='')


@app.route('/images/<name>', methods=['GET', 'POST'])
def download_(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name, as_attachment=True)


def removeOld(*args):
    time.sleep(10)
    for file in args:
        filePath = app.config['UPLOAD_FOLDER'] + '/' + file

        os.remove(filePath)
        print('removed', file)


if __name__ == '__main__':
    # check if /images folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug = True)