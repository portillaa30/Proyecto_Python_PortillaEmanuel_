from persistencia import guardar_datos

def diagnosticar_paciente(datos, medico_actual):
    print("\n=== DIAGNOSTICAR PACIENTE ===")
    
    id_paciente = input("Ingrese el número de identificación del paciente: ").strip()
    
    paciente_encontrado = None
    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == id_paciente:
            paciente_encontrado = paciente
            break  
            
    if not paciente_encontrado:
        print("\n[Error] El paciente no está registrado en el sistema. Debe registrarlo primero.")
        return

    print(f"\nPaciente encontrado: {paciente_encontrado['nombres']} {paciente_encontrado['apellidos']}")

    sintomas = []
    print("\n--- Registro de Síntomas ---")
    while True:
        sintoma = input("Ingrese un síntoma (o escriba 'fin' para terminar): ").strip()
        if sintoma.lower() == 'fin':
            break
        if sintoma != "":
            sintomas.append(sintoma)
            
    if len(sintomas) == 0:
        print("\n[Aviso] No se ingresaron síntomas. Operación cancelada.")
        return

    print("\n--- Registro de Diagnóstico ---")
    diagnostico_texto = input("Describa la patología o enfermedad del paciente: ").strip()

    print("\n--- Registro de Prescripción Médica ---")
    medicamentos = []
    while True:
        nombre_med = input("Nombre del medicamento (o escriba 'fin' para terminar): ").strip()
        if nombre_med.lower() == 'fin':
            break
        cantidad = input("Cantidad: ").strip()
        dosis = input("Dosis (cuánto debe tomar diariamente): ").strip()
        tiempo = input("Tiempo de aplicación (días de duración): ").strip()
        
        medicamento = {
            "medicamento": nombre_med,
            "cantidad": cantidad,
            "dosis": dosis,
            "tiempo_aplicacion": tiempo
        }
        medicamentos.append(medicamento)

    while True:
        fecha_consulta = input("Ingrese la fecha en formato AAAA-MM-DD (ej. 2026-06-06): ").strip()
        
        if len(fecha_consulta) == 10 and fecha_consulta[4] == '-' and fecha_consulta[7] == '-':
            anio = fecha_consulta[0:4]
            mes = fecha_consulta[5:7]
            dia = fecha_consulta[8:10]
            
            if anio.isdigit() and mes.isdigit() and dia.isdigit():
                print(f"¡Fecha validada con éxito: {fecha_consulta}!")
                break  
            else:
                print("\n[Error] El año, el mes y el día deben ser números. Intente de nuevo.")
        else:
            print("\n[Error] Formato incorrecto. Respete el formato AAAA-MM-DD (ej. 2026-06-06).")

    nueva_consulta = {
        "fecha": fecha_consulta,
        "paciente": {
            "identificacion": paciente_encontrado["identificacion"],
            "nombre_completo": f"{paciente_encontrado['nombres']} {paciente_encontrado['apellidos']}"
        },
        "medico": {
            "email": medico_actual["email"],
            "nombre_completo": f"{medico_actual['nombre']} {medico_actual['apellidos']}"
        },
        "sintomas": sintomas,
        "diagnostico": diagnostico_texto,
        "prescripcion_medica": medicamentos
    }

    datos["consultas"].append(nueva_consulta)
    guardar_datos(datos)

    print("\n¡Diagnóstico y prescripción médica guardados con éxito en el sistema!")