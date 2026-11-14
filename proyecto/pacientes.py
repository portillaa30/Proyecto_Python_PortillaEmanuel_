from persistencia import guardar_datos

def registrar_paciente(datos):
    print("\n=== REGISTRO DE PACIENTES ===")
    
    identificacion = input("Ingrese el número de identificación del paciente: ").strip()
    
    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            print("\n[Error] Ya existe un paciente registrado con este número de identificación.")
            return

    nombres = input("Ingrese los nombres: ").strip()
    apellidos = input("Ingrese los apellidos: ").strip()
    telefono = input("Ingrese el número de teléfono: ").strip()
    email = input("Ingrese el e-mail: ").strip()
    direccion = input("Ingrese la dirección: ").strip()
    genero = input("Ingrese el género: ").strip()
    estado_civil = input("Ingrese el estado civil: ").strip()

    nuevo_paciente = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil
    }

    datos["pacientes"].append(nuevo_paciente)

    guardar_datos(datos)

    print(f"\n¡Paciente {nombres} {apellidos} registrado con éxito!")