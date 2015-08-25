from flask import (render_template, 
                   flash, 
                   redirect,
                   session, 
                   url_for, 
                   request, 
                   g,
                   abort )
from flask.ext.login import (login_user, 
                             logout_user, 
                             current_user,
                             login_required )
from app import app, db, lm
from .forms import get_swtIDForm, MyForm, LoginForm, InputSweetForm
from .models import User
import requests

@app.before_request
def get_current_user():
    g.user = None
    email = session.get('email')
    if email is not None:
        g.user = email

@app.route('/')
@app.route('/index')
def home_page():
    form = MyForm()
    return render_template('welcome.html', form=form)

@app.route('/showall')
def showall_page():
    user = 'Sai'      
    sweet_array = [
        {'uid': 'SaiGo 1', 
         'context': 'testSweet', 
         'url' : 'https://saigo1works.com/',
         'attributes': 'fake 1 Attrib'
        },
        {'uid': 'SaiGo 2', 
         'context': 'testSweet', 
         'url' : 'https://saigo2works.com/',
         'attributes': 'fake 2 Attrib'
        },
        {'uid': 'SaiGo 3', 
         'context': 'testSweet', 
         'url' : 'https://saigo3works.com/',
         'attributes': 'fake 3 Attrib'
        } 
    ]
    return render_template('showSweets.html', 
                           title='SaiGo_Home', 
                           user=user, 
                           sweet_array=sweet_array)

@app.route('/inputsweet', methods=['GET', 'POST'])
def input_sweet():
    form = InputSweetForm(request.form) 

    # this is activated when the form is filled by user
    if request.method == 'POST' and form.validate():
         flash('thanks for the sweet!')

         #  # if no email given, then force to conform; check for authentication
         #  if form.email is None or resp.email == "":
         #     flash('Invalid Login. Please try again.')
         #     return redirect(url_for('login'))

         #  # check for existing users in database based on email ID
         #  user = User.query.filter_by(login_emailID=form.email).first()

         #  # user seems to be new, then proceed
         #  if user is None:
         #     usr = form.usr
         #     # user name is not given, then extract it from email ID
         #     if usr is None or usr == ""
         #        usr = form.email.split(@')[0]

         # store email ID, name in USER table of database
         user = User(login_name    = form.usr.data, 
                     login_emailID = form.email.data)
   
         # store the details from form into SWEET table of database   
         sweet = Sweet(sUsrname   = form.usr.data, 
                       sUrl       = form.url.data, 
                       sContext   = form.context.data, 
                       sAttrib    = form.attributes.data, 
                       sTimestamp = form.timestamp.data)

         # add, commit the user, sweet values into the database
         db.session.add(user)
         db.session.add(sweet)
         db.session.commit()
         return redirect(url_for('/index'))
    return render_template('inputsweetform.html',
                           title='input sweets',
                           form=form)

@app.route('/_auth/login', methods=['GET', 'POST'])
def login_handler():
    """This is used by the persona.js file to kick off the
    verification securely from the server side.  If all is okay
    the email address is remembered on the server.
    """
    resp = requests.post(app.config['PERSONA_VERIFIER'], data={
        'assertion': request.form['assertion'],
        'audience': request.host_url,
    }, verify=True)
    if resp.ok:
        verification_data = resp.json()
        if verification_data['status'] == 'okay':
            session['email'] = verification_data['email']
            return 'OK'
    abort(400)

@app.route('/_auth/logout', methods=['POST'])
def logout_handler():
    """This is what persona.js will call to sign the user
    out again.
    """
    session.clear()
    return 'OK'

@app.route('/get_swtID', methods=['GET', 'POST'])
def get_swtID():
    form = get_swtIDForm()
    return render_template('get_swtID.html',
                           title='Sign In',
                           form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       login_user(user)
       flask.flash('logged in successfully')
       
       next = flask.request.args.get('next')
       if not next_is_valid(next):
          return flask.abort(400)
          
       return flask.redirect(next or flask.url_for('/index'))
    return render_template('login.html', form=form)

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

@lm.user_loader
def load_user(id):
    # user Id from Flask-Login is unicode, thats why we need to convert
    # to int before sending it to database (SQLAlchemy) pkg
    return User.query.get(int(id))  

if __name__ == '__main__':
    app.run()
