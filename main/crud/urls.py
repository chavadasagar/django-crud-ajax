from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('savestd',views.savestd,name='savestd'),
    path('showallstd',views.showallstd,name='showallstd'),
    path('deletestd',views.deletestd,name='deletestd'),
    path('updatestd',views.updatestd,name='updatestd'),
    path('update',views.update,name='update'),


]
