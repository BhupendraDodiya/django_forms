from django.shortcuts import render,redirect
from django.http import HttpResponse
from .froms import FriendForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import Friend

class index(CreateView):
    model = Friend
    form_class = FriendForm
    template_name = 'index.html'
    success_url = '/table/'

class table(ListView):
    model = Friend
    template_name = 'table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = self.model.objects.all()
        return context
    
class delete(DeleteView):
    model = Friend
    template_name ='delete.html'
    success_url = '/table/'

class update(UpdateView):
    model = Friend
    template_name ='update.html'
    success_url ='/table/'
    fields = ['name','age','active']



    