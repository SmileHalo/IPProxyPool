from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey,TEXT,DateTime,CHAR,Float,VARCHAR,BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from Utils import DButil
base = declarative_base()
engine = DButil.get_engine()
class webPage(base):
    def __init__(self):
        self.metadata.create_all(engine)
    __tablename__ = 'webPage'
    webUrl = Column(VARCHAR(70),primary_key=True)
    webName = Column(VARCHAR(260))
    subPageCount = Column(Integer(),default=0)
    proxyCount = Column(Integer(),default=0)
    weight = Column (Integer(),default=100) #权值
    scheme = Column(VARCHAR(20))
    updateTime = Column(DateTime())

class proxy(base):
    def __init__(self):
        self.metadata.create_all(engine)
    __tablename__ = 'proxyList'
    id = Column(Integer,primary_key=True)
    ip = Column(VARCHAR(40))
    port = Column(VARCHAR(20))
    scheme = Column(VARCHAR(20))
    source = Column(VARCHAR(70))
    speed =  Column(Float())
    status = Column(BOOLEAN())
    type = Column(Integer())
    checkCount = Column(Integer(),default=0)
    lastUpdateTime = Column(DateTime())
    createTime = Column(DateTime())