from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home" ),
    path('livelocation/', views.get_data, name="livelocation")
]
