from django.urls import path

from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='adv_home'),
    path('add_advisee/', views.add_advisee, name="add_advisee"),
    path('student_overview/<int:student>/', views.student_overview, name="overview"),
    path('add_advisement/<int:student>/', views.add_advisement, name="advisement"),
    path('add_major/<int:student>/', views.add_major, name="add_major"),
]


