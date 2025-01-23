from django.urls import path
from . import views
urlpatterns = [
    path('learn_home/',views.home),
    path('learn_about/',views.about),
    path('learn_db/',views.studentinfo),
    path('learn_st_form/',views.showformdata),
    path('success/',views.thanyou),
]
