import json
import getpass
import hashlib
import funciones
from GestionDePersonal.Campers import ControllerCampers
from GestionDePersonal.Coordinadores import ControllerCoordinadores
from GestionDePersonal.Trainers import ControllerTrainers
def login():
    try:
        # Abrir el archivo JSON de usuarios en modo lectura
        with open('DefaultJsons/usuario.json', 'r') as usuarios_json:
            # Lee el contenido del archivo JSON y carga los datos en una variable Python
            users = json.load(usuarios_json)
            
        print("\nInicio de Sesion")
        usuarioIn = input("Usuario: ")                  
        if funciones.salir(usuarioIn):
            usuarioIn = "salir"
            return usuarioIn
        campers = ControllerCampers.retornarCamper()
        trainers = ControllerTrainers.retornarTrainers()
        coordinadores = ControllerCoordinadores.retronarCoordinadores()
        campers = ControllerCampers.retornarCamper()
        # Verifica si el usuario existe en los datos del archivo JSON
        for usuario in users:
            if usuarioIn == usuario["usuario"]:
                clave = getpass.getpass("Contraseña: ")
                claveIncriptada = encriptar_contraseña(clave)
                # Verifica si la contraseña coincide
                if claveIncriptada == usuario["clave"]:
                    print("Inicio de sesión exitoso")
                    
                    for camper in campers:
                        if usuario["dni"] == camper["dni"]:
                            usuario["rol"] = "camper"
                            print("Inicio de sesión exitoso")
                            return usuario  # Devuelve todos los datos del usuario autenticado

                    for trainer in trainers:
                        if usuario["dni"] == trainer["dni"]:
                            usuario["rol"] = "trainer"
                            print("Inicio de sesión exitoso")
                            return usuario  # Devuelve todos los datos del usuario autenticado

                    for coordinador in coordinadores:
                        if usuario["dni"] == coordinador["dni"]:
                            usuario["rol"] = "coordinador"
                            print("Inicio de sesión exitoso")
                            return usuario  # Devuelve todos los datos del usuario autenticado
                    
                    
                else:
                    print("\nLa contraseña ingresada es incorrecta")
                    return None
        # Si el usuario no se encuentra después de iterar sobre todos los usuarios
        print("\nEl usuario ingresado no existe")
        return None
    except Exception as e:
        print(f"\nHa ocurrido un error: {e}")
        return None
    
def encriptar_contraseña(contraseña):
    sha256 = hashlib.sha256()
    sha256.update(contraseña.encode('utf-8'))
    return sha256.hexdigest()

