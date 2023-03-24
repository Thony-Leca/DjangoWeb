from django import forms
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView

from .models import *


class ServiceList(ListView):
    model = Servicios
    template_name = 'shop/service/list.html'
    context_object_name = 'servicios'

class ServiceDetail(DetailView):
    model = Servicios
    template_name = 'shop/service/service_detail.html'
    context_object_name = 'servicio'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ['name', 'description', 'price', 'category']
    
    def clean_name(self):
        name = self.cleaned_data('name')
        if Servicios.objects.filter(name=name).exists():
            raise forms.ValidationError('Servicio with this name already exists')
        return name

class ServiceCreate(CreateView):
    model = Servicios
    form_class = ServiceForm
    fields = ['name', 'description', 'price', 'category']
    template_name = 'shop/service/service_create.html'
    success_url = '/'

class Index(TemplateView):
    template_name = 'shop/service/index.html'

class AboutMe(TemplateView):
    template_name = 'shop/service/about_me.html'

class Repo(TemplateView):
    template_name = 'shop/service/repo.html'

def clienteCreate(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        description = request.POST.get('description')
        cliente = Cliente.objects.create(
            name=name,
            last_name=last_name,
            email=email,
            telephone=telephone,
            description=description,
        )
        return redirect('shop:index')
    return render(request, 'shop/service/contact.html')

