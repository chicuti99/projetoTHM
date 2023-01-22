from django.shortcuts import render,redirect
from Core.forms import RegistroForm
from . import models
from Core.models import Registros
from PIL import Image
from django.conf import settings
import os
from django.http import HttpResponse

# Create your views here.
def home(request):
    data = {}
    data['db'] = Registros.objects.all()
    return render(request,'index.html',data)

def form(request):
    data = {}
    data['form'] = RegistroForm()
    return render(request,'form.html',data)

def up(request):
    return render(request,'upload.html')

def create(request):
    form = RegistroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        return redirect('form')

def upload(request):
    if request.method == "GET":
        return render(request, 'upload.html')
    elif request.method == "POST":
        file = request.FILES.get('my_file')
        img = Image.open(file)
        path =  os.path.join(settings.BASE_DIR, f'media/{file.name}')
        img = img.save(path)

        print(file)
        return render(request,'index.html')