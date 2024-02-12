import json
from faker import Faker
import random
from datetime import datetime
import os

# Crear el directorio si no existe
if not os.path.exists('DefaultJsones'):
    os.makedirs('DefaultJsones')

fake = Faker()

# Lista para almacenar los campers generados
campers = []

# Generar 10 campers
for _ in range(10):
    camper = {
        "id": fake.random_number(digits=5),
        "dniCamper": fake.random_number(digits=8),
        "nombres": fake.first_name(),
        "apellidos": fake.last_name(),
        "direccion": fake.address(),
        "dniAcudiente": fake.random_number(digits=8),
        "telContacto": {
            "celular": fake.phone_number(),
            "fijo": fake.phone_number()
        },
        "estado": random.choice([True, False]),
        "riesgo": fake.random_element(elements=("Bajo", "Medio", "Alto")),
        "idRol": fake.random_number(digits=1)
    }
    campers.append(camper)

# Escribir los campers en un archivo JSON
with open('DefaultJsones/campers.json', 'w') as f:
    json.dump(campers, f, indent=2)

print("Los datos de los campers han sido guardados en el archivo campers.json.")


# Lista de módulos con sus respectivos detalles
modulos = [
    {"id": 1, "nombreModulo": "Fundamentos de programación", "detalles": ["Introducción a la algoritmia", "PSeInt", "Python"]},
    {"id": 2, "nombreModulo": "Programación Web", "detalles": ["HTML", "CSS", "Bootstrap"]},
    {"id": 3, "nombreModulo": "Programación formal", "detalles": ["Java", "JavaScript", "C#"]},
    {"id": 4, "nombreModulo": "Bases de datos", "detalles": ["Mysql", "MongoDb", "Postgresql"]},
    {"id": 5, "nombreModulo": "Backend", "detalles": ["NetCore", "Spring Boot", "NodeJS", "Express"]}
]

# Convertir la lista de módulos a formato JSON
json_modulos = json.dumps(modulos, indent=2)

# Guardar el JSON en un archivo
with open('DefaultJsones/modulos.json', 'w') as f:
    f.write(json_modulos)

print("El archivo modulos.json ha sido creado exitosamente con la información de los módulos.")


# Lista de roles
roles = [
    {"id": 1, "name": "Camper"},
    {"id": 2, "name": "Trainer"},
    {"id": 3, "name": "Coordinador"}
]

# Convertir la lista de roles a formato JSON
json_roles = json.dumps(roles, indent=2)

# Guardar el JSON en un archivo
with open('DefaultJsones/roles.json', 'w') as f:
    f.write(json_roles)

print("El archivo roles.json ha sido creado exitosamente con la información de roles.")


# Definir la información de las rutas de entrenamiento
rutas_entrenamiento = [
    {
        "id": 1,
        "nombreRuta": "NodeJS",
        "capacidad": 34,
        "duracionClase": "4 horas",
        "HoraInicio": "14:00",
        "HoraFin": "17:30"
    },
    {
        "id": 2,
        "nombreRuta": "Java",
        "capacidad": 34,
        "duracionClase": "4 horas",
        "HoraInicio": "18:00",
        "HoraFin": "22:00"
    },
    {
        "id": 3,
        "nombreRuta": "NetCore",
        "capacidad": 34,
        "duracionClase": "4 horas",
        "HoraInicio": "18:00",
        "HoraFin": "22:00"
    }
]

# Escribir la información de las rutas en un archivo JSON
with open('DefaultJsones/rutas_entrenamiento.json', 'w') as f:
    json.dump(rutas_entrenamiento, f, indent=2)

print("La información de las rutas de entrenamiento ha sido guardada en el archivo rutas_entrenamiento.json.")


# Crear el diccionario con la información del coordinador
coordinador = {
    "id": 1,
    "dniCoordinador": "123456789A",
    "nombre": "Juan Pérez"
}

# Convertir el diccionario a formato JSON
json_coordinador = json.dumps(coordinador, indent=2)

# Guardar el JSON en un archivo
with open('DefaultJsones/coordinador.json', 'w') as f:
    f.write(json_coordinador)

print("El archivo coordinador.json ha sido creado exitosamente con la información del coordinador.")


fake = Faker()

# Generar información para 5 trainers
trainers = []
for i in range(1, 6):
    trainer = {
        "id": i,
        "dniTrainer": fake.random_number(digits=8),
        "nombreTrainer": fake.name(),
        "idRol": 2  # Suponiendo que el id del rol para Trainer es 2
    }
    trainers.append(trainer)

# Convertir la lista de trainers a formato JSON
json_trainers = json.dumps(trainers, indent=2)

# Guardar el JSON de trainers en un archivo
with open('DefaultJsones/trainers.json', 'w') as f:
    f.write(json_trainers)

print("El archivo trainers.json ha sido creado exitosamente con la información de los trainers.")

# Generar información de horarios disponibles para 5 trainers
horarios_trainers = []
for i in range(1, 6):
    horario = {
        "id": i,
        "idTrainer": i,
        "horaInicio": fake.time(pattern="%H:%M"),
        "horaFin": fake.time(pattern="%H:%M")
    }
    horarios_trainers.append(horario)

# Convertir la lista de horarios de trainers a formato JSON
json_horarios_trainers = json.dumps(horarios_trainers, indent=2)

# Guardar el JSON de horarios de trainers en un archivo
with open('DefaultJsones/horarios_trainers.json', 'w') as f:
    f.write(json_horarios_trainers)

print("El archivo horarios_trainers.json ha sido creado exitosamente con la información de los horarios disponibles de los trainers.")



# Lista de salones con sus respectivos nombres
salones = [
    {"id": 1, "nombre": "Sputnik"},
    {"id": 2, "nombre": "Apolo"},
    {"id": 3, "nombre": "Artemis"},
    {"id": 4, "nombre": "Kylab"},
    {"id": 5, "nombre": "Cosmos"},
    {"id": 6, "nombre": "Kepler"},
    {"id": 7, "nombre": "Auditorio"}
]

# Convertir la lista de salones a formato JSON
json_salones = json.dumps(salones, indent=2)

# Guardar el JSON en un archivo
with open('DefaultJsones/salones.json', 'w') as f:
    f.write(json_salones)

print("El archivo salones.json ha sido creado exitosamente con la información de los salones.")



# Generar información de matrículas para 10 campers
matriculas = []
for camper_id in range(1, 11):
    # Seleccionar aleatoriamente una ruta de entrenamiento para el camper
    ruta_entrenamiento = random.choice(rutas_entrenamiento)
    
    matricula = {
        "id": camper_id,
        "idCamper": camper_id,
        "idTrainer": random.randint(1, 5),  # Suponiendo que hay 5 trainers en total
        "idRutaEntrenamiento": ruta_entrenamiento["id"],
        "fechaInicio": fake.date_this_year().strftime('%Y-%m-%d'),
        "fechaFin": fake.date_this_year().strftime('%Y-%m-%d'),
        "salon": fake.random_element(elements=("Sputnik", "Apolo", "Artemis", "Kylab", "Cosmos", "Kepler", "Auditorio"))
    }
    matriculas.append(matricula)

# Convertir la lista de matrículas a formato JSON
json_matriculas = json.dumps(matriculas, indent=2)

# Guardar el JSON en un archivo
with open('DefaultJsones/matriculas.json', 'w') as f:
    f.write(json_matriculas)

print("El archivo matriculas.json ha sido creado exitosamente con la información de las matrículas.")



# Crear el diccionario con la información del usuario
usuario = {
    "id": 1,
    "usuario": "nombre_usuario",
    "contraseña": "contraseña_segura",
    "dni": ""
}

# Convertir el diccionario a formato JSON
json_usuario = json.dumps(usuario, indent=2)

# Guardar el JSON en un archivo
with open('DefaultJsones/usuario.json', 'w') as f:
    f.write(json_usuario)

print("El archivo usuario.json ha sido creado exitosamente con la información del usuario.")



