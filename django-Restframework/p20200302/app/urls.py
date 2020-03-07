from django.urls import path,include
from .views import *
from .views2 import * 
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('hello',hello),
    path('create_student',createStudent,name='create-student'),
    path('get_student/<int:id>',getStudent,name='get-student'),
    path('get_all_students',getAllStudents,name='get-all-student'),
    path('update_student/<int:id>',updateStudent,name='update-student'),
    path('delete_student/<int:id>',deleteStudent,name='delete-student'),
# path('student_list',StudentViewSet.as_view({'get':'list'})), # get all student = view set
# http://127.0.0.1:8000/app/students/broad_cast_message/
# http://127.0.0.1:8000/app/students/1/sick_leave_request/ 
]
router = DefaultRouter()
router.register('students',StudentViewSet)
urlpatterns += router.urls

# localhost:8000/app/students -->GET(list),POST(create)
# localhost:8000/app/students/1 -->GET(item),POST(update)


