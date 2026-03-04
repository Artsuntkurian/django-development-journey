from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

from django.views.generic import FormView,ListView,TemplateView


class TVWData(TemplateView):
    template_name='TVWData.html'
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Athul George'
        ECDO['age']=23
        ECDO['gender']='M'
        return ECDO


class InsertwithTV(TemplateView):
    template_name='InsertwithTV.html'
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ETMFO=TopicMF()
        ECDO['ETMFO']=ETMFO
        return ECDO

    def post(self,request):

        TMFO=TopicMF(request.POST)

        if TMFO.is_valid():
            TMFO.save()
            return HttpResponse('Data Inserted')
        else:
            return HttpResponse('Data Invalid')






class InsertwithFV(FormView):
    form_class=TopicMF
    template_name='InsertwithFV.html'
    
    
    def form_valid(self, form):
        form.save()
        return HttpResponse('Data Inserted')



class display_topic(ListView):
    model=Topics
#   queryset=
    context_object_name='QSLTO'
    template_name='display_topic.html'
#   ordering=['topic_name']

