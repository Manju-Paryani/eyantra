"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include,path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# urlpatterns = [path("", include("covidpred.urls")),
#     path('admin/', admin.site.urls),
#     path("",include("covidpred.urls")),
# ]

from django.contrib import admin
from django.urls import path, include
from covidpred import views as user_view
from django.contrib.auth import views as auth
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

	path('admin/', admin.site.urls),

	##### user related path##########################
	path('', include('covidpred.urls')),
	path('login/', user_view.Login, name ='login'),
	path('logout/', auth.LogoutView.as_view(template_name ='covidpred/index.html'), name ='logout'),
	path('register/', user_view.register, name ='register'),
    path('result/',user_view.result,name= 'result'),
    path('about/',user_view.about,name='about')

]
urlpatterns+= staticfiles_urlpatterns()

