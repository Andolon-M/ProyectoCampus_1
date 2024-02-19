import CrudJsones as data
from tabulate import tabulate
from funciones import confirmarDecision
from GestionAcademica.GestionDeMatriculas.Grupos import GruposController
import time

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
    tabla_datos = []

    # Obtener el grupo del camper
    grupos = GruposController.leerGrupos()
    grupo_camper = ""
    for grupo in grupos:
        if registro["id"] in grupo["integrantes"]:
            grupo_camper = grupo.get('nombreGrupo', '')
            break

    # Obtener las notas finales de los módulos
    notas_finales_modulos = []
    for modulo in registro['matricula']['ruta']['modulos']:
        notas_finales_modulos.append(f"{modulo['nombre']}: {modulo['notaFinal']}")

    fila = [
        registro.get('id', ''),
        registro.get('dni', ''),
        registro.get('nombres', ''),
        registro.get('apellidos', ''),
        registro['matricula'].get('estado', ''),
        registro['matricula'].get('riesgo', ''),
        grupo_camper,
        ", ".join(notas_finales_modulos)  # Concatenar las notas finales de los módulos en una sola cadena
    ]
    tabla_datos.append(fila)
            
    # Definir los nombres de las columnas
    headers = ["ID", "DNI", "Nombres", "Apellidos", "Riesgo", "ID Grupo", "Notas finales Modulos"]
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def menuBuscarCamper(Camper):
    while True:
        opciones = input("Opciones: ENTER = Regresar   M = Modificar   MAS DETALLES = "'"+"'"\nIngrese una opcion: ")
        if opciones == "":
            break
        elif opciones.lower() == "m":
            campo_modificar = input("Ingrese el nombre del campo que desea modificar ('notas' para actualizar las notas de los módulos): ")
            if campo_modificar.lower() == "notas":
                Camper = cargar_notas_camper(Camper)
                actualizarCamper(Camper["id"], Camper)
            else:
                if campo_modificar.lower() in Camper:
                    print(f"El campo {campo_modificar} actualmente contiene: {Camper[campo_modificar]}")
                    nuevo_valor = input("Ingrese el nuevo valor: ")
                    if confirmarDecision():
                        Camper[campo_modificar] = nuevo_valor
                        actualizarCamper(Camper["id"], Camper)
                        print(f"Se ha actualizado el campo {campo_modificar}.")
                    else:
                        print("Operación cancelada.")
                else:
                    print(f"El campo {campo_modificar} no se encuentra en el Camper.")
       
        elif opciones == "+":
            listar_notas_modulos(Camper)
        else:
            print("La opción ingresada no es válida.")

    return Camper

def cargar_notas_camper(Camper):
    # Calcular las notas según los porcentajes especificados
    porcentaje_proyecto = 0.30
    porcentaje_prueba_teorica = 0.60
    porcentaje_prueba_practica = 0.10
    
    # Imprimir los módulos disponibles para que el usuario elija
    print("Módulos disponibles:")
    for i, modulo in enumerate(Camper['matricula']['ruta']['modulos'], 1):
        print(f"{i}. {modulo['nombre']}")

    # Solicitar al usuario que elija el módulo a modificar
    while True:
        try:
            opcion = int(input("Ingrese el número del módulo que desea modificar: "))
            if 1 <= opcion <= len(Camper['matricula']['ruta']['modulos']):
                break
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número válido.")

    modulo_seleccionado = Camper['matricula']['ruta']['modulos'][opcion - 1]

    # Solicitar las notas al usuario
    nota_proyecto = float(input("Ingrese la nota del proyecto (30%): "))
    nota_prueba_teorica = float(input("Ingrese la nota de la prueba teórica (60%): "))
    nota_prueba_practica = float(input("Ingrese la nota de la prueba práctica (10%): "))

    # Validar que las notas estén en el rango correcto
    if 0 <= nota_proyecto <= 100 and 0 <= nota_prueba_teorica <= 100 and 0 <= nota_prueba_practica <= 100:
        # Calcular la nota final según los porcentajes
        nota_final = nota_proyecto * porcentaje_proyecto + nota_prueba_teorica * porcentaje_prueba_teorica + nota_prueba_practica * porcentaje_prueba_practica

        # Actualizar las notas en la estructura del Camper para el módulo seleccionado
        modulo_seleccionado['notaFinal'] = nota_final
        modulo_seleccionado["notas"] = [nota_proyecto, nota_prueba_teorica, nota_prueba_practica]

        # Imprimir la nota final
        print(f"Nota final del módulo {modulo_seleccionado['nombre']}: {nota_final:.2f}")

        # Retornar el Camper actualizado
        return Camper
    else:
        print("Error: Las notas deben estar en el rango de 0 a 100.")
        return None
    
def listar_notas_modulos(Camper):
    tabla_datos = []
    headers = ["Nombre del módulo", "Nota final", "Notas individuales"]
    
    for modulo in Camper['matricula']['ruta']['modulos']:
        nombre_modulo = modulo['nombre']
        nota_final = f"{modulo['notaFinal']:.2f}"
        notas_individuales = ", ".join(map(str, modulo.get('notas', [])))
        tabla_datos.append([nombre_modulo, nota_final, notas_individuales])
    
    print(tabulate(tabla_datos, headers=headers, tablefmt="rounded_grid", numalign="left", stralign="left"))

def pedirNuevosDatos(diccionario):
    clave = input("Ingrese el nombre del campo que desea actualizar: ")
    if clave in diccionario:
        valor_actual = diccionario[clave]
        nuevo_valor = input(f"Ingrese el nuevo valor para '{clave}' (actual: '{valor_actual}'): ")
        diccionario[clave] = nuevo_valor
    else:
        print("La clave ingresada no existe en el diccionario.")
    
