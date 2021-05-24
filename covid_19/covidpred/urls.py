# from django.urls import path
# from covidpred import views

# urlpatterns = [
#     path("", views.home, name="home"),
#     path("hello/<name>",views.hello_there, name="blah")
# ]
from django.urls import path, include
from django.conf import settings
from . import views
from covidpred import views
from django.conf.urls.static import static
 
urlpatterns = [
         path('', views.index, name ='index'),
]