import os 

#esta funcion se encarga de limpiar la consola para mantener un entrono visual mas llimpio
def limpiar_consola():
    # Comprobar el sistema operativo para determinar el comando de limpieza de la consola adecuado
    if os.name == "posix": # Para sistemas basados en Unix (Linux y macOS)
        os.system("clear")
    elif os.name == "nt": # Para sistemas basados en Windows
        os.system("cls")
    else:
        # Si el sistema operativo no es compatible, simplemente imprimimos líneas en blanco para simular la limpieza de la consola
        print("\n" * 100)
        
def salir(input):
    if input == "-999":
        print("Saliendo...")
        return True
    

def ingresar_dato(mensaje):
    dato = input(mensaje)
    if not dato:
        dato = " "
        return dato
    elif dato.lower() == "n":
        print("se retorna falso")
        return False
    else:
        return dato
    
def confirmarDecision():
    print("Esta acttion NO SE PODRA REVERTIR\n ¿esta seguro?                       ****Ingrese "'"Si"'" o "'"NO"'" ")
    confirmacion= input(":")
    if confirmacion.lower() == "si":
        return True
    else:
        print("No se guardaron los cambios: ")
        return False
    