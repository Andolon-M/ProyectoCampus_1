import CrudJsones as data
from tabulate import tabulate
import funciones
import time

# Nombre del archivo JSON
archivo_json = 'DefaultJsons/trainers.json'

def retornarTrainers():
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    return datos

#agregar trainers
def agregartrainer(trainer):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    # Agregar el nuevo registro a los datos existentes
    datos = data.crear_registro(datos, trainer)
    # guardar los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#buscar un registro por ID
def buscartrainer(id_buscar):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    registro_encontrado = data.buscar_registro(datos, id_buscar, "dni")
    if registro_encontrado:
        print("Se encontro coincidencia con el DNI del sigueinte trainer\n")
        mostrartrainer(registro_encontrado)
        menuBuscartrainer(registro_encontrado)
    else:
        registro_encontrado = data.buscar_registro_por_id(datos, int(id_buscar))
        if registro_encontrado:
            print("Se encontro coincidencia con el ID del sigueinte trainer\n")
            mostrartrainer(registro_encontrado)
            menuBuscartrainer(registro_encontrado)
        else:    
            print("No se encontró ningún registro con el ID o DNI", id_buscar)

#actualizar un registro por ID
def actualizartrainer(id_actualizar, nuevos_datos):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.actualizar_registro_por_id(datos, id_actualizar, nuevos_datos):
        print("CAMBIOS REALIZADOS.")
    else:
        print("NO SE HICIERON CAMBIOS.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#eliminar un registro por ID
def eliminartrainer(id_eliminar): 
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.eliminar_registro_por_id(datos, id_eliminar):
        print("Registro eliminado correctamente.")
    else:
        print("No se pudo eliminar el registro.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

def mostrartrainers():
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
            registro.get('horario', ''),
            ]
        tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["ID", "DNI", "Nombres", "Apellidos", "Horario (Hora de llegada  - Hora de salida)"]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def mostrartrainer(registro):   
    # Convertir los datos a una lista de listas para tabulate
    tabla_datos = []
    
    fila = [
            registro.get('id', ''),
            registro.get('dni', ''),
            registro.get('nombres', ''),
            registro.get('apellidos', ''),
            registro.get('horario', ''),
            ]
    tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["ID", "DNI", "Nombres", "Apellidos", "Horario (Hora de llegada  - Hora de salida)"]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def menuBuscartrainer(trainer):
    while True:
        opciones = input("                Opciones:             ENTER = Regresar   M = Modificar   D = Eliminar\nIngrese una opcion: ")
        if opciones.lower() == "m":
            campoModificar = input("Ingrese el nombre del campo que desea modificar: ")

            

            if campoModificar.lower() in trainer:
                if campoModificar.lower() == "horario":
                    print("El campo", campoModificar, "actualmente contiene:")
                    for i, horario in enumerate(trainer["horario"], 1):
                        print(f"{i}. {horario}")
                    
                    opcion = input("Seleccione la acción a realizar (eliminar, agregar o actualizar): ").lower()
                    
                    if opcion == "eliminar":
                        posicion_eliminar = int(input("Ingrese el número de posición del horario que desea eliminar: ")) - 1
                        
                        if 0 <= posicion_eliminar < len(trainer["horario"]):
                            confirmar_eliminar = input(f"¿Está seguro de eliminar el horario en la posición {posicion_eliminar + 1}? (S/N): ")
                            if confirmar_eliminar.lower() == "s":
                                horario_eliminado = trainer["horario"].pop(posicion_eliminar)
                                actualizartrainer(trainer["id"], trainer)
                                print(f"Horario {horario_eliminado} eliminado exitosamente.")
                            else:
                                print("Cancelando eliminación.")
                        else:
                            print("Posición de horario inválida.")
                    
                    elif opcion == "agregar":
                        while True:
                            print("INSTRUCCIONES: Ingrese la hora en formato 24h (HH:MM)")
                            HoraInicio = funciones.ingresar_dato("\nIngrese la hora de INGRESO: ")
                            if HoraInicio is None:
                                return None
                            HoraFin = funciones.ingresar_dato("\nIngrese la hora de SALIDA: ")
                            if HoraFin is None:
                                return None
                            
                            nuevo_horario = f"{HoraInicio}-{HoraFin}"
                            
                            confirmar_agregar = input(f"¿Está seguro de agregar el nuevo horario {nuevo_horario}? (S/N): ")
                            if confirmar_agregar.lower() == "s":
                                trainer["horario"].append(nuevo_horario)
                                actualizartrainer(trainer["id"], trainer)
                                print("Horario agregado exitosamente.")
                                break
                            else:
                                print("Cancelando agregado.")
                    
                    elif opcion == "actualizar":
                        posicion_modificar = int(input("Ingrese el número de posición del horario que desea actualizar: ")) - 1
                        
                        if 0 <= posicion_modificar < len(trainer["horario"]):
                            print(f"Modificando el horario en la posición {posicion_modificar + 1}")
                            
                            while True:
                                print("INSTRUCCIONES: Ingrese la hora en formato 24h (HH:MM)")
                                HoraInicio = funciones.ingresar_dato("\nIngrese la hora de INGRESO: ")
                                if HoraInicio is None:
                                    return None
                                HoraFin = funciones.ingresar_dato("\nIngrese la hora de SALIDA: ")
                                if HoraFin is None:
                                    return None
                                
                                nuevo_horario = f"{HoraInicio}-{HoraFin}"
                                
                                confirmar_modificacion = input(f"¿Está seguro de cambiar el horario en la posición {posicion_modificar + 1} a {nuevo_horario}? (S/N): ")
                                if confirmar_modificacion.lower() == "s":
                                    trainer["horario"][posicion_modificar] = nuevo_horario
                                    actualizartrainer(trainer["id"], trainer)
                                    print("Horario modificado exitosamente.")
                                    break
                                else:
                                    print("Cancelando modificación.")
                        else:
                            print("Posición de horario inválida.")
                    else:
                        print("Opción no válida.")
                
                else:
                    print("El campo", campoModificar, "actualmente contiene:", trainer[campoModificar.lower()])
                    nuevoEstado = input("Ingrese el nuevo valor: ")
                    print(f"¿Está seguro de cambiar {campoModificar} del trainer {trainer['dni']} de {trainer[campoModificar.lower()]} a {nuevoEstado}?")
                    if funciones.confirmarDecision():
                        trainer[campoModificar.lower()] = nuevoEstado.upper()
                        actualizartrainer(trainer["id"], trainer)
                    else:
                        print("Regresando...")
            else:
                print("El campo", campoModificar, "no se encuentra...")

            break

    
        elif opciones.lower() == "d":
            if funciones.confirmarDecision():
                eliminartrainer(trainer["id"])
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
    