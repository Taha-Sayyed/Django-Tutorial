from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('chai_stores/',views.chai_store_view,name="chai_stores")


]