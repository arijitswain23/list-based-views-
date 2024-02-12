from django.shortcuts import render
from django.views.generic import ListView,DetailView
from app.models import *
# Create your views here.

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    ordering=['sname']
    #queryset=School.objects.filter(id=1)
    #template_name='app/school_list.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'