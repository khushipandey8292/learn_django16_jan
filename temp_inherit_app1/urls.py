from django.urls import path
from . import views
urlpatterns = [
    path('learn_home/',views.home),
    path('learn_about/',views.about),
]
