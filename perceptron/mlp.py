import numpy as np

class MLP:
    def __init__(self):
        # Configuración inicial de pesos y biases
        self.pesos_capa_oculta = np.random.rand(2, 2)  # 2 entradas a 2 neuronas ocultas
        self.bias_capa_oculta = np.random.rand(2)
        self.pesos_capa_salida = np.random.rand(2, 1)  # 2 ocultas a 1 salida
        self.bias_capa_salida = np.random.rand(1)
    
    def funcion_activacion(self, x):
        """Función sigmoide para activación"""
        return 1 / (1 + np.exp(-x))
    
    def propagacion_adelante(self, entradas):
        """Calcula la salida de la red"""
        self.capa_oculta = self.funcion_activacion(
            np.dot(entradas, self.pesos_capa_oculta) + self.bias_capa_oculta
        )
        self.salida = self.funcion_activacion(
            np.dot(self.capa_oculta, self.pesos_capa_salida) + self.bias_capa_salida
        )
        return self.salida
    
    def entrenar(self, X, y, epocas=10000, tasa_aprendizaje=0.1):
        """Entrenamiento con backpropagation"""
        for _ in range(epocas):
            # Paso hacia adelante
            salida = self.propagacion_adelante(X)
            
            # Backpropagation
            error = y.reshape(-1, 1) - salida
            derivada_salida = error * (salida * (1 - salida))
            
            error_oculto = derivada_salida.dot(self.pesos_capa_salida.T)
            derivada_oculta = error_oculto * (self.capa_oculta * (1 - self.capa_oculta))
            
            # Actualizar pesos y biases
            self.pesos_capa_salida += tasa_aprendizaje * self.capa_oculta.T.dot(derivada_salida)
            self.bias_capa_salida += tasa_aprendizaje * np.sum(derivada_salida, axis=0)
            self.pesos_capa_oculta += tasa_aprendizaje * X.T.dot(derivada_oculta)
            self.bias_capa_oculta += tasa_aprendizaje * np.sum(derivada_oculta, axis=0)
    
    def predecir(self, entradas):
        """Predicción redondeada (0 o 1)"""
        return np.round(self.propagacion_adelante(entradas))