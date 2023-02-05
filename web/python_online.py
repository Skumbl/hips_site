#Package import
import os
import time

from flask import (Flask, Response, flash, make_response, redirect,
                   render_template, request, send_file, url_for)
from werkzeug.utils import secure_filename

#initialise app
app = Flask(__name__)

app.secret_key = "super secret key that takes us places, HackViolet 2023 HIPS"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = {'png'}

#decorator for homepage 
@app.route('/' )
def index():
    return render_template('index.html',
                           PageTitle = "Landing page")


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
        #reading the file
        #text = uploaded_file.read()
        #converting to a string.
        #text = str(text)

        target = os.path.join(APP_ROOT,'images/')
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            flash('Working....')
            destination = ''.join([target, filename])
            uploaded_file.save(destination)
        else:
            flash('file not allowed')
            filename = 'warning.png'
            destination = ''.join([target, filename])
            
        
        #You can then run any scripts you want on our file. 
        #Here we used a text file so any sort of text analysis could be undertaken
        #You could even run machine learning on a csv dataset.
        # function_that_does_something_1(text)
        # function_that_does_something_2(text)
        # function_that_does_something_3(text)

        # #Here I want to visualise my output for my users - so I return a plot.
        # #Plotting
        # fig = plot_something()
        
        # output = io.BytesIO()
        # FigureCanvas(fig).print_png(output)
        time.sleep(2)
        return send_file(destination, mimetype = 'image/png')
        #The created image will be opened on a new page
    
    else:
        return render_template('index.html',
                        PageTitle = "Landing page")
      #This just reloads the page if no file is selected and the user tries to POST. 


if __name__ == '__main__':
    app.run(debug = True)