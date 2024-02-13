import json
import getpass
import hashlib


def login():
    try:
        # Abrir el archivo JSON de usuarios en modo lectura
        with open('DefaultJsons/usuario.json', 'r') as usuarios_json:
            # Lee el contenido del archivo JSON y carga los datos en una variable Python
            users = json.load(usuarios_json)
            
        print("\nInicio de Sesion")
        usuarioIn = input("Usuario: ")
        
        # Verifica si el usuario existe en los datos del archivo JSON
        for usuario in users:
            if usuarioIn == usuario["usuario"]:
                clave = getpass.getpass("Contraseña: ")
                claveIncriptada = encriptar_contraseña(clave)
                # Verifica si la contraseña coincide
                if claveIncriptada == usuario["clave"]:
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

