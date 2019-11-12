from django.urls import path
from . import views

app_name = 'chatbot'
urlpatterns = [
    # path(r'', views.index_template, name='index'),
    # path(r'', views.index_dic, name='index'),
    path('chatbot', views.chatbot, name='chatbot'),
]
