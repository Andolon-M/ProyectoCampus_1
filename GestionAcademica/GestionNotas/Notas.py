import funciones
import time
from GestionAcademica.GestionNotas import NotasController

def menu(auth_data):
    mostrarMenu()
    while True:
        opcion = 0
        opcion = int(input("\n------Ingrese una opcion: "))
        
        if opcion == 1:
            if auth_data["rol"] == "camper":
               print("NO tiene autorizaicon para usar este modulo")
            else:     
               buscar = input("Ingrese el id o el DNI del camper que desea buscar: ")
               NotasController.buscarCamper(buscar)
               time.sleep(1)
               mostrarMenu()
               pass
        elif opcion == 2:
            NotasController.mostrarCampers()
            input("Presione enter para regresar ")
            time.sleep(1)
            mostrarMenu()
            pass

        elif opcion == 4:
            break
    
def mostrarMenu():
    funciones.limpiar_consola()
    print("\n*****************************************************************************************************")
    print("Modulo para la gestion de notas de Campers")
    print("-- -- -- -- -- -- -- -- -- -- -- --")
    print("1. Subir las notas de Un Camper")
    print("2. Mostrar Todos los campers")
    print("4. Regresar")
    
def pedirCamper():
    print("                                                  Cancelar = '"'N'"' ")
    nuevoCamper = {}
    nombres = funciones.ingresar_dato("\nIngrese los nombres del camper: ")
    if nombres is False:
         return None
    apellidos = funciones.ingresar_dato("\nIngrese los apellidos del camper: ")
    if apellidos is False:
         return None
    dni = funciones.ingresar_dato("\nIngrese el número de identificación del camper: ")
    if dni is False:
         return None
    direccion = funciones.ingresar_dato("\nIngrese la dirección del camper: ")
    if direccion is False:
         return None
    dniAcudiente = funciones.ingresar_dato("\nIngrese el DNI del acudiente del camper: ")
    if dniAcudiente is False:
         return None
    celular = funciones.ingresar_dato("\nIngrese el número de celular del camper: ")
    if celular is False:
         return None
    fijo = funciones.ingresar_dato("\nIngrese el número de teléfono fijo del camper: ")
    if fijo is False:
         return None
    
    nuevoCamper = {
        "dni":dni, 
        "nombres":nombres,
        "apellidos":apellidos,
        "direccion":direccion,
        "dniAcudiente":dniAcudiente,
        "celular":celular,
        "fijo":fijo
        }
        
    return nuevoCamper

