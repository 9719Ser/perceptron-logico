from django import forms

class FormularioPerceptron(forms.Form):
    OPCIONES_COMPUERTA = [
        ('AND', 'AND (Y)'),
        ('OR', 'OR (O)'),
        ('XOR', 'XOR (O exclusivo)'),
    ]
    
    compuerta = forms.ChoiceField(
        choices=OPCIONES_COMPUERTA,
        label="Seleccione la compuerta lógica",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    entrada1 = forms.IntegerField(
        label="Primera entrada (x₁)",
        min_value=0,
        max_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '0 o 1'
        })
    )
    
    entrada2 = forms.IntegerField(
        label="Segunda entrada (x₂)",
        min_value=0,
        max_value=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '0 o 1'
        })
    )