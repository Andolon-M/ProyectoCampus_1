
import json
import os
import Login as auth

# Crear el directorio si no existe
if not os.path.exists('DefaultJsons'):
    os.makedirs('DefaultJsons')


# Datos para las tablas principales
grupo_camper_data = [
    {"id": 1, "nombreGrupo": "Grupo1"},
    {"id": 2, "nombreGrupo": "Grupo2"}
]

camper_data = [
    {"id": 1, "dni": "12345678A", "nombres": "Juan", "apellidos": "Perez", "direccion": "Calle 123", "dniAcudiente": "87654321B", "celular": "123456789", "fijo": "987654321", "estado": "Inscrito", "riesgo": "Bajo", "idGrupo": 1},
    {"id": 2, "dni": "23456789B", "nombres": "Maria", "apellidos": "Gomez", "direccion": "Avenida 456", "dniAcudiente": "76543210C", "celular": "987654321", "fijo": "123456789", "estado": "Inscrito", "riesgo": "Medio", "idGrupo": 2}
]

trainer_data = [
    {"id": 1, "dni": "34567890C", "nombres": "Pedro", "apellidos": "Lopez"},
    {"id": 2, "dni": "45678901D", "nombres": "Ana", "apellidos": "Martinez"}
]

roles_data = [
    {"id": 1, "nombreRol": "Camper"},
    {"id": 2, "nombreRol": "Trainer"}
]

ruta_entrenamiento_data = [
    {"id": 1, "nombreRuta": "Ruta1"},
    {"id": 2, "nombreRuta": "Ruta2"}
]

modulo_data = [
    {"id": 1, "nombreModulo": "Modulo1", "detalles": "Detalles del Modulo 1", "estado": "Activo", "idRutaEntrenamiento": 1},
    {"id": 2, "nombreModulo": "Modulo2", "detalles": "Detalles del Modulo 2", "estado": "Activo", "idRutaEntrenamiento": 2}
]

matricula_data = [
    {"id": 1, "idCamper": 1, "idTrainer": 1, "idGrupo": 1, "idRutaEntrenamiento": 1, "fechaInicio": "2024-02-01", "fechaFin": "2024-03-01", "idSalon": 1},
    {"id": 2, "idCamper": 2, "idTrainer": 2, "idGrupo": 2, "idRutaEntrenamiento": 2, "fechaInicio": "2024-02-15", "fechaFin": "2024-03-15", "idSalon": 2}
]

salon_data = [
    {"id": 1, "nombre": "Salon1"},
    {"id": 2, "nombre": "Salon2"}
]

# Datos para las tablas de relación
modulo_en_ruta_data = [
    {"id": 1, "idModulo": 1, "idRutaEntrenamiento": 1},
    {"id": 2, "idModulo": 2, "idRutaEntrenamiento": 2}
]

nota_modulo_data = [
    {"id": 1, "idMatricula": 1, "idModulo": 1, "notaFinal": 85},
    {"id": 2, "idMatricula": 2, "idModulo": 2, "notaFinal": 90}
]

# Guardar datos en archivos JSON separados
def guardar_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

guardar_json(grupo_camper_data, 'DefaultJsons/grupo_camper.json')
guardar_json(camper_data, 'DefaultJsons/camper.json')
guardar_json(trainer_data, 'DefaultJsons/trainer.json')
guardar_json(roles_data, 'DefaultJsons/roles.json')
guardar_json(ruta_entrenamiento_data, 'DefaultJsons/ruta_entrenamiento.json')
guardar_json(modulo_data, 'DefaultJsons/modulo.json')
guardar_json(matricula_data, 'DefaultJsons/matricula.json')
guardar_json(salon_data, 'DefaultJsons/salon.json')
guardar_json(modulo_en_ruta_data, 'DefaultJsons/modulo_en_ruta.json')
guardar_json(nota_modulo_data, 'DefaultJsons/nota_modulo.json')

print("Archivos JSON generados correctamente.")


usuarios =[]
#crear contraseña admin encriptada
clave = "admin"
claveEncriptada = auth.encriptar_contraseña(clave)
# Crear el diccionario con la información del usuario
usuarios = [
    {
    "id": 1,
    "usuario": "admin",
    "clave": claveEncriptada,
    "dni": "123456789"
    },
    {
    "id": 2,
    "usuario": "andolon",
    "clave": claveEncriptada,
    "dni": ""
    },
    {
    "id": 3,
    "usuario": "juanperez",
    "clave": claveEncriptada,
    "dni": ""
    }
    ]

# Convertir el diccionario a formato JSON
json_usuario = json.dumps(usuarios, indent=2)

# Guardar el JSON en un archivo
with open('DefaultJsons/usuario.json', 'w') as f:
    f.write(json_usuario)

print("El archivo usuario.json ha sido creado exitosamente con la información del usuario.")



