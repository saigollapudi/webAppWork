from flask.ext.wtf import Form
from wtforms import TextField, StringField, BooleanField, validators
from wtforms.validators import DataRequired

class get_swtIDForm(Form):
   usr_name = StringField('usr_name', validators=[DataRequired()])
   remember_me = BooleanField('remember_me', default=False)

class MyForm(Form):
   usr_name = StringField('usr_name', validators=[DataRequired()])

class LoginForm(Form):
   usr_name = StringField('usr_name', validators=[DataRequired()])
   remember_me = BooleanField('remember_me', default=False)

class InputSweetForm(Form):
   usr        = TextField('sweet creator', [validators.Length(min=6, max=35)])
   email      = StringField('login email', validators=[DataRequired()])
   url        = StringField('url being modified', validators=[DataRequired()])
   context    = TextField('context of sweet', [validators.Length(min=6, max=35)])
   attributes = StringField('sweet attributes',   validators=[DataRequired()])
   timestamp  = StringField('timestamp',          validators=[DataRequired()])
   
