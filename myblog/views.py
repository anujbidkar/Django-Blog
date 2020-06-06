from django.views.generic import ListView

from .models import Myblog


class Homepage(ListView):
    model = Myblog
    template_name ="home.html"