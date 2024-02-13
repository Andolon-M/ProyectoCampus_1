import json

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

# Función para agregar un nuevo registro al JSON
def crear_registro(data, nuevo_registro):
    data.append(nuevo_registro)
    return data

# Función para buscar un registro por ID
def buscar_registro_por_id(data, id):
    for registro in data:
        if registro['id'] == id:
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