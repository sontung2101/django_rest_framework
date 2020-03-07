
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

students = [{"id":1,"name":"Nguyen Son Tung","studentNo":"210197"},
            {"id":2,"name":"Nguyen Thi Quyen","studentNo":"181097"},
            {"id":3,"name":"Nguyen Tung Quyen","studentNo":"211897"}]

@api_view(['GET'])
def hello(request):
    return Response({'message':'Hello'})

@api_view(['GET'])
def getAllStudent(request):
    return Response({"students":students})

@api_view(['POST'])
def addStudent(request):
    data = request.data
    student = dict(data)
    maxid = 0 if len(students) == 0 else students[-1]["id"]
    student["id"] = maxid + 1
    students.append(student)
    return Response({"success":True,"student":student})

@api_view(['PUT'])
def updateStudent(request,id):
    student = dict(request.data)
    student["id"] = id
    for i in range(len(students)):
        if students[i]["id"] == id:
            students[i] = student
    return Response({'success':True,"student":student})

@api_view(['PATCH'])
def updateStudentParial(request,id):
    for st in students:
        if st["id"] == id:
            st.update(request.data)
            return Response({"success":True,"student":st})
    return Response({"success":False})


@api_view(['DELETE'])
def deleteStudent(request,id):
    student = None
    for st in students:
        if st["id"] == id:
            student = st
    if student:
        students.remove(student)
        return Response({"success":True})
    else:
        return Response({"success":False})