from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView , FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

class taskList(LoginRequiredMixin , ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/allTasks.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: 
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(isDone = False).count()
        return context
    
class taskDetail(LoginRequiredMixin ,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/eachTask.html'


class taskCreate(LoginRequiredMixin ,CreateView):
    model = Task
    fields = ['title' , 'description' ,'isDone']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super(taskCreate ,self ).form_valid(form)

class taskUpdate(LoginRequiredMixin ,UpdateView):
    model = Task
    fields =['title' , 'description' ,'isDone']
    success_url = reverse_lazy('tasks')


class taskDelete(LoginRequiredMixin ,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'base/confirmDelete.html'


    def handle_no_permission(self) -> HttpResponseRedirect:
        return super().handle_no_permission()
    # def noPermission(self , queryset = None):
    #     data = super().get_object(queryset)
    #     if data.user != self.request.user:
    #         return reverse_lazy('tasks')


class loginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True # default is false!

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')
    

class registerView(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self , form):
        user = form.save()
        if user is not None:
            login(self.request , user)
        return super(registerView , self).form_valid(form)