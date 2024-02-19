import funciones
import time
from GestionDePersonal.Trainers import ControllerTrainers

def menu():
    mostrarMenu()
    while True:
        opcion = 0
        opcion = int(input("\n------Ingrese una opcion: "))
        if opcion == 1:
            nuevoTrainer=pedirTrainer()
            if nuevoTrainer != None:
                ControllerTrainers.agregartrainer(nuevoTrainer)
            else:
                print("No se hizo ningun registro")
                pass
            print("Continuando")
            time.sleep(3)
            mostrarMenu()
            pass
        elif opcion == 2:
            buscar = input("Ingrese el id o el DNI del Trainer que desea buscar: ")
            ControllerTrainers.buscartrainer(buscar)
            time.sleep(1)
            mostrarMenu()
            pass
        elif opcion == 3:
            ControllerTrainers.mostrartrainers()
            input("Presione enter para regresar ")
            time.sleep(1)
            mostrarMenu()
            pass

        elif opcion == 4:
            break
    
def mostrarMenu():
    funciones.limpiar_consola()
    print("\n*****************************************************************************************************")
    print("Modulo para la gestion de Trainers")
    print("-- -- -- -- -- -- -- -- -- -- -- --")
    print("\n1. Registrar Un Trainer")
    print("2. Buscar Un Trainer")
    print("3. Mostrar Todos los Trainers")
    print("4. Regresar")
    
def pedirTrainer():
    print("                                                  Cancelar = '"'N'"' ")
    nuevoTrainer = {}
    horarioTrainer = []
    nombres = funciones.ingresar_dato("\nIngrese los nombres del trainer: ")
    if nombres is False:
         return None
    apellidos = funciones.ingresar_dato("\nIngrese los apellidos del trainer: ")
    if apellidos is False:
         return None
    dni = funciones.ingresar_dato("\nIngrese el número de identificación del trainer: ")
    if dni is False:
         return None
    while  True:
        print("                                      INSTRUCCIONES: ingrese la hora en formato 24h   Ejemplo: (18:00 (HH:MM))")
        HoraInicio = funciones.ingresar_dato("\nIngrese la hora de INGRESO: ")
        if HoraInicio is False:
         return None
        HoraFin = funciones.ingresar_dato("\nIngrese la hora de SALIDA: ")
        if HoraFin is False:
         return None
        horarioTrainer.append((HoraInicio+"-"+HoraFin))
        continuar=input("\nDesea Ingresar otra franja horaria?             Ingrese "'"S"'" para SI o CUALQUIER tecla para NO ")
        if continuar.lower() != "s":
            break

    nuevoTrainer = {
        "dni":dni, 
        "nombres":nombres,
        "apellidos":apellidos,
        "horario": horarioTrainer
        }
        
    return nuevoTrainer
