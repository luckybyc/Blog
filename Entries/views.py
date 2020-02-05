from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Entry


# Create your views here.
class HomeView(LoginRequiredMixin,ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name = "blog_entries"
    ordering = ['-Entry_date']
    paginate_by = 3
class EntryView(LoginRequiredMixin,DetailView):
     model=Entry
     template_name = 'entries/entry_detail.html'

class CreateEntryView(LoginRequiredMixin,CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['Entry_title','Entry_text']
    def form_valid(self,form):
        form.instance.Entry_author=self.request.user
        return super().form_valid(form)
