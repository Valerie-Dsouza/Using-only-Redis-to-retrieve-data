from sqlalchemy import func
from assetproto import student_pb2
from assetserver.packages.base import base
import json
# from assetserver.models import StudentDetailsSchema

class StudentService(base):
    def CreateStudent(self, request):
     with self.session_obj as session:
        self.get_id()
        rollno = self.empcount
        student = self.studentd.studentd.insert().values(rollno=rollno, fullname=request.fullname, standard=request.standard,division=request.division)
        session.execute(student)
        session.commit()
        existingdata = self.redis_client.get("student")
        if existingdata:
            existingsstudents = json.loads(existingdata)
        else:
            existingsstudents = []
        existingsstudents.append({
            'rollno': rollno,
            'fullname': request.fullname,
            'standard': request.standard,
            'division': request.division,
        
        })
        json_data = json.dumps(existingsstudents)
        self.redis_client.setex(f"student_{rollno}",600, json_data)
        return student_pb2.CreateStudentRequest(rollno=rollno, fullname=request.fullname, standard=request.standard, division=request.division)
        
       
    def get_id(self):
        with self.session_obj as session:
            max_rollno=session.query(func.max(self.studentd.studentd.c.rollno)).scalar()
            print(max_rollno)
            if max_rollno is None:
                self.empcount = 1
            else:
                self.empcount=max_rollno +1    
        return self.empcount

    def GetStudent(self, request):
       with self.session_obj as session:
            student_data_redis = self.redis_client.get(f"student_{request.rollno}")
            if student_data_redis:
                    student_data_dict = json.loads(student_data_redis)
                    print("Data fetched from Redis")
                    print(student_data_dict)
                    return student_pb2.CreateStudentRequest(rollno=request.rollno, fullname=student_data_dict["fullname"], standard=student_data_dict["standard"], division=student_data_dict["division"])
        
                   
            else:
                    student_record = session.query(self.studentd.studentd).filter_by(rollno=request.rollno).first()
                    if student_record:
                        student_data_dict = {
                            'rollno': student_record.rollno,
                            'fullname': student_record.fullname,
                            'standard': student_record.standard,
                            'division': student_record.division
                        }
                        json_data = json.dumps(student_data_dict)
                        self.redis_client.setex(f"student_{request.rollno}",600, json_data)
                        return student_pb2.CreateStudentRequest(rollno=request.rollno, fullname=student_data_dict["fullname"], standard=student_data_dict["standard"], division=student_data_dict["division"])
        
                    else:
                        return student_pb2.CreateStudentRequest()
            

   
    def GetRedis(self,request):
          data = self.redis_client.get(request.key)
          print(type(data))
          if data:
              return student_pb2.GetRedisResponse(data=data)
          else:
              return student_pb2.GetRedisResponse(data="Unable to find key!!")
          
    