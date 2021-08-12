contendedor = dict()
 
def insertarEnHash(item, key : str):
    key = key.lower()
    key = obtenerClaveHash(item[key])
    if contendedor.get(key):
        contendedor[key].append(item)
    else:
        nuevaLista = list()
        nuevaLista.append(item)
        contendedor[key] = nuevaLista

def insertarDiccionarioEnHash(items : dict, key : str):
    for item in items:
        insertarEnHash(item, key)
    
    return contendedor

def obtenerClaveHash(key : str):
    key = valorDeLaCadena(key)%47
    return key

def valorDeLaCadena(cadena : str):
    valor = 0
    for l in cadena:
        valor += ord(l)
    return valor

def searchInDiccionariobyKey(value , key : str , items: dict):
    
    if items.get(obtenerClaveHash(value)):
        for item in items[obtenerClaveHash(value)]:
            if item[key] == value :
                return item 
    else:
        return 'Item No encontrado'