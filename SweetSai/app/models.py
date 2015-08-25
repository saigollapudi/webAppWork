from app import db

# creating an object for a table named User
class User(db.Model):
   id            = db.Column(db.Integer,     primary_key = True)
   login_name    = db.Column(db.String(64),  index=True, unique=True)
   login_emailID = db.Column(db.String(120), index=True, unique=True)
   sweets        = db.relationship('Sweet', backref='author', lazy='dynamic')

   # should the user be allowed to authenticate?
   def is_authenticated(self):
       return True

   # banned users can be considered inactive    
   def is_active(self):
       return True

   # fake users who are not allowed to even log on
   def is_anonymous(self):
       return False

   # returns a unique identifier for user    
   def get_id(self):
       try:
           return unicode(self.id) # python 2
       except NameError:
          return str(self.id)      # python 3
          
   def __repr__(self):
       return '<User %r>' % (self.login_name)


class Sweet(db.Model):
   id        = db.Column(db.Integer,     primary_key=True)

   # the "s" in front represents the notion of a "sweet"; these are
   # attributes of a "sweet"
   sUsrname  = db.Column(db.String(64),  index=True, unique=True) #this is the Sweet user name
   sUrl      = db.Column(db.String(320), index=True, unique=True)
   sContext  = db.Column(db.String(64),  index=True, unique=True)
   sAttrib   = db.Column(db.Text,        index=True, unique=True)
   sTimestamp= db.Column(db.DateTime)
   sUser_id  = db.Column(db.Integer,     db.ForeignKey('user.id'))

   def __repr__(self):
       return '<Sweet %r>' % (self.sUsrname)
