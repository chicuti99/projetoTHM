from django.shortcuts import render,redirect
from Core.forms import RegistroForm
from . import models
from Core.models import Registros

# Create your views here.
def home(request):
    data = {}
    data['db'] = Registros.objects.all()
    return render(request,'index.html',data)

def form(request):
    data = {}
    data['form'] = RegistroForm()
    return render(request,'form.html',data)

def upload(request):
    return render(request,'upload.html')

def create(request):
    form = RegistroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        return redirect('form')

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Registros(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Registros.objects.all()

    return render(request, "Core/upload-file.html", context = {
        "files": documents
    })
