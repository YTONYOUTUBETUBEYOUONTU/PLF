import pandas as pd
import matplotlib.pyplot as plt


# Decorador para evaluación diferida
def lazy_evaluation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return lambda: result  # Devuelve una función que se ejecuta más tarde
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

@lazy_evaluation
def sales_by_vendedor(values):
    return values.groupby("vendedor")["valor"].sum()

@lazy_evaluation
def sales_by_region(values):
    return values.groupby("region")["valor"].sum()

@lazy_evaluation
def sales_by_product(values):
    return values.groupby("producto")["valor"].sum()

@lazy_evaluation
def plot_sales(values, title):
    values.plot(kind='bar', figsize=(8,5))
    plt.title(title)
    plt.xlabel("Categoría")
    plt.ylabel("Ventas Totales")
    plt.xticks(rotation=45)
    plt.show()

# Cargar datos
filename = 'datos.csv'
data = load_data(filename)

processed_data = process_data(data()) 
plot_histogram(processed_data())  

# Calcular ventas por vendedor, región y producto
vendedor_sales = sales_by_vendedor(data())
region_sales = sales_by_region(data())
product_sales = sales_by_product(data())

# Graficar resultados
plot_sales(vendedor_sales(), "Ventas por Vendedor")
plot_sales(region_sales(), "Ventas por Región")
plot_sales(product_sales(), "Ventas por Producto")

