from sqlalchemy import Table, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from .config import database_file

Base = declarative_base()

class User(Base):

    __tablename__ = 'facebook_users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    gender = Column(String)

class FacebookUsers(object):
    def __init__(self):
        db_file = 'sqlite:///{}'.format(database_file)
        engine = create_engine(db_file)
        Base.metadata.create_all(engine)
        db_session = sessionmaker(bind=engine)
        self.session = db_session()
        
    def add(self, user):
        try:
            self.session.add(user)
            self.session.commit()
        except IntegrityError as error:
            self.session.rollback()
            raise error
    
    def remove(self, id):
        user = self.session.query(User).filter_by(id=id).first()
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False
    
    def get_all(self, limit=None):
        return self.session.query(User).limit(limit).all()
