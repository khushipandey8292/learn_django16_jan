from django.urls import path
from . import views
urlpatterns = [
    path('learn_course/',views.course),
]
