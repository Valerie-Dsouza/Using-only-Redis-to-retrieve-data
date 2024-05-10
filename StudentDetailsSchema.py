from marshmallow import Schema, fields
from sqlalchemy import Integer,Float,String,Column,Table,MetaData




class StudentDetailsTable:
    def __init__(self):
        self.meta = MetaData()
        self.studentd = Table(
            'studentdetails', self.meta,
            Column('rollno', Integer, primary_key=True),
            Column('fullname', String),
            Column('standard', Integer),
            Column('division', String)
        )
    class StudentDetailsSchema(Schema):
     rollno = fields.Integer()
     fullname = fields.String()
     standard = fields.Integer()
     division = fields.String()
    
        
