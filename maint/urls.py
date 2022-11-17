from django.urls import path
 
from . import views

urlpatterns = [
    path('works/', views.work_list, name='work-list'),
]