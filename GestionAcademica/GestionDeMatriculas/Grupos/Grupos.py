import funciones
import time
from GestionAcademica.GestionDeMatriculas.Grupos import GruposController
from GestionDeRecursos.Salones import ControllerSalones
from GestionDePersonal.Trainers import ControllerTrainers

def menu():
    mostrarMenu()
    while True:
          try:
               opcion = 0
               opcion = int(input("\n------Ingrese una opcion: "))
               if opcion == 2:
                    buscar = input("Ingrese el id o el nombre del grupo que desea buscar: ")
                    GruposController.buscarGrupo(buscar)
                    input("Presione Enter para continuar: ")
                    print("Continuando")
                    time.sleep(1)
                    mostrarMenu()
                    pass
               elif opcion == 1:
                    
                    nuevoGrupo=pedirGrupo()
                    if nuevoGrupo != None:
                         GruposController.agregarGrupo(nuevoGrupo)
                    time.sleep(1)
                    mostrarMenu()
                    pass
               elif opcion == 3:
                    
                    GruposController.mostrarGrupos()
                    input("Precione ente para continuar: ")
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
    print("\n1. o	    Agregar un Grupo")
    print("2. o	    Buscar un grupo")
    print("3. o	    Listar los grupos")
    print("\n4. Regresar")
    
def pedirGrupo():
    print("                                                  Cancelar = '"'N'"' ")
    nuevogrupo = {}
    nombres = funciones.ingresar_dato("\nIngrese el nombre del grupo: ")
    if nombres is False:
         return None
    capacidad = funciones.ingresar_dato("\nIngrese la capacidad del grupo: ")
    if capacidad is False:
         return None
    horaInicio = funciones.ingresar_dato("\nIngrese la hora de incio de clase del grupo    Ejemplo (18:00): ")
    if horaInicio is False:
         return None
    horaFin = funciones.ingresar_dato("\nIngrese la hora de fin de clase del grupo    Ejemplo (22:00): ")
    if horaFin is False:
         return None
    
    trainers=ControllerTrainers.retornarTrainers()
    grupos = GruposController.leerGrupos()
    
    trainers_disponibles = []

    # Filtrar entrenadores disponibles según la hora de inicio y fin
    for trainer in trainers:
        if horaInicio not in trainer["horario"] and horaFin not in trainer["horario"]:
            trainers_disponibles.append(trainer)

    # Verificar si el ID del entrenador ya está registrado en algún grupo con la misma hora de inicio y fin
    trainers_filtrados = []
    for trainer in trainers_disponibles:
        id_trainer = trainer["id"]
        for grupo in grupos:
            if grupo["horaInicio"] == horaInicio and grupo["horaFin"] == horaFin and id_trainer in grupo["idTrainer"]:
                break
        else:
            trainers_filtrados.append(trainer)

    # Mostrar los entrenadores filtrados disponibles
    print("Entrenadores disponibles para el grupo con la hora de inicio", horaInicio, "y la hora de fin", horaFin)
    for trainer in trainers_filtrados:
        print(f"ID: {trainer['id']}, Nombre: {trainer['nombres']} {trainer['apellidos']}")

    SeleccionadoidTrainer = funciones.ingresar_dato("\nIngrese el ID del entrenador seleccionado: ")
    if SeleccionadoidTrainer == "N":
        return None
    
    print("Salones Disponibles")
    salones = ControllerSalones.retornarSalones()
    for salon in salones:
        print("- - - - - - - - ID:", salon['id'], "Nombre:", salon['nombre'])
 
     
    seleccion_salon = funciones.ingresar_dato("\nIngrese el id del salon que quiere selccionar: ")
    if seleccion_salon is False:
         return None
      
    nuevogrupo = {
        "nombreGrupo":nombres, 
        "capacidad":int(capacidad),
        "idSalon": seleccion_salon,
        "horaInicio" : horaInicio,
        "horaFin": horaFin,
        "idTrainer": SeleccionadoidTrainer
        }
        
    return nuevogrupo
