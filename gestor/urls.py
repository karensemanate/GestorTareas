from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('listar',listar,name='listar'),
    path('crear',crear,name='crear')
    
]