import grpc
import json
from assetproto import student_pb2
from assetproto import student_pb2_grpc
from flask import Flask, jsonify, request

app = Flask(__name__)

channel = grpc.insecure_channel('localhost:50051')
stub = student_pb2_grpc.StudentServiceStub(channel)



@app.route('/createstudent',methods=['POST'])
def CreateStudent():
    
    req_data = request.get_json()
    fullname = req_data['fullname']
    standard = req_data['standard']
    division = req_data['division']

    create_request = student_pb2.CreateStudentRequest(fullname=fullname, standard=standard, division=division)
    response = stub.CreateStudent(create_request)
    if response:
      return jsonify({'message': 'Student details created successfully'}), 200
    else:
            return jsonify({'error': 'Failed to fetch student records: {}'.format(str(response))}), 500
    

@app.route('/getstudent', methods=['GET'])
def GetStudent():
    req_data = request.get_json()
    rollno = req_data.get('rollno')
    request_message_emp = student_pb2.GetStudentRequest(rollno=rollno)
    response_stud = stub.GetStudent(request_message_emp)
    employee_details = {
        'rollno': response_stud.rollno,
        'fullname': response_stud.fullname,
        'standard': response_stud.standard,
        'division': response_stud.division
    }
    
    return jsonify({'employee_details': employee_details}), 200



@app.route('/getredis',methods=['POST'])
def GetRedisdata():
    req_data=request.get_json()
    key=req_data['key']
    request_message = student_pb2.GetRedisRequest(key=key)
    response = stub.GetRedisData(request_message)
    if response:
     return jsonify({'data': response.data}), 200
    else:
     return jsonify({'message': 'No data found'}), 500


if __name__ == '__main__':
    app.run(debug=True)
