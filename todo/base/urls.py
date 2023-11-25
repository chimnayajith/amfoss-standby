from django.urls import path
from .views import taskList , taskDetail , taskCreate , taskUpdate , taskDelete , loginView , registerView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/' , loginView.as_view() , name = 'login'),
    path('logout/' , LogoutView.as_view(next_page = 'login') , name = 'logout'),
    path('register/' , registerView.as_view() , name='register'),
    path('',taskList.as_view() ,  name ="tasks"),
    path('task/<int:pk>/',taskDetail.as_view() ,  name ="task"),
    path('create/',taskCreate.as_view() ,  name ="task-create"),
    path('update/<int:pk>/',taskUpdate.as_view() ,  name ="task-update"),
    path('delete/<int:pk>/',taskDelete.as_view() ,  name ="task-delete"),\
]