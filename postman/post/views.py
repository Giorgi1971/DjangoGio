from django.shortcuts import render
from django.db import models
from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView, DeleteView, DetailView, ListView)
from django.urls import reverse_lazy, reverse
from .models import Author, Post
from .forms import *
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
# Create your views here.

class PostListView(ListView):
    paginate_by = 3
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    fields = '__all__'
    model = Post


class PostUpdateView(UpdateView):
    fields = '__all__'
    # fields = ('username', 'first_name', 'last_name', 'image')
    model = Post


# ეს არ შლის სურათს მედია ფაილიდან. გადასაწყვეტია ...
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post:posts')