from django.views.generic import ListView, DetailView
from .models import Snacks,Drinks

class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snacks

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snacks


class DrinkslistView(ListView):
    template_name="drinks_list.html"
    model=Drinks

class DrinksDetailView(DetailView):
    template_name="drinks_detail.html"
    model=Drinks