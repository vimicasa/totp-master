from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import LoginForm, VerifyForm
import pyotp
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #Check the password
        if form.password.data == Config.SECRET_KEY:
            return redirect(url_for('generate', email=form.email.data))  
        flash('Password is not correct')
    return render_template('login.html', form=form)

@app.route('/generate/<email>')
def generate(email):
    
    #Check folder users
    folder= Config.FOLDER_NAME
    if not os.path.exists(folder):
        os.makedirs(folder)

    #Check if file already exists
    if not os.path.exists(folder+'/'+email):
        with open(folder+'/'+email, 'w') as file:
            #Generate random seed
            seed = pyotp.random_base32()
            file.write(seed)
            file.close()            
    else:
        with open(folder+'/'+email, 'r') as file: 
            seed = file.readline()
            file.close()     
      
    #Generate otpAuth URL
    otpQR = pyotp.totp.TOTP(seed).provisioning_uri(email, issuer_name=Config.APP_NAME)

    return render_template('generateQR.html', email=email, otpQR=otpQR)

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    form = VerifyForm()
    if form.validate_on_submit():
        
        #Check if file already exists
        if not os.path.exists(Config.FOLDER_NAME+'/'+form.email.data):
            flash('User not found {}'.format(form.email.data))
        else :
            with open(Config.FOLDER_NAME+'/'+form.email.data, 'r') as file: 
                seed = file.readline()
                file.close() 
            totp = pyotp.TOTP(seed)

            if totp.verify(form.token.data): 
                flash('Token OK for user {}'.format(form.email.data))
            else:
                flash('Invalid Token for user {}'.format(form.email.data))
        
        return redirect('/verify')
    return render_template('verify.html', form=form)

if __name__ == '__main__':
    app.run()