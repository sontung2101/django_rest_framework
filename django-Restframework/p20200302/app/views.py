from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def hello(request):
    return Response({'message':'Hello'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createStudent(request):
    # data = request.data
    # code = data['code']
    # name = data['name']
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        st = serializer.save()
        return Response({'success':True})
    else:
        return Response({'success':False,'errors':serializer.errors})
    # st = Student(name = name,code = code)
    # st.save()
    # return Response({'success':True})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getStudent(request,id):
    st = Student.objects.get(pk=id)
    serializer = StudentSerializer(st)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllStudents(request):
    studentList = Student.objects.all()
    serializer = StudentSerializer(studentList,many = True) #list -> many = True
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateStudent(request,id):
    st = Student.objects.get(pk=id)
    serializer = StudentSerializer(data = request.data,instance = st)
    if serializer.is_valid():
        st = serializer.save()
        return Response({'success':True})
    else:
        return Response({'success':False,'errors':serializer.errors})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteStudent(request,id):
    st = Student.objects.get(pk = id)
    st.delete()
    return Response({'success':True})

