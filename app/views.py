from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Main
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic import DeleteView
from django.views.generic import CreateView

from .forms import MainEditFrom, CreateUserForm


class Register(FormView):
    template_name = 'html/register.html'
    form_class = CreateUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(Register, self).get(*args, **kwargs)


class LoginPage(LoginView):
    template_name = 'html/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')


class CreateMain(LoginRequiredMixin, CreateView):
    model = Main
    fields = ['title', 'img']
    success_url = reverse_lazy('main')
    template_name = 'html/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateMain, self).form_valid(form)


class DeleteMain(LoginRequiredMixin, DeleteView):
    model = Main
    template_name = 'html/delete.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('main')


class MainEdit(LoginRequiredMixin, UpdateView):
    template_name = "html/edit.html"
    model = Main
    form_class = MainEditFrom
    success_url = reverse_lazy('main')
    context_object_name = 'todo'
    # def form_valid(self, form):
    #     form.save()
    #     return reverse_lazy('main')


class MainDetail(LoginRequiredMixin, DetailView):
    template_name = "html/detail.html"
    model = Main
    context_object_name = "todo"


class MainView(LoginRequiredMixin, ListView):
    template_name = "html/main.html"
    model = Main
    context_object_name = 'todo'

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-created_data')
        return ordering
