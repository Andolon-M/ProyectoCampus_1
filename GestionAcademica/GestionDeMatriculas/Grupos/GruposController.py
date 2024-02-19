import CrudJsones as data
from tabulate import tabulate
from funciones import confirmarDecision
from GestionDeRecursos.Salones import ControllerSalones
from GestionDePersonal.Trainers import ControllerTrainers
import time

# Nombre del archivo JSON
archivo_json = 'DefaultJsons/grupo_camper.json'

def leerGrupos():
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    return datos

#agregar Grupos
def agregarGrupo(grupo):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    #generar campo integrantes:
    
    grupo.update({"integrantes":[]})
    # Agregar el nuevo registro a los datos existentes  
    datos = data.crear_registro(datos, grupo)
    # guardar los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#buscar un registro por ID
def buscarGrupo(id_buscar):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    registro_encontrado = data.buscar_registro(datos, id_buscar, "nombreGrupo")
    if registro_encontrado:
        print("Se encontro coincidencia con el NOMBRE del sigueinte grupo\n")
        mostrarGrupo(registro_encontrado)
        menuBuscarGrupo(registro_encontrado)
    else:
        registro_encontrado = data.buscar_registro_por_id(datos, int(id_buscar))
        if registro_encontrado:
            print("Se encontro coincidencia con el ID del sigueinte grupo\n")
            mostrarGrupo(registro_encontrado)
            menuBuscarGrupo(registro_encontrado)
        else:    
            print("No se encontró ningún registro con el ID o NOMBRE", id_buscar)

#actualizar un registro por ID
def actualizarGrupo(id_actualizar, nuevos_datos):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.actualizar_registro_por_id(datos, id_actualizar, nuevos_datos):
        print("CAMBIOS REALIZADOS.")
    else:
        print("NO SE HICIERON CAMBIOS.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#eliminar un registro por ID
def eliminarGrupo(id_eliminar): 
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.eliminar_registro_por_id(datos, id_eliminar):
        print("Registro eliminado correctamente.")
    else:
        print("No se pudo eliminar el registro.")

    # Escribir los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

def mostrarGrupos():
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    
    # Convertir los datos a una lista de listas para tabulate
    tabla_datos = []
    
    for registro in datos:
        
        
        salones = ControllerSalones.retornarSalones()
        nombre_salon =""
        for salon in salones:
            if salon["id"] == registro["idSalon"]:
                nombre_salon = salon.get("nombre", "")
            else:
                nombre_salon = " no se encontro"
                
        trainers = ControllerTrainers.retornarTrainers()
        Nombre_Trainer =""
        for trainer in trainers:
            if trainer["id"] == registro["idTrainer"]:
                nombre_salon = salon.get("nombres", "")
            else:
                nombre_salon = " no se encontro"
                
        fila = [
            registro.get('id', ''),
            registro.get('nombreGrupo', ''),
            registro.get('capacidad', ''),
            nombre_salon,
            registro.get('horaInicio', ''),
            registro.get('horaFin', ''),
            Nombre_Trainer,
            registro.get(len('integrantes'), '')
            
        ]
        tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["Nombre", "Salon", "Capacidad", "Inicio Clase", "Fin Clase", "Trainer", "Numero de integrantes"]
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def mostrarGrupo(registro):   
    tabla_datos = []
    salones = ControllerSalones.retornarSalones()
    nombre_salon =""
    for salon in salones:
        if salon["id"] == registro["idSalon"]:
            nombre_salon = salon.get("nombre", "")
        else:
            nombre_salon = " no se encontro"
            
    trainers = ControllerTrainers.retornarTrainers()
    Nombre_Trainer =""
    for trainer in trainers:
        if trainer["id"] == registro["idTrainer"]:
            nombre_salon = salon.get("nombres", "")
        else:
            nombre_salon = " no se encontro"
            
    fila = [
        registro.get('id', ''),
        registro.get('nombreGrupo', ''),
        registro.get('capacidad', ''),
        nombre_salon,
        registro.get('horaInicio', ''),
        registro.get('horaFin', ''),
        Nombre_Trainer,
        registro.get('integrantes', '')
        
    ]
    tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["Nombre", "Salon", "Capacidad", "Inicio Clase", "Fin Clase", "Trainer", "Celular", "Fijo", "Estado", "Riesgo", "ID Grupo"]
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def menuBuscarGrupo(grupo):
    while True:
        opciones = input("                Opciones:             ENTER = Regresar   M = Modificar   D = Eliminar\nIngrese una opcion: ")
        if opciones == "":
            break
        elif opciones.lower() == "m":
           
            
                 campoModificar=input("Ingrese el nombre del campo que desea modificar: ")
                 if campoModificar.lower() != "integrantes":
                    if campoModificar.lower() in grupo:
                        print("El campo",campoModificar," actualmente contiene", grupo[campoModificar.lower()])
                        nuevoEstado = input("Ingrese el nuevo valor: ")                                    
                        print("Esta seguro de cambiar ",campoModificar," del grupo", grupo["nombreGrupo"], "de", grupo[campoModificar.lower()],"a", nuevoEstado)
                        if confirmarDecision():
                            grupo[campoModificar.lower()]=nuevoEstado.upper()
                            actualizarGrupo(grupo["id"], grupo)
                        else:
                            print("Regresando...")
                        break
                    else:
                        print("El campo", campoModificar,"no se encuentra...")
                    
                 else:
                    print("El campo integrantes no se puede modificar de esta manera")
            
                    
        elif opciones.lower() == "d":
            if confirmarDecision():
                eliminarGrupo(grupo["id"])
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
    