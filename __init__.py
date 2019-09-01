from flask import *
from random import randint
import keymgmt
import db
import os
from werkzeug.utils import *
uploadfolder = str(os.getcwd())+'/upload_folder'
allowedextensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = uploadfolder
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in allowedextensions

@app.route('/api/v1/login/login', methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        if not checkloginstat():
            name = db.check_user(request.form['api_key'])
            
            if name == None:
                return 'wrong key'
            else:
                res = make_response(render_template('logedin.html',username=name,k=request.form['api_key']))
                res.set_cookie('logedin',value='true',max_age=260000000)
                return res
        else:
            return redirect('https://api.matthew.tk/')
    elif checkloginstat():
        return redirect(url_for('already_logged'))
    else:
        return render_template('keysubmit.html')

@app.route('/api/v1/login/already_logged')
def already_logged():
    return 'welcome back :)'

@app.route('/api/v1/login/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        key = keymgmt.create_new_key()
        db.new_user(request.form['name'], apikey = key)
        return render_template('registered.html',name = request.form['name'], apik = key)
    else:
        return render_template('register.html')

@app.route('/api/v1')
def welcome():
    return render_template('welcome.html')

@app.route('/')
def rootdom():
    return redirect('https://api.matthew.tk/api/v1')

def checkloginstat():
    if request.cookies.get('logedin')=='true':
        return True
    else:
        return False

@app.route('/api/v1/logout', methods = ['POST','GET'])
def logout():
    if request.method == 'POST':
        res = make_response(redirect('https://api.matthew.tk/api/v1'))
        res.set_cookie('logedin','',max_age=0)
        return res
    else:
        return render_template('logout.html')

@app.route('/api/v1/fup', methods = ['POST','GET'])
def fupload():
    if checkloginstat():
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('no file found')
                return (request.url)
            file = request.files['file']
            if file.filename == '':
                flash('no file selected')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return 'successfully uploaded file'
        return render_template('fileupload.html')
    else:
        
        return redirect('https://api.matthew.tk/')

app.run('0.0.0.0',80)
#11RT#&:KX#MooUGK