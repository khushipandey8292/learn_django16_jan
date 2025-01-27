from django.urls import path
from . import views
# register_converter(converter.FourDigitYearConverter,'YYYY')
urlpatterns = [
    path('learn_course/',views.course),
    # path('learn_dynamic/<slug:courseid>',views.make_dynamic_url),
    # path('session/<YYYY:Year>/',views.show_details),
    path('inherit_temp1/',views.student_form),
    path('inherit_temp2/',views.teacher_form),
]
