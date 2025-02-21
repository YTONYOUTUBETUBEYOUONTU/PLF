import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def lazy_evaluation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return lambda: result
    return wrapper

@lazy_evaluation
def load_data(filename):
    return pd.read_csv(filename)

@lazy_evaluation
def process_data(values):
    return values[values['valor'] > 10]

@lazy_evaluation
def plot_histogram(values):
    values.plot(x='fecha', y='valor', kind='bar')  # Corrección en el gráfico
    plt.show()

# Ejecución para procesar datos
filename = 'datos.csv'
data = load_data(filename) 
processed_data = process_data(data()) 
plot_histogram(processed_data())  