import funciones
import time
from GestionAcademica.GestionDeAdmisiones import Admisiones
from GestionAcademica.GestionDeMatriculas import Matriculas
#from GestionAcademica.GestionDeRutasEntrenamiento import RutasEntrenamiento
#from GestionAcademica.GestionNotas import GestionNotas


def menu():
    
    mostrarMenu()
    while True:
        try:
            opcion = 0
            opcion = int(input("\n------Ingrese una opcion: "))
            if opcion == 1:
                Admisiones.menu()
                time.sleep(1)
                mostrarMenu()
                pass
            elif opcion == 2:
                Matriculas.menu()
                time.sleep(1)
                mostrarMenu()
                pass
            elif opcion == 3:
                #RutasEntrenamiento.menu()
                time.sleep(1)
                mostrarMenu()
                pass

            elif opcion == 4:
                #GestionNotas.menu()
                time.sleep(1)
                mostrarMenu()
                pass
            elif opcion == 5:
                break
            else:
                print("Opción no valida")
                mostrarMenu()
                pass
        except Exception as e:
            print("\nUPS!! Ha habido un error:\n", e, "\nPor favor comunícate con el área de soporte. GRACIAS")
        
    
def mostrarMenu():
    funciones.limpiar_consola()
    print("\n - -GESTION ACADEMICA --\nMenu:")
    print("1. •	Gestión de Admisiones")
    print("2. •	Gestión de Matriculas")
    print("3. •	Gestión de rutas de entrenamiento")
    print("4. •	Gestión de notas")
    print("5. •	********************** SALIR")