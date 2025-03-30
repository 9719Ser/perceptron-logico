from django.shortcuts import render
from .forms import FormularioPerceptron
from .models import Perceptron
from .mlp import MLP
import numpy as np

def vista_perceptron(request):
    # Datos de entrenamiento
    entradas_ejemplo = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    salidas_and = np.array([0, 0, 0, 1])
    salidas_or = np.array([0, 1, 1, 1])
    salidas_xor = np.array([0, 1, 1, 0])
    
    resultado = None
    compuerta_seleccionada = None
    
    if request.method == 'POST':
        formulario = FormularioPerceptron(request.POST)
        if formulario.is_valid():
            compuerta_seleccionada = formulario.cleaned_data['compuerta']
            entrada_1 = int(formulario.cleaned_data['entrada1'])
            entrada_2 = int(formulario.cleaned_data['entrada2'])
            entrada_actual = np.array([entrada_1, entrada_2])
            
            if compuerta_seleccionada in ['AND', 'OR']:
                modelo = Perceptron(n_entradas=2) 
                salidas_entrenamiento = salidas_and if compuerta_seleccionada == 'AND' else salidas_or
                modelo.entrenar(entradas_ejemplo, salidas_entrenamiento)
                resultado = modelo.predecir(entrada_actual)
            elif compuerta_seleccionada == 'XOR':
                red_neuronal = MLP()
                red_neuronal.entrenar(entradas_ejemplo, salidas_xor)
                resultado = red_neuronal.predecir(entrada_actual.reshape(1, -1))[0][0]
    else:
        formulario = FormularioPerceptron()
    
    return render(request, 'perceptron_form.html', {
        'formulario': formulario,
        'resultado': resultado,
        'compuerta': compuerta_seleccionada
    })