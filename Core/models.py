from django.db import models

class Registros(models.Model):
    nome = models.CharField(max_length=30)
    horario = models.TimeField()
    local = models.CharField(max_length=30)
    intensidade = models.CharField(max_length=13)
    clas = models.CharField(max_length=15)
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "img")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)