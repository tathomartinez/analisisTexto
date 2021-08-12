import analisisFunciones
import customHasher
pokemons = [{"name":"bullbasaur","codigo":"1"},
    {"name":"ivysaur","codigo":"3"},
    {"name":"blastoise","codigo":"a"},
    {"name":"charmander","codigo":"7"},
    {"name":"charizard","codigo":"8"},]
hash = dict()
def main():
    print("Works.....")
    text = "Hola Mundo"
    # print(f"Cantidad letras: {analisisFunciones.cantidadLetras(text)}")
    hash = customHasher.insertarDiccionarioEnHash(pokemons, 'name')
    print(hash)
    print(customHasher.searchInDiccionariobyKey('charmander','name',hash))

main()