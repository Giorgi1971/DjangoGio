from django.shortcuts import render
from django.db import models
from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView, DeleteView, DetailView, ListView)
from django.urls import reverse_lazy, reverse
from .models import Author, Group
# from .forms import *
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

class GroupListView(ListView):
    model = Group


class GroupDetailView(DetailView):
    model = Group


class GroupCreateView(CreateView):
    fields = '__all__'
    model = Group


class GroupUpdateView(UpdateView):
    fields = '__all__'
    # fields = ('username', 'first_name', 'last_name', 'image')
    model = Group


# ეს არ შლის სურათს მედია ფაილიდან. გადასაწყვეტია ...
class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('group:groups')