from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
bracket = Table('bracket', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=96)),
    Column('parent_id', Integer),
    Column('user_id', Integer),
    Column('scoring_bracket_id', Integer),
    Column('completed', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['bracket'].columns['completed'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['bracket'].columns['completed'].drop()
