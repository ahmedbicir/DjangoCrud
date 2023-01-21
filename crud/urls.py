from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add-student/', views.addStudent, name='add-student'),
    path('students/', views.studentList, name='students'),
    path('delete-student/<int:id>/', views.deleteStudent, name='delete-student'),
    path('edit-student/<int:id>/', views.editStudent, name='edit-student'),
    path('sign-in/', views.signIn, name='sign-in'),
    path('sign-up/', views.signUp, name='sign-up'),
    path('exams/', views.exams, name='exams'),
]