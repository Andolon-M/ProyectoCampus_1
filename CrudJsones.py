import json
import time

# Función para leer el archivo JSON
def leer_json(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("El archivo no existe.")
        return []
    
# Función para escribir en el archivo JSON
def escribir_json(nombre_archivo, data):
    with open(nombre_archivo, 'w') as file:
        json.dump(data, file, indent=4)
        print("se guardo el nuevo registro")
        time.sleep(1)

# Función para agregar un nuevo registro al JSON
def crear_registro(data, nuevo_registro):
    data=generarID(data, nuevo_registro)
    data.append(nuevo_registro)
    print("se creo el nuevo registro")
    time.sleep(1)
    return data

# Función para buscar un registro por ID
def buscar_registro_por_id(data, id):
    for registro in data:
        if registro['id'] == id:
            return registro
    return None

# Función para buscar un registro por ID
def buscar_registro(data, valor, nomCampo):
    for registro in data:
        if registro[nomCampo] == valor:
            return registro
    return None

# Función para actualizar un registro por ID
def actualizar_registro_por_id(data, id, nuevos_datos):
    for registro in data:
        if registro['id'] == id:
            registro.update(nuevos_datos)
            return True
    return False

# Función para eliminar un registro por ID
def eliminar_registro_por_id(data, id):
    for registro in data:
        if registro['id'] == id:
            data.remove(registro)
            return True
    return False

def generarID(data, nuevo_registro):
    
    # Obtener el próximo ID
    if data:
        nuevo_id = data[-1]["id"] + 1
    else:
        nuevo_id = 1
    
    # Asignar el nuevo ID al nuevo registro
    nuevo_registro["id"] = nuevo_id
    
    # Agregar el nuevo registro a la lista de diccionarios
    print("se genero el id")
    return data
