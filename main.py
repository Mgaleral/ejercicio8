import persistencia_json as perj

lista_coches = []
nombre_archivo = input("Cómo se llama el archivo: ")

while True:
    marca = input("Marca del coche: ")
    if marca == "fin":
        break
    modelo = input("Modelo del coche: ")
    combustible = input("Combusituble del coche: ")
    cilindrada = input("Cilindrada del coche: ")

    línea = {}
    línea["Marca coche"] = marca
    línea["Modelo coche"] = modelo
    línea["Combustible coche"] = combustible
    línea["Cilindrada coche"] = cilindrada
    lista_coches.append(línea)

perj.store(lista_coches, nombre_archivo)
lista_coches = []
print("Lista de coches vacia: ", lista_coches)
lista_coches = perj.retrieve(nombre_archivo)
print("Estos son los coches de la lista: ", lista_coches)