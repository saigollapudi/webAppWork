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
    Column('sTimestamp', DateTime),
    Column('sUser_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['sweet'].columns['sTimestamp'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['sweet'].columns['sTimestamp'].drop()
