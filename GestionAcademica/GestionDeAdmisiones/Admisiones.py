import funciones
import time
from GestionAcademica.GestionDeAdmisiones import AdmisionesController


def menu():
    mostrarMenu()
    while True:
          try:
               opcion = 0
               opcion = int(input("\n------Ingrese una opcion: "))
               if opcion == 1:
                    buscar = input("Ingrese el id o el DNI del camper que desea buscar: ")
                    AdmisionesController.buscarCamper(buscar)
                    input("Presione Enter para continuar: ")
                    print("Continuando")
                    time.sleep(1)
                    mostrarMenu()
                    pass
               elif opcion == 2:
                    print("esta opcion no esta disponible")
                    
                    time.sleep(1)
                    mostrarMenu()
                    pass
               elif opcion == 3:
                    
                    print("esta opcion no esta disponible")
                    time.sleep(1)
                    mostrarMenu()
                    pass

               elif opcion == 4:
                    break
          except Exception as e:
               print("\nUPS!! Ha habido un error:\n", e, "\nPor favor comunícate con el área de soporte. GRACIAS")
    
def mostrarMenu():
    funciones.limpiar_consola()
    print("\n*****************************************************************************************************")
    print("Modulo para la gestion de Admisiones")
    print("-- -- -- -- -- -- -- -- -- -- -- --")
    print("\n1. o	    Cargar o modificar la nota de la prueba de admisión de un CAMPER")
    #print("2. o	    Modificar la nota de la prueba de admisión de un CAMPER")
    #print("2. o	    Modificar la fecha de presentación de la prueba")
    print("\n4. Regresar")
    
