
from django.urls import path
from drfapp.views import*



urlpatterns = [
   path("hello/",HelloApi.as_view()),
#    path("students/",StudentView.as_view()),
   path("students/",StudentModelView.as_view()),
   path("students/<int:id>/",StudentModelDetailView.as_view()),
   path("user/register/",RegisterView.as_view()),
   
#    path("students/<int:id>/",StudentDetailView.as_view())
]
