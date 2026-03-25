from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/<int:candidate_id>/', views.cast_vote, name='vote'),
]