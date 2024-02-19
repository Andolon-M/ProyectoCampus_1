import funciones
import time
from GestionDeRecursos.Salones import ControllerSalones

def menu():
    mostrarMenu()
    while True:
        opcion = 0
        opcion = int(input("\n------Ingrese una opcion: "))
        if opcion == 1:
            nuevoSalon=pedirSalon()
            if nuevoSalon != None:
                ControllerSalones.agregarSalon(nuevoSalon)
            else:
                print("No se hizo ningun registro")
                pass
            print("Continuando")
            time.sleep(3)
            mostrarMenu()
            pass
        elif opcion == 2:
            buscar = input("Ingrese el id o el Nombre del Salon que desea buscar: ")
            ControllerSalones.buscarSalon(buscar)
            time.sleep(1)
            mostrarMenu()
            pass
        elif opcion == 3:
            ControllerSalones.mostrarSalones()
            input("Presione enter para regresar ")
            time.sleep(1)
            mostrarMenu()
            pass

        elif opcion == 4:
            break
    
def mostrarMenu():
    funciones.limpiar_consola()
    print("\n*****************************************************************************************************")
    print("Modulo para la Gestion De Salones")
    print("-- -- -- -- -- -- -- -- -- -- -- --")
    print("\n1. Registrar Un Salon")
    print("2. Buscar Un Salon")
    print("3. Mostrar Todos los Salones")
    print("4. Regresar")
    
def pedirSalon():
    print("                                                  Cancelar = '"'N'"' ")
    nuevoSalon = {}
    nombres = funciones.ingresar_dato("\nIngrese el nombre del Salon: ")
    if nombres is False:
         return None
    
    nuevoSalon = {
        
        "nombre":nombres,
        
        }
        
    return nuevoSalon

