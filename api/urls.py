from django.urls import path
from . import views

urlpatterns=[
    path('students/', views.student_operations, name="student_operations"),
    path('students/<int:pk>',views.student_operations,name='student_operations_details'),
    # path('students/<int:pk>/update/', update_student, name='update_student'),
    # path('students/<int:pk>/delete/', delete_student, name='delete_student')
]