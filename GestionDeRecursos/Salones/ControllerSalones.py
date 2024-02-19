import CrudJsones as data
from tabulate import tabulate
from funciones import confirmarDecision
import time

# Nombre del archivo JSON
archivo_json = 'DefaultJsons/salones.json'

def retornarSalones():
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    return datos

#agregar salones
def agregarSalon(salon):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    # Agregar el nuevo registro a los datos existentes
    datos = data.crear_registro(datos, salon)
    # guardar los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#buscar un registro por ID
def buscarSalon(id_buscar):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    
    # Intentar buscar coincidencias por nombre
    registro_encontrado = data.buscar_registro(datos, id_buscar, "nombre")
    if registro_encontrado:
        print("Se encontró una coincidencia con el nombre del siguiente salón:\n")
        mostrarSalon(registro_encontrado)
        menuBuscarSalon(registro_encontrado)
        return  # Salir de la función después de encontrar una coincidencia
    
    # Si no se encontraron coincidencias por nombre, intentar buscar por ID
    try:
        id_buscar = int(id_buscar)  # Convertir a entero si es posible
        registro_encontrado = data.buscar_registro_por_id(datos, id_buscar)
        if registro_encontrado:
            print("Se encontró una coincidencia con el ID del siguiente salón:\n")
            mostrarSalon(registro_encontrado)
            menuBuscarSalon(registro_encontrado)
        else:
            print("No se encontró ningún registro con el ID", id_buscar)
    except ValueError:
        print("El valor ingresado no es un ID válido.")


#actualizar un registro por ID
def actualizarSalon(id_actualizar, nuevos_datos):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.actualizar_registro_por_id(datos, id_actualizar, nuevos_datos):
        print("CAMBIOS REALIZADOS.")
    else:
        print("NO SE HICIERON CAMBIOS.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#eliminar un registro por ID
def eliminarSalon(id_eliminar): 
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.eliminar_registro_por_id(datos, id_eliminar):
        print("Registro eliminado correctamente.")
    else:
        print("No se pudo eliminar el registro.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

def mostrarSalones():
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    # Convertir los datos a una lista de listas para tabulate
    tabla_datos = []
    for registro in datos:
        fila = [
            registro.get('id', ''),
            registro.get('nombre', ''),
            
            ]
        tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["ID", "Nombre"]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def mostrarSalon(registro):   
    # Convertir los datos a una lista de listas para tabulate
    tabla_datos = []
    
    fila = [
        registro.get('id', ''),
        registro.get('nombre', '')
    ]
    tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["ID", "Nombre"]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def menuBuscarSalon(salon):
    while True:
        opciones = input("                Opciones:             ENTER = Regresar   M = Modificar   D = Eliminar\nIngrese una opcion: ")
        if opciones == "":
            break
        elif opciones.lower() == "m":           
            campoModificar=input("Ingrese el nombre del campo que desea modificar: ")
            if campoModificar.lower() in salon:
                print("El campo",campoModificar," actualmente contiene", salon[campoModificar.lower()])
                nuevoEstado = input("Ingrese el nuevo valor: ")                                    
                print("Esta seguro de cambiar ",campoModificar," del salon", salon["nombre"], "de", salon[campoModificar.lower()],"a", nuevoEstado)
                if confirmarDecision():
                    salon[campoModificar.lower()]=nuevoEstado.upper()
                    actualizarSalon(salon["id"], salon)
                    break
            else:
                print("Regresando...")
                break
            
                    
        elif opciones.lower() == "d":
            if confirmarDecision():
                eliminarSalon(salon["id"])
                print("Se eliminará el registro")
                time.sleep(1)
                break
        else:
            print("la opcion ingresada no es valida")
                 
def pedirNuevosDatos(diccionario):
    clave = input("Ingrese el nombre del campo que desea actualizar: ")
    if clave in diccionario:
        valor_actual = diccionario[clave]
        nuevo_valor = input(f"Ingrese el nuevo valor para '{clave}' (actual: '{valor_actual}'): ")
        diccionario[clave] = nuevo_valor
    else:
        print("La clave ingresada no existe en el diccionario.")
    