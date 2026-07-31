diccionario = {
    "marca":{
        "nombre": "Toyota",
        "id": 1234
    },
    "modelo":{
        "nombre": "Corolla",
        "id": 5678
    }
}
for x in diccionario:
    if x == "marca":
        print(diccionario[x]["nombre"])
    if x == "modelo":
        print(diccionario[x]["nombre"])

for x,y in diccionario.items():
    print(x,y)

#agregar un nuevo elemento al diccionario
diccionario["año"] = {
    "nombre": "2020",
    "id": 9012
}
#buscar un elemento en el diccionario
print(diccionario["año"]["nombre"])

diccionario_vacio = {}
#agregar un nuevo elemento al diccionario vacio
diccionario_vacio["clave"] = "valor"