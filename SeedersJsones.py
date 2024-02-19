
import json
import os
import Login as auth
from faker import Faker
import random

# Crear el directorio si no existe
if not os.path.exists('DefaultJsons'):
    os.makedirs('DefaultJsons')


# Datos para las tablas principales
grupo_camper_data = [
    {"id": 1, "nombreGrupo": "S4", "capacidad": 34,  "idSalon": "", "horaInicio":"18:00", "horaFin":"21:00", "idTrainer":"", "integrantes": []},
    {"id": 2, "nombreGrupo": "U3", "capacidad": 34,  "idSalon": "", "horaInicio":"18:00", "horaFin":"21:00", "idTrainer":"", "integrantes": []},
    {"id": 3, "nombreGrupo": "Y3", "capacidad": 34,  "idSalon": "", "horaInicio":"18:00", "horaFin":"21:00", "idTrainer":"", "integrantes": []},
    {"id": 4, "nombreGrupo": "S3", "capacidad": 34,  "idSalon": "", "horaInicio":"18:00", "horaFin":"21:00", "idTrainer":"", "integrantes": []},
    {"id": 5, "nombreGrupo": "U2", "capacidad": 34,  "idSalon": "", "horaInicio":"18:00", "horaFin":"21:00", "idTrainer":"", "integrantes": []},
    {"id": 6, "nombreGrupo": "Y2", "capacidad": 34,  "idSalon": "", "horaInicio":"18:00", "horaFin":"21:00", "idTrainer":"", "integrantes": []},
    {"id": 7, "nombreGrupo": "S2", "capacidad": 34,  "idSalon": "", "horaInicio":"18:00", "horaFin":"21:00", "idTrainer":"", "integrantes": []},
    {"id": 8, "nombreGrupo": "U1", "capacidad": 34,  "idSalon": "", "horaInicio":"18:00", "horaFin":"21:00", "idTrainer":"", "integrantes": []}, 
]

SGDB_Principal =random.choice(["Mysql","MongoDb","Postgresql"])
SGDB_Secundario =random.choice(["Mysql","MongoDb","Postgresql"])
while SGDB_Secundario == SGDB_Principal:
    SGDB_Secundario =random.choice(["Mysql","MongoDb","Postgresql"])
        
modulo_data = [
    {"id": 1, "nombre": "Fundamentos de programación", "description": ["Introducción a la algoritmia,","PSeInt","Python"],"notaFinal": 0 , "notas": [] },
    {"id": 2, "nombre": "Programación Web", "description": ["HTML","CSS ","Bootstrap"],"notaFinal": 0 , "notas": [] },
    {"id": 3, "nombre": "Programación forma", "description": ["Java","JavaScript ","C#"],"notaFinal": 0 , "notas": [] },
    {"id": 4, "nombre": "Bases de datos", "description": {"SGDB Principal": SGDB_Principal, "SGDB Secundario": SGDB_Secundario},"notaFinal": 0 , "notas": [] },
    {"id": 5, "nombre": "Backend" , "description": ["NetCore","Spring Boot ","NodeJS ","Express"],"notaFinal": 0 , "notas": [] },
]

ruta_entrenamiento_data = [
    {"id": 1, "nombreRuta": "NodeJS", "modulos": modulo_data},
    {"id": 2, "nombreRuta": "Java", "modulos": modulo_data},
    {"id": 3, "nombreRuta": "NetCore","modulos": modulo_data},
    
]

fake = Faker()

# Lista para almacenar los registros generados
camper_data = []

# Generar 100 registros
for i in range(1, 101):   
    Matricula = {
        "estado": random.choice(["Inscrito", "En proceso de ingreso", "Aprobado", "Cursando", "Graduado,", "Expulsado", "Retirado"]),
        "riesgo": random.choice(["Bajo", "Medio", "Alto"]),
        "pruebaAdmision" : random.randint(0,100),
        "ruta" : ruta_entrenamiento_data[random.randint(0,2)],
        "fechaInicio" : "",
        "FechaDeFinalizacion": ""
}
    registro = {
        "id": i,
        "dni": fake.random_int(min=10000000, max=99999999),  # Generar un número de DNI aleatorio de 8 dígitos
        "nombres": fake.first_name(),
        "apellidos": fake.last_name(),
        "direccion": fake.address(),
        "dniAcudiente": fake.random_int(min=10000000, max=99999999),  # Generar un número de DNI aleatorio de 8 dígitos para el acudiente
        "celular": fake.phone_number(),
        "fijo": fake.phone_number(),
        "matricula": Matricula
    }
    Matricula = {}
    camper_data.append(registro)

Matricula = {
        "estado": random.choice(["Inscrito", "No inscrito", "En proceso", "Cancelado"]),
        "riesgo": random.choice(["Bajo", "Medio", "Alto"]),
        "pruebaAdmision" : random.randint(0,100),
        "ruta" : ruta_entrenamiento_data[random.randint(0,2)],
        "fechaInicio" : "",
        "FechaDeFinalizacion": ""
}

primerCamperRegistrado = {
    "id": 101,
    "dni": "12345678",
    "nombres": "Juan",
    "apellidos": "Perez",
    "direccion": "Calle 123",
    "dniAcudiente": "87654321B",
    "celular": "123456789",
    "fijo": "987654321",
    "matricula": Matricula
    }

camper_data.append(primerCamperRegistrado)

# Lista para almacenar los registros generados
trainer_data = []
grupos_asignados = set()

# Generar 10 registros
for i in range(1, 8):
    
    
    registro = {
        "id": i,
        "dni": fake.random_int(min=10000000, max=99999999),  # Generar un número de DNI aleatorio de 8 dígitos
        "nombres": fake.first_name(),
        "apellidos": fake.last_name(),
        "horario":[],
        
    }
    trainer_data.append(registro)
    
primerTrainerRegistrado = {
    "id": 11, "dni": "222554477", "nombres": "Andolon", "apellidos": "Mendez","horario":[]
}
trainer_data.append(primerTrainerRegistrado)


#se genera el primer coordinador.
Coordinadores_data = [
    {"id": 1, "dni": "0", "nombres": "ADMIN", "apellidos": ""}
]

roles_data = [
    {"id": 1, "nombreRol": "Coordinador"},
    {"id": 2, "nombreRol": "Trainer"},
    {"id": 3, "nombreRol": "Camper"}
    
]


salon_data = [
    {"id": 1, "nombre": "Auditorio"},
    {"id": 2, "nombre": "Apolo"},
    {"id": 3, "nombre": "Artemis"},
    {"id": 4, "nombre": "Kepler"},
    {"id": 5, "nombre": "Skilab"},
    {"id": 6, "nombre": "Cosmos"},
    {"id": 7, "nombre": "Skilab"},  
]


# Guardar datos en archivos JSON separados
def guardar_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


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
    "dni": "0"
    },
    {
    "id": 2,
    "usuario": "andolon",
    "clave": claveEncriptada,
    "dni": "222554477"
    },
    {
    "id": 3,
    "usuario": "juanperez",
    "clave": claveEncriptada,
    "dni": "12345678"
    }
    ]

guardar_json(usuarios, 'DefaultJsons/usuario.json')
guardar_json(grupo_camper_data, 'DefaultJsons/grupo_camper.json')
guardar_json(camper_data, 'DefaultJsons/campers.json')
guardar_json(trainer_data, 'DefaultJsons/trainers.json')
guardar_json(Coordinadores_data, 'DefaultJsons/coordinadores.json')
guardar_json(roles_data, 'DefaultJsons/roles.json')
guardar_json(ruta_entrenamiento_data, 'DefaultJsons/ruta_entrenamiento.json')
guardar_json(modulo_data, 'DefaultJsons/modulo.json')
guardar_json(salon_data, 'DefaultJsons/salones.json')
print("El archivo usuario.json ha sido creado exitosamente con la información del usuario.")
print("Archivos JSON generados correctamente.")








