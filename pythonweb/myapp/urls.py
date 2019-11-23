from django.urls import path
from . import views

urlpatterns = [
    # path(r'', views.index_template, name='index'),
    path(r'', views.index_dic, name='index'),
    path('formtest', views.formtest, name='formtest'),
]
