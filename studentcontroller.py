
from assetserver.service.StudentService import StudentService
from assetproto import student_pb2_grpc

class StudentController(student_pb2_grpc.StudentServiceServicer):
    def __init__(self):
        self.service=StudentService()


    def CreateStudent(self,request , context):
        response=self.service.CreateStudent(request)
        return response    
    
    def GetStudent(self,request,context ):
        response=self.service.GetStudent(request)
        return response 
    
    def GetRedisData(self,request,context):
        response=self.service.GetRedis(request)
        return response 
    