from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
class BlogListView(ListView):
    model=Post
    template_name='home.html'

class BlogDetailView(DetailView):
    model=Post
    template_name = 'detail_list.html'
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','body','author']
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'

    success_url=reverse_lazy('home')



# Create your views here.
