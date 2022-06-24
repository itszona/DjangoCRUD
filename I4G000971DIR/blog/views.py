from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from . import models

# Create your views here.
class PostListView(ListView):
    model = models.Post

class PostCreateView(CreateView):
    model = models.Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = models.Post

class PostUpdateView(UpdateView):
    model = models.Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = models.Post
    success_url = reverse_lazy("blog:all")