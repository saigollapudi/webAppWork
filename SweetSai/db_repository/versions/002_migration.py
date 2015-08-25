from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
sweet = Table('sweet', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('sUsrname', String(length=64)),
    Column('sUrl', String(length=320)),
    Column('sContext', String(length=64)),
    Column('sAttrib', String(length=320)),
    Column('sUser_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('sUsrname', VARCHAR(length=64)),
    Column('sUrl', VARCHAR(length=320)),
    Column('sContext', VARCHAR(length=64)),
    Column('sAttrib', VARCHAR(length=320)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('login_name', String(length=64)),
    Column('login_emailID', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['sweet'].create()
    pre_meta.tables['user'].columns['sAttrib'].drop()
    pre_meta.tables['user'].columns['sContext'].drop()
    pre_meta.tables['user'].columns['sUrl'].drop()
    pre_meta.tables['user'].columns['sUsrname'].drop()
    post_meta.tables['user'].columns['login_emailID'].create()
    post_meta.tables['user'].columns['login_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['sweet'].drop()
    pre_meta.tables['user'].columns['sAttrib'].create()
    pre_meta.tables['user'].columns['sContext'].create()
    pre_meta.tables['user'].columns['sUrl'].create()
    pre_meta.tables['user'].columns['sUsrname'].create()
    post_meta.tables['user'].columns['login_emailID'].drop()
    post_meta.tables['user'].columns['login_name'].drop()
