from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import create_engine
from mysql.connector.errors import IntegrityError
engine = create_engine('mysql+mysqlconnector://root@localhost:3306/IPProxyPool')
DBSession = sessionmaker(bind=engine)
DBScopedSession = scoped_session(sessionmaker(bind=engine))
session = DBSession()
def query_all(obj):
    return session.query(obj).all()
def merge(obj):
    return session.merge(obj)
def add(obj):
    return session.add(obj)
def commit():
    try :
        return session.commit()
    except IntegrityError:
        pass
def get_engine():
    return engine
def add_all(objs):
    return session.add_all(objs)