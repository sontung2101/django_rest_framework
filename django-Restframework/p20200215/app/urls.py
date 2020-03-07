"""p20200215 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
urlpatterns = [
    path('hello',hello,name='hello'),
    path('get_all_students',getAllStudent,name='get-all-students'),
    path('add_student',addStudent),
    path('update_student/<int:id>',updateStudent),
    path('update_student_partial/<int:id>',updateStudentParial),
    path('delete_student/<int:id>',deleteStudent),
]
