import funciones
import time
from GestionDePersonal.Campers import Campers
from GestionDePersonal.Trainers import Trainers
from GestionDePersonal.Coordinadores import Coordinador

def menu():
    mostrarMenu()
    while True:
        opcion = 0
        opcion = int(input("\n------Ingrese una opcion: "))
        if opcion == 1:
            Campers.menu()
            time.sleep(1)
            mostrarMenu()
            pass
        elif opcion == 2:
            Trainers.menu()
            time.sleep(1)
            mostrarMenu()
            pass
        elif opcion == 3:
            Coordinador.menu()
            time.sleep(1)
            mostrarMenu()
            pass

        elif opcion == 4:
            break
    
def mostrarMenu():
    funciones.limpiar_consola()
    print("\n --GESTION DE PERSONAL--\nMenu:")
    print("1. Gestionar Camper")
    print("2. Gestionar Trainers")
    print("3. Gestionar Coordinadores")
    print("4. Regresar")