import funciones
import time
from GestionAcademica.GestionDeAdmisiones import Admisiones
from GestionAcademica.GestionDeMatriculas import Matriculas
#from GestionAcademica.GestionDeRutasEntrenamiento import RutasEntrenamiento
from GestionAcademica.GestionNotas import Notas


def menu(auth_data):
    mostrarMenu()
    while True:
        try:
            opcion = int(input("\n------Ingrese una opcion: "))
            if opcion == 1:
                if auth_data["rol"] == "coordinador":
                    Admisiones.menu()
                else:
                    print("Acceso restringido. Solo los coordinadores pueden acceder a esta función.")
                mostrarMenu()
            elif opcion == 2:
                if auth_data["rol"] == "coordinador":
                    Matriculas.menu()
                else:
                    print("Acceso restringido. Solo los coordinadores pueden acceder a esta función.")
                mostrarMenu()
            elif opcion == 3:
                if auth_data["rol"] == "coordinador":
                    #RutasEntrenamiento.menu()
                    pass
                else:
                    print("Acceso restringido. Solo los coordinadores pueden acceder a esta función.")
                mostrarMenu()
            elif opcion == 4:
                Notas.menu(auth_data)
                mostrarMenu()
            elif opcion == 5:
                break
            else:
                print("Opción no válida")
                mostrarMenu()
        except ValueError:
            print("Por favor, ingrese un número válido.")
            mostrarMenu()
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