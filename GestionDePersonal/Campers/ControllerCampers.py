import CrudJsones as data
from tabulate import tabulate
from funciones import confirmarDecision
from GestionAcademica.GestionDeMatriculas.Grupos import GruposController
import time

# Nombre del archivo JSON
archivo_json = 'DefaultJsons/campers.json'

def retornarCamper():
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    return datos

#agregar campers
def agregarCamper(camper):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    #generar la matricula:
    Matricula = {
        "estado": "Inscrito",
        "riesgo": "",
        "idGrupo": {}, # Generar un ID de grupo aleatorio entre 1 y 8
        "pruebaAdmision" : 0,
        "ruta" : {},
        "fechaInicio" : "",
        "FechaDeFinalizacion": ""
}
    camper.update({"matricula":Matricula})
    # Agregar el nuevo registro a los datos existentes  
    datos = data.crear_registro(datos, camper)
    # guardar los datos actualizados en el archivo JSON
    data.escribir_json(archivo_json, datos)

#buscar un registro por ID
def buscarCamper(id_buscar):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    registro_encontrado = data.buscar_registro(datos, id_buscar, "dni")
    if registro_encontrado:
        print("Se encontro coincidencia con el DNI del sigueinte camper\n")
        mostrarCamper(registro_encontrado)
        menuBuscarCamper(registro_encontrado)
    else:
        registro_encontrado = data.buscar_registro_por_id(datos, int(id_buscar))
        if registro_encontrado:
            print("Se encontro coincidencia con el ID del sigueinte camper\n")
            mostrarCamper(registro_encontrado)
            menuBuscarCamper(registro_encontrado)
        else:    
            print("No se encontró ningún registro con el ID o DNI", id_buscar)
            
#buscar y retornar un camper
def buscaryRetornarCamper(id_buscar):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    registro_encontrado = data.buscar_registro(datos, id_buscar, "dni")
    if registro_encontrado:
        print("Se encontro coincidencia con el DNI del sigueinte camper\n")
        mostrarCamper(registro_encontrado)
        return registro_encontrado
    else:
        registro_encontrado = data.buscar_registro_por_id(datos, int(id_buscar))
        if registro_encontrado:
            print("Se encontro coincidencia con el ID del sigueinte camper\n")
            mostrarCamper(registro_encontrado)
            return registro_encontrado
        else:    
            print("No se encontró ningún registro con el ID o DNI", id_buscar)

#actualizar un registro por ID
def actualizarCamper(id_actualizar, nuevos_datos):
    # Leer datos existentes desde el archivo JSON
    datos = data.leer_json(archivo_json)
    if data.actualizar_registro_por_id(datos, id_actualizar, nuevos_datos):
        print("CAMBIOS REALIZADOS.")
    else:
        print("NO SE HICIERON CAMBIOS.")

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

