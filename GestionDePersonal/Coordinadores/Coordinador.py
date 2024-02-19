import funciones
import time
from GestionDePersonal.Coordinadores import ControllerCoordinadores

def menu():
    mostrarMenu()
    while True:
        opcion = 0
        opcion = int(input("\n------Ingrese una opcion: "))
        if opcion == 1:
            nuevocoordinador=pedircoordinador()
            if nuevocoordinador != None:
                ControllerCoordinadores.agregarcoordinador(nuevocoordinador)
            else:
                print("No se hizo ningun registro")
                pass
            print("Continuando")
            time.sleep(3)
            mostrarMenu()
            pass
        elif opcion == 2:
            buscar = input("Ingrese el id o el DNI del coordinador que desea buscar: ")
            ControllerCoordinadores.buscarcoordinador(buscar)
            time.sleep(1)
            mostrarMenu()
            pass
        elif opcion == 3:
            ControllerCoordinadores.mostrarcoordinadores()
            input("Presione enter para regresar ")
            time.sleep(1)
            mostrarMenu()
            pass

        elif opcion == 4:
            break
    
def mostrarMenu():
    funciones.limpiar_consola()
    print("\n*****************************************************************************************************")
    print("Modulo para la gestion de coordinadores")
    print("-- -- -- -- -- -- -- -- -- -- -- --")
    print("\n1. Registrar Un coordinador")
    print("2. Buscar Un coordinador")
    print("3. Mostrar Todos los coordinadores")
    print("4. Regresar")
    
def pedircoordinador():
    print("                                                  Cancelar = '"'N'"' ")
    nuevocoordinador = {}
    nombres = funciones.ingresar_dato("\nIngrese los nombres del coordinador: ")
    if nombres is False:
         return None
    apellidos = funciones.ingresar_dato("\nIngrese los apellidos del coordinador: ")
    if apellidos is False:
         return None
    dni = funciones.ingresar_dato("\nIngrese el número de identificación del coordinador: ")
    if dni is False:
         return None
    
    nuevocoordinador = {
        "dni":dni, 
        "nombres":nombres,
        "apellidos":apellidos,
        }
        
    return nuevocoordinador
