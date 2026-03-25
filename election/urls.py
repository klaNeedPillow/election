from django.urls import path
from . import views

urlpatterns = [
   
    path('<str:username>/', views.index, name='index'),
   
    path('<str:username>/vote/<int:candidate_id>/', views.cast_vote, name='vote'),
]