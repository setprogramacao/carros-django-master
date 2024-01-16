from django import forms
from cars.models import Brand, Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser')
        return value