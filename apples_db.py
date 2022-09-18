from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from datetime import date as d

PATH = f'sqlite:///apples_db.sqlite'

def construct_db():
    engine = create_engine(PATH)

    Base = declarative_base()

    class phrase(Base):
        __tablename__ = 'phrase'
        id = Column(Integer, primary_key=True)
        phrase = Column(String(255))
        playername = Column(String(255))
        date = Column(Date, default=d.today())

    class answer(Base):
        __tablename__ = 'answer'
        id = Column(Integer, primary_key=True)
        phrase_id = Column(Integer, ForeignKey('phrase.id'), nullable=False)
        answer = Column(String(255))
        playername = Column(String(255))
        votes = Column(Integer, default=0)
        date = Column(Date, default=d.today())

    Base.metadata.create_all(engine)

def add_to_db(table, **kwargs):
    engine = create_engine(PATH)
    Base = automap_base()
    Base.prepare(autoload_with=engine)
    element = Base.classes[table](**kwargs)
    with Session(engine) as s:
        s.add(element)
        s.commit()

def query_db(table, **kwargs):
    engine = create_engine(PATH)
    Base = automap_base()
    Base.prepare(autoload_with=engine)
    Table = Base.classes[table]
    with Session(engine) as s:
       q = s.query(Table).filter_by(**kwargs).all()
    return q

def update_db(table, column, value, **kwargs):
    engine = create_engine(PATH)
    Base = automap_base()
    Base.prepare(autoload_with=engine)
    Table = Base.classes[table]
    with Session(engine) as s:
        s.query(Table).filter_by(**kwargs).update({column: value}, synchronize_session=False)
        s.commit()