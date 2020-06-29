from django.views.generic import ListView,DetailView
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Myblog
from django.urls import reverse_lazy

class Homepage(ListView):
    model = Myblog
    template_name ="home.html"

class ViewDetail(DetailView):
    model = Myblog
    template_name ="DetailView.html"
    context_object_name = 'batman'

class AddPost(CreateView):
    model = Myblog
    template_name ="addnew.html"
    fields = ['author','title' ,'text']

class EditPost(UpdateView):
    model = Myblog
    template_name ="blog_edit.html"
    fields = ['title' ,'text']

class DeletePost(DeleteView):
    model = Myblog
    template_name ="blog_delete.html"
    context_object_name = 'batman'
    fields = ['title' ,'text']
    success_url = reverse_lazy('home')
