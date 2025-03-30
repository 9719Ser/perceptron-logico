import numpy as np

class Perceptron:
    def __init__(self, n_entradas):
        self.pesos = np.random.rand(n_entradas) * 0.1 - 0.05  # Pequeños valores aleatorios
        self.sesgo = np.random.rand() * 0.1 - 0.05
    
    def funcion_activacion(self, x):
        return 1 if x >= 0 else 0
    
    def predecir(self, entradas):
        suma = np.dot(entradas, self.pesos) + self.sesgo
        return self.funcion_activacion(suma)
    
    def entrenar(self, X, y, epocas=1000, tasa_aprendizaje=0.1):
        for _ in range(epocas):
            for entradas, etiqueta in zip(X, y):
                prediccion = self.predecir(entradas)
                error = etiqueta - prediccion
                self.pesos += tasa_aprendizaje * error * entradas
                self.sesgo += tasa_aprendizaje * error