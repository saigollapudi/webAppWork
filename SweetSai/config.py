
#to make the WTF forms in app highly secure 
WTF_CSRF_ENABLED = True  #this is for cross-site request forgery prevention
SECRET_KEY = '_Aum_JaiSaiRam,SuperD00perSecretKey_ThatUwillN0T_b_ab1E_2_GUESS?' # needed when CSRF is enabled; this makes a cryptographic token

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#configuration info for the Mozilla Persona authorization work
PERSONA_JS='https://login.persona.org/include.js'
PERSONA_VERIFIER='https://verifier.login.persona.org/verify'

# sqlite database related constants
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') # path to our database
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository') # folder where we will store the SQLAlchemy migrate files.
