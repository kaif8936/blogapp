from django.views.generic import ListView, DetailView
from .models import Post, About, Contact
from django.utils import timezone

class HomePageView(ListView):
    model = Post
    query_sets = Post.objects.order_by('-created_date')
    template_name = 'home.html'
    paginate_by = 4

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutPageView(ListView):
    model = About
    template_name = 'about.html'

class ContactPageView(ListView):
    model = Contact 
    template_name = 'contact.html'