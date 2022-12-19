from django.forms import ModelForm

from app_pokemon.apps.owner.models import Owner


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ('nombre', 'edad', 'pais', 'dni')


# class OwnerForm(forms.Form):
#     nombre = forms.CharField(max_length=40)
#     edad = forms.IntegerField(max_value=100)
#     pais = forms.CharField(max_length=25)
#     dni = forms.CharField(max_length=8)