def mostrarCampers():
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
            registro.get('direccion', ''),
            registro.get('dniAcudiente', ''),
            registro.get('celular', ''),
            registro.get('fijo', ''),
            registro['matricula'].get('estado', ''),
            registro['matricula'].get('riesgo', ''),
            registro['matricula']['idGrupo'].get('nombreGrupo', '') if 'idGrupo' in registro['matricula'] else ''
        ]
        tabla_datos.append(fila)
    
    # Definir los nombres de las columnas
    headers = ["ID", "DNI", "Nombres", "Apellidos", "Dirección", "DNI Acudiente", "Celular", "Fijo", "Estado", "Riesgo", "ID Grupo"]
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def mostrarCamper(registro):   
    # Convertir los datos a una lista de listas para tabulate
    grupos = data.leer_json('DefaultJsons/grupo_camper.json')
    grupo_camper = ""
    for grupo in grupos:
        if registro["id"] in grupo["integrantes"]:
            grupo_camper = grupo.get('nombreGrupo', '')
            break
    tabla_datos = []
    fila = [
        registro.get('id', ''),
        registro.get('dni', ''),
        registro.get('nombres', ''),
        registro.get('apellidos', ''),
        registro.get('direccion', ''),
        registro.get('dniAcudiente', ''),
        registro.get('celular', ''),
        registro.get('fijo', ''),
        registro['matricula'].get('estado', ''),
        registro['matricula'].get('riesgo', ''),
        grupo_camper
    ]
    tabla_datos.append(fila)
            
    # Definir los nombres de las columnas
    headers = ["ID", "DNI", "Nombres", "Apellidos", "Dirección", "DNI Acudiente", "Celular", "Fijo", "Estado", "Riesgo", "ID Grupo"]
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def menuBuscarCamper(Camper):
    while True:
        opciones = input("                Opciones:             ENTER = Regresar   M = Modificar   D = Eliminar\nIngrese una opcion: ")
        if opciones == "":
            break
        elif opciones.lower() == "m":
            menuModificar=input("1. Modificar el grupo asignado\n2. Modificar otro campo\n4. Salir\n\nSeleccione una opcion: ")
            if menuModificar == "1":
                grupos = GruposController.leerGrupos()  # Obtener los datos del JSON de grupos
                grupo_camper = ""
                
                for grupo in grupos:
                    if Camper["id"] in grupo["integrantes"]:
                        grupo_camper = grupo
                        break
                
                if grupo_camper:
                    print("Los grupos disponibles son:                              --- Grupo Actual:", grupo_camper["nombreGrupo"], "\n")
                    tabla_datos = []
                    
                    for registro in grupos:
                        fila = [
                            registro.get('id', ''),
                            registro.get('nombreGrupo', ''),
                            registro.get('capacidad', ''),
                            registro.get('idSalon', ''),
                            registro.get('idTrainer', ''),
                            len(registro["integrantes"])
                        ]
                        tabla_datos.append(fila)
                    
                    # Definir los nombres de las columnas
                    headers = ["ID", "Nombre", "Capacidad", "Salon", "Nombre Trainer", "Numero de Integrantes"]
                    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))
                    
                    nuevoGrupo = input("Ingrese el número del nuevo grupo: ")
                    
                    if confirmarDecision():
                        for integrante in grupo_camper["integrantes"]:
                            if integrante == Camper["id"]:
                                grupo_camper["integrantes"].remove(integrante)
                                GruposController.actualizarGrupo(grupo_camper["id"], grupo_camper)
                                print("Se eliminó del grupo anterior")
                                break
                        else:
                            print("No se encontró al integrante en el grupo camper.")
                        
                        for grupo in grupos:
                            if grupo["id"] == int(nuevoGrupo):
                                grupo["integrantes"].append(Camper["id"])
                                GruposController.actualizarGrupo(grupo["id"], grupo)
                                print("Se asignó al nuevo grupo")
                                break
                        else:
                            print("No se encontró el nuevo grupo.")
                    
                    else:
                        print("Regresando...")
                else:
                    print("El camper no está en ningún grupo actualmente.")
                    
                    print("Los grupos disponibles son:")
                    for grupo in grupos:
                        print(f"ID: {grupo['id']}, Nombre: {grupo['nombreGrupo']}")
                    
                    nuevoGrupo = input("Ingrese el número del nuevo grupo: ")
                    nuevoGrupo = int(nuevoGrupo)  # Convertir a entero
                    
                    # Verificar si el grupo seleccionado existe
                    grupo_existente = next((grupo for grupo in grupos if grupo["id"] == nuevoGrupo), None)
                    if grupo_existente:
                        # Agregar al camper al grupo seleccionado
                        grupo_existente["integrantes"].append(Camper["id"])
                        GruposController.actualizarGrupo(grupo_existente["id"], grupo_existente)
                        print("Se asignó al nuevo grupo.")
                    else:
                        print("El grupo seleccionado no existe.")
                    
                break

            elif menuModificar == "2":
                 campoModificar=input("Ingrese el nombre del campo que desea modificar: ")
                 if campoModificar.lower() in Camper:
                    print("El campo",campoModificar," actualmente contiene", Camper[campoModificar.lower()])
                    nuevoEstado = input("Ingrese el nuevo valor: ")                                    
                    print("Esta seguro de cambiar ",campoModificar," del Camper", Camper["dni"], "de", Camper[campoModificar.lower()],"a", nuevoEstado)
                    if confirmarDecision():
                        Camper[campoModificar.lower()]=nuevoEstado.upper()
                        actualizarCamper(Camper["id"], Camper)
                    else:
                        print("Regresando...")
                    break
                 else:
                    print("El campo", campoModificar,"no se encuentra...")
            elif menuModificar == "4":
                break
            else:
                print("La opcion seleccionada no es valida...")
                    
        elif opciones.lower() == "d":
            if confirmarDecision():
                eliminarCamper(Camper["id"])
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
    