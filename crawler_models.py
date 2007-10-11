from sqlalchemy import Table, Column, MetaData, ForeignKey, types
from sqlalchemy.orm import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///crawler.db', echo=True)

metadata = MetaData()

urls_table = Table('urls', metadata,
    Column('id', types.Integer, primary_key=True),
    Column('url', types.String(500))
)

links_table = Table('links', metadata,
    Column('id', types.Integer, primary_key=True),
    Column('from_id', types.Integer, ForeignKey('urls.id')),
    Column('to_id', types.Integer, ForeignKey('urls.id'))
)

#metadata.create_all(engine)

class Url(object):
    pass

class Link(object):
    pass

mapper(Url, urls_table)
mapper(Link, links_table)