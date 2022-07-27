from django.urls import path
from . import views


urlpatterns = [
    path('mentor-list/',views.MentorCreateView.as_view()),
    path('group-list/',views.GroupView.as_view()),
    path('student-list/',views.StudentView.as_view()),
]
