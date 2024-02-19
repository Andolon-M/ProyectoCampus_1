import Login as auth
import funciones
import os
import time
from GestionDePersonal import GestiondePersonal
from GestionDeRecursos import GestiondeRecursos
from GestionAcademica import GestionAcademica
def mostrar_menu(auth_data):
    while True:
        funciones.limpiar_consola() 
        print(f"\nBienvenido {auth_data['usuario']}, \nMENU PRINCIPAL")
        print("1. Gestión de personal")
        print("2. Gestión de recursos")
        print("3. Gestión académica")
        print("4. Reportes")
        print("5. SALIR")
        opcion = input("\n---------Ingrese una opción: ")
        
        if opcion == "1":
            if auth_data["rol"] == "coordinador":
                GestiondePersonal.menu()
            else:
                print("Acceso denegado: No tiene permiso para esta opción.")
        elif opcion == "2":
            if auth_data["rol"] == "coordinador":
                GestiondeRecursos.menu()
            else:
                print("Acceso denegado: No tiene permiso para esta opción.")
        elif opcion == "3":
            GestionAcademica.menu(auth_data)
        elif opcion == "4":
            if auth_data["rol"] == "coordinador":
                GestionAcademica.menu()
            else:
                print("Acceso denegado: No tiene permiso para esta opción.")
        elif opcion == "5":
            auth_data = None
            break
        else:
            print("Ingrese una opción válida")
        time.sleep(2)

sesion = False

try:
    while True:
        funciones.limpiar_consola()
        print("\n********************************")
        print("|           Bienvenido         |                  **Puede ingresar '"'-999'"' para salir")
        print("******************************** \n")     
        auth_data = auth.login()
        if auth_data == "salir":
            break
        if auth_data == None:
                sesion = False
                time.sleep(1)
        else:
            sesion = True
            time.sleep(1)
            mostrar_menu(auth_data)
except Exception as error:
    print("\nUPS!! Ha habido un error:\n", error, "\nPor favor comunícate con el área de soporte. GRACIAS")









