"""QsPy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
from QueenPy.views import qsMethodCalled, renderMiao, renderPoupou, renderPhoto
from QueenPy.views import renderTime # add html templates in this way

urlpatterns = [

    path('admin/', admin.site.urls), # to route url path to the function

    path( '', qsMethodCalled), #to use rex to show info_path in URL
    # to remove / slash to fix this router.

    path(r'miao/(\w+)/', renderMiao),

    path(r'poupou/', renderPoupou),

    path(r'showme/', renderPhoto),

    path(r'time/', renderTime),

]


