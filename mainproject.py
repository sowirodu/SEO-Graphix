from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy
app = Flask(__name__)     
proxied = FlaskBehindProxy(app)  ## add this line
app.config['SECRET_KEY'] = 'e30b92ab25051f1ed6da06292f122baf'
@app.route("/")
@app.route("/Seo_Tech_Conference.html")
def hello_world():
    return render_template('Seo_Tech_Conference.html')
    
@app.route('/Seo_Tech_Conference_SignUpPage.html')
def sign_up():
    return render_template('Seo_Tech_Conference_SignUpPage.html')

@app.route('/Seo_Tech_Conference_AboutUsPage.html')
def about_us():
    return render_template('Seo_Tech_Conference_AboutUsPage.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")