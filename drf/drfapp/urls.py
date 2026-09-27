
from django.urls import path
from drfapp.views import*



urlpatterns = [
   path("hello/",HelloApi.as_view()),
   path("students/",StudentView.as_view())
]
