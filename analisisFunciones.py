def cantidadLetras(text):
    cantidad : int = 0
    diccionario : dict = {}
    for letra in text:
        if normalizar(letra) in diccionario:
            diccionario[normalizar(letra)] = diccionario[normalizar(letra)] + 1
        else:
            diccionario[normalizar(letra)] = 1

    return diccionario

def normalizar(letra):
    return letra.lower()