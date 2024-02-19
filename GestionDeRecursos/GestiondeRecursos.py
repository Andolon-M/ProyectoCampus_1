import funciones
import time
from GestionDeRecursos.Salones import Salones


def menu():
    mostrarMenu()
    while True:
        opcion = 0
        opcion = int(input("\n------Ingrese una opcion: "))
        if opcion == 1:
            Salones.menu()
            time.sleep(1)
            mostrarMenu()
            pass
        elif opcion == 2:
            break
    
def mostrarMenu():
    funciones.limpiar_consola()
    print("\n --GESTION DE RECURSOS--\nMenu:")
    print("1. Gestionar Salones")
    print("2. Regresar")