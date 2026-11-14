import json

ARCHIVO = "acme_clinic.json"

def cargar_datos():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
            
    except FileNotFoundError:
        datos_iniciales = {
            "usuarios": [
                {
                    "identificacion": "0000",
                    "nombre": "Admin",
                    "apellidos": "Administrador",
                    "telefono": "555 000111",
                    "email": "admin@acmeclinic.com",
                    "direccion": "Cl 185 # 26 - 85",
                    "password": "admin",
                    "rol": "administrativo" 
                },
                {
                    "identificacion": "1111",
                    "nombre": "Juan",
                    "apellidos": "Médico",
                    "telefono": "555 222333",
                    "email": "medico@acmeclinic.com",
                    "direccion": "Cl 100 # 10 - 20",
                    "password": "123",
                    "rol": "medico"     }     
            ],
            "pacientes": [],
            "consultas": []
        }
        guardar_datos(datos_iniciales)
        return datos_iniciales

def guardar_datos(datos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
