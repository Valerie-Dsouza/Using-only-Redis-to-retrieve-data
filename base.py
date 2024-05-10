from assetserver.packages.session import sessions
from assetserver.models.StudentDetailsSchema import StudentDetailsTable
# from sqlalchemy import Integer,Float,String,Column,Table,MetaData

class base(sessions):
    def __init__(self):
        super().__init__()
        # self.session_obj = self.get_session()
        self.studentd= StudentDetailsTable()  
       
        self.session_obj = self.get_session()
        self.redis_client=self.start_redis()
        
        