from django.forms import ModelForm
from Core.models import Registros

# Create the form class.
class RegistroForm(ModelForm):
    class Meta:
        model = Registros
        fields = ['nome', 'horario', 'local', 'intensidade','clas']