from django.urls import path
from . import views
app_name = 'staffpanel'

urlpatterns = [
    path('staff', views.StaffDetailView.as_view(), name='staff_panel')
]
