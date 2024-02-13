import CrudJsones as data

# Nombre del archivo JSON
archivo_json = 'DefaultJsons/campers.json'

#agregar campers
def agregarCamper(camper):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    # Agregar el nuevo registro a los datos existentes
    datos = data.crear_registro(datos, camper)
    # guardar los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#buscar un registro por ID
def buscarCamper(id_buscar):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    registro_encontrado = data.buscar_registro_por_id(datos, id_buscar)
    if registro_encontrado:
        print("Registro encontrado:", registro_encontrado)
    else:
        print("No se encontró ningún registro con el ID", id_buscar)

#actualizar un registro por ID
def actualizarCamper(id_actualizar, nuevos_datos):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.actualizar_registro_por_id(datos, id_actualizar, nuevos_datos):
        print("Registro actualizado correctamente.")
    else:
        print("No se pudo actualizar el registro.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#eliminar un registro por ID
def eliminarCamper(id_eliminar): 
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.eliminar_registro_por_id(datos, id_eliminar):
        print("Registro eliminado correctamente.")
    else:
        print("No se pudo eliminar el registro.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)
