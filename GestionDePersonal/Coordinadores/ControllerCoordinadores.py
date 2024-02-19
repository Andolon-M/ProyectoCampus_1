import CrudJsones as data
from tabulate import tabulate
from funciones import confirmarDecision
import time

# Nombre del archivo JSON
archivo_json = 'DefaultJsons/coordinadores.json'

#agregar coordinadores
def agregarcoordinador(coordinador):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    # Agregar el nuevo registro a los datos existentes
    datos = data.crear_registro(datos, coordinador)
    # guardar los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#buscar un registro por ID
def buscarcoordinador(id_buscar):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    registro_encontrado = data.buscar_registro(datos, id_buscar, "dni")
    if registro_encontrado:
        print("Se encontro coincidencia con el DNI del sigueinte coordinador\n")
        mostrarcoordinador(registro_encontrado)
        menuBuscarcoordinador(registro_encontrado)
    else:
        registro_encontrado = data.buscar_registro_por_id(datos, int(id_buscar))
        if registro_encontrado:
            print("Se encontro coincidencia con el ID del sigueinte coordinador\n")
            mostrarcoordinador(registro_encontrado)
            menuBuscarcoordinador(registro_encontrado)
        else:    
            print("No se encontró ningún registro con el ID o DNI", id_buscar)

#actualizar un registro por ID
def actualizarcoordinador(id_actualizar, nuevos_datos):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.actualizar_registro_por_id(datos, id_actualizar, nuevos_datos):
        print("CAMBIOS REALIZADOS.")
    else:
        print("NO SE HICIERON CAMBIOS.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#eliminar un registro por ID
def eliminarcoordinador(id_eliminar): 
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.eliminar_registro_por_id(datos, id_eliminar):
        print("Registro eliminado correctamente.")
    else:
        print("No se pudo eliminar el registro.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

def mostrarcoordinadores():
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    
    # Convertir los datos a una lista de listas para tabulate
    tabla_datos = []
    for registro in datos:
        fila = [
            registro.get('id', ''),
            registro.get('dni', ''),
            registro.get('nombres', ''),
            registro.get('apellidos', ''),
            ]
        tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["ID", "DNI", "Nombres", "Apellidos"]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def mostrarcoordinador(registro):   
    # Convertir los datos a una lista de listas para tabulate
    tabla_datos = []
    
    fila = [
        registro.get('id', ''),
        registro.get('dni', ''),
        registro.get('nombres', ''),
        registro.get('apellidos', ''),

    ]
    tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["ID", "DNI", "Nombres", "Apellidos"]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def menuBuscarcoordinador(coordinador):
    while True:
        opciones = input("                Opciones:             ENTER = Regresar   M = Modificar   D = Eliminar\nIngrese una opcion: ")
        if opciones.lower() == "m":
            campoModificar=input("Ingrese el nombre del campo que desea modificar: ")
            if campoModificar.lower() in coordinador:
                print("El campo",campoModificar," aactualmente contiene", coordinador[campoModificar.lower()])
                nuevoEstado = input("Ingrese el nuevo valor: ")                                    
                print("Esta seguro de cambiar ",campoModificar," del coordinador", coordinador["dni"], "de", coordinador[campoModificar.lowe()],"a", nuevoEstado)
                if confirmarDecision():
                    coordinador[campoModificar.lower()]=nuevoEstado.upper()
                    actualizarcoordinador(coordinador["id"], coordinador)
                else:
                    print("Regresando...")
                break
            else:
                print("El campo", campoModificar,"no se encuentra...")
    
        elif opciones.lower() == "d":
            if confirmarDecision():
                eliminarcoordinador(coordinador["id"])
                print("Se eliminará el registro")
                time.sleep(1)
                break
        else:
            break
                 
def pedirNuevosDatos(diccionario):
    clave = input("Ingrese el nombre del campo que desea actualizar: ")
    if clave in diccionario:
        valor_actual = diccionario[clave]
        nuevo_valor = input(f"Ingrese el nuevo valor para '{clave}' (actual: '{valor_actual}'): ")
        diccionario[clave] = nuevo_valor
    else:
        print("La clave ingresada no existe en el diccionario.")
    