from django.views.generic import ListView, DetailView
from .models import Post, Comment


class BlogView(ListView):
    template_name = "blog/blog.html"
    model = Post.objects.filter(status=True)


class SingleView(DetailView):
    template_name = 