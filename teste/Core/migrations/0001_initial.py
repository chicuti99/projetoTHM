# Generated by Django 4.1.5 on 2023-01-21 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('horario', models.TimeField()),
                ('local', models.CharField(max_length=30)),
                ('intensidade', models.CharField(max_length=13)),
                ('clas', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200)),
                ('uploadedFile', models.FileField(upload_to='Uploaded Files/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
