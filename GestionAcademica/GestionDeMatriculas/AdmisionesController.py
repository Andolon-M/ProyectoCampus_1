import CrudJsones as data
from tabulate import tabulate
from funciones import confirmarDecision
from GestionAcademica.GestionDeMatriculas.Grupos import GruposController
import time
import funciones

# Nombre del archivo JSON
archivo_json = 'DefaultJsons/campers.json'

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
    #grupos = data.leer_json('DefaultJsons/grupo_camper.json')
    #grupo_camper = ""
    #for grupo in grupos:
    #    if registro["id"] in grupo["integrantes"]:
    #        grupo_camper = grupo.get('nombreGrupo', '')
    #        break
    
    tabla_datos = []
    fila = [
        registro.get('id', ''),
        registro.get('dni', ''),
        registro.get('nombres', ''),
        registro.get('apellidos', ''),
        registro["matricula"].get('pruebaAdmision'),
        registro['matricula'].get('estado', '')
    ]
    tabla_datos.append(fila)
            
    # Definir los nombres de las columnas
    headers = ["ID", "DNI", "Nombres", "Apellidos", "Resultado Prueba de Admision", "Estado"]
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def menuBuscarCamper(Camper): 
    try:
        print("vamos a asignar la nueva nota...                          puede precionar ENTER para ABORTAR")
        nuevaNota = 0
        contador = 0
        while True:
            print("********************* Ingrese notas en el rango valido de 0 a 100")
            print("\nPor favor ingrese la nueva nota de la prueba TEORICA de admision del Camper",Camper["nombres"])
            notaTeorica = funciones.ingresar_dato("\n: ")
            if notaTeorica == ' ':
                break

            print("\nPor favor ingrese la nueva nota de la prueba PRACTICA de admision del Camper",Camper["nombres"])
            notaPractica = funciones.ingresar_dato("\n: ")
            if notaPractica == ' ':
                break

            try:
                nuevaNota = (int(notaPractica) + int(notaTeorica)) / 2
                if 0 < nuevaNota <= 100:
                    break  # Salir del ciclo si nuevaNota está en el rango válido
                else:
                    print("La nota promedio está fuera del rango válido. Por favor, ingrese nuevamente.")
            except ValueError:
                print("El valor ingresado no es válido. Por favor, ingrese un número.")

            
        # se asigna el estado segun lanota de admision del Camper
        if int(nuevaNota) == 0:
            return None
        elif int(nuevaNota) >=  60:
            if Camper["matricula"]["estado"] == "En proceso de ingreso":
                print("segun las notas ingresadas el estado del camper se actualizara "'"APROBADO"'"")                
                if confirmarDecision():
                    Camper["matricula"]["pruebaAdmision"]=nuevaNota
                    Camper["matricula"]["estado"]="APROBADO"
                    actualizarCamper(Camper["id"], Camper)
                else:
                    print("Regresando...") 
            else:
                print("El camper se NO se envuentra en PROCESO DE INSCRIPCION.\nsi aun desea cambiar la nota cambie el ESTADO del camper en la seccion GESTIONAR CAMPERS")
        else:
            if Camper["matricula"]["estado"] == "En proceso de ingreso":
                    print("El estado seleccionado segun las notas ingresadas "'"NO CAMBIARA"'"")                
                    if confirmarDecision():
                        Camper["matricula"]["pruebaAdmision"]=nuevaNota
                        actualizarCamper(Camper["id"], Camper)
                    else:
                        print("Regresando...") 
            else:
                print("El camper se NO se envuentra en PROCESO DE INSCRIPCION.\nsi aun desea cambiar la nota cambie el ESTADO del camper en la seccion GESTIONAR CAMPERS")
                
    except Exception as e:
            print("\nUPS!! Ha habido un error:\n", e, "\nPor favor comunícate con el área de soporte. GRACIAS")

                 
def pedirNuevosDatos(diccionario):
    clave = input("Ingrese el nombre del campo que desea actualizar: ")
    if clave in diccionario:
        valor_actual = diccionario[clave]
        nuevo_valor = input(f"Ingrese el nuevo valor para '{clave}' (actual: '{valor_actual}'): ")
        diccionario[clave] = nuevo_valor
    else:
        print("La clave ingresada no existe en el diccionario.")
    