from django.urls import path
 
from . import views

urlpatterns = [
    path('works/', views.work_list, name='work-list'),
    path('work/<int:work_id>/', views.work_detail, name='work-detail'),
]