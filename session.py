from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,MetaData
import redis
from signalrcore.hub_connection_builder import HubConnectionBuilder

class sessions():

    def __init__(self):
        self.meta = MetaData()
        self.engine = create_engine('sqlite:///assetserver/studentdata.db', echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.redis_client=redis.Redis(host='localhost',port=6379,db=0)
        self.meta.create_all(self.engine)



    def get_session(self):
        return self.Session()
    
    def start_redis(self):
        return self.redis_client
    
    