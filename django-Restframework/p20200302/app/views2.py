from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    def list(self,request):
        print('====get all students =====')
        return super().list(request)
    @action(detail = True,methods =['get']) #detail = True --> thao tac tren 1 ban ghi
    def sick_leave_request(self,request,pk):
        st = Student.objects.get(pk= pk)
        return Response({'message':f'Student {st.name} requests sick leave'})
    @action(detail = False,methods =['get'])
    def broad_cast_message(self,request):
        return Response({'message':'Broadcast to all students'})