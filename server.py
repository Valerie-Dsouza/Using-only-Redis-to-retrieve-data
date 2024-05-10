from concurrent import futures
import grpc
from assetproto.student_pb2_grpc import add_StudentServiceServicer_to_server


from assetserver.controller.studentcontroller import StudentController

def server_start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_StudentServiceServicer_to_server(StudentController(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

    
if __name__ == '__main__':
    server_start()      