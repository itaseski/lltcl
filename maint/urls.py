from django.urls import path
 
from . import views


app_name = 'maint'
urlpatterns = [
    path('works/', views.work_list, name='work-list'),
    path('work/<int:work_id>/', views.work_detail, name='work-detail'),
]