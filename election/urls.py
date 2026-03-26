from django.urls import path
from . import views

urlpatterns = [
    # เพิ่มบรรทัดนี้ไว้บนสุดของ list
    path('', views.root_redirect, name='root_redirect'), 
    
    path('<str:username>/', views.index, name='index'),
    path('<str:username>/vote/<int:candidate_id>/', views.cast_vote, name='vote'),
]