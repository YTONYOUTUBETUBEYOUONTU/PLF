import itertools

def numeros_infinitos():
    n = 1
    while True:
        yield n
        n += 1
        
numeros = numeros_infinitos()

#Generadores
print(next(numeros))
print(next(numeros))

#compresion de listas
# Compresión de listas con un límite
numeros_cubos = [n**3 for n in itertools.islice(numeros, 10)]
print(numeros_cubos)

def lazy_evaluation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return lambda: result
    return wrapper

@lazy_evaluation
def suma(a, b):
    return a + b

sumatoria = suma(5, 10)
print(sumatoria())
