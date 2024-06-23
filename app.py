from flask import Flask, render_template, url_for, flash, redirect, request
from datetime import datetime
from sys import stderr
import segno


app = Flask(__name__)
app.config["TEMPLATES_FOLDER"] = "templates"
# app.config["TEMPLATES_FOLDER"] = "templates"


@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')


    
@app.route('/qr', methods=['GET','POST'])
def qr():
    if request.method == 'POST':
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        imagepath = f"static/images/QR_({time})_.png"
        
        url = request.form['userinput']
        print(f'USER input: {url}',file=stderr)
        finished_image = segno.make(url)
        finished_image.save(imagepath, scale=10)
        print(f'Image path: {imagepath}')
        return render_template('qr.html', imagepath=imagepath)
    else:  
        return render_template('qr.html')


@app.route('/bmremover', methods=['GET', 'POST'])
def bmremover():
    return render_template('bmremover.html')



if __name__ == '__main__':
   app.run(debug=True)