def consultar_historia_clinica(datos):

    print("\n=== HISTORIA CLÍNICA DE PACIENTE ===")
    id_paciente = input("Ingrese el número de identificación del paciente: ").strip()

    paciente_encontrado = None
    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == id_paciente:
            paciente_encontrado = paciente
            break

    if not paciente_encontrado:
        print("\n[Error] No se encontró ningún paciente registrado con esa identificación.")
        return
    print("\n" + "="*40)
    print(" ENCABEZADO - DATOS DEL PACIENTE")
    print("="*40)
    print(f"Identificación : {paciente_encontrado['identificacion']}")
    print(f"Nombres        : {paciente_encontrado['nombres']}")
    print(f"Apellidos      : {paciente_encontrado['apellidos']}")
    print(f"Teléfono       : {paciente_encontrado['telefono']}")
    print(f"E-mail         : {paciente_encontrado['email']}")
    print(f"Dirección      : {paciente_encontrado['direccion']}")
    print(f"Género         : {paciente_encontrado['genero']}")
    print(f"Estado Civil   : {paciente_encontrado['estado_civil']}")
    print("="*40)


    print("\n--- CUERPO DEL HISTORIAL (CONSULTAS MÉDICAS) ---")
    
    consultas_paciente = []
    for consulta in datos["consultas"]:
        if consulta["paciente"]["identificacion"] == id_paciente:
            consultas_paciente.append(consulta)

    if len(consultas_paciente) == 0:
        print("\n[Aviso] El paciente aún no registra consultas o diagnósticos en el sistema.")
        return

    for i, consulta in enumerate(consultas_paciente, start=1):
        print(f"\n Consulta #{i}")
        print(f"   Fecha       : {consulta['fecha']}")
        print(f"   Médico      : {consulta['medico']['nombre_completo']} ({consulta['medico']['email']})")
        print(f"   Síntomas    : {', '.join(consulta['sintomas'])}")
        print(f"   Diagnóstico : {consulta['diagnostico']}")
        print("   Prescripción Médica:")
        
        for med in consulta["prescripcion_medica"]:
            print(f"    - Medicamento: {med['medicamento']} | Cantidad: {med['cantidad']} | Dosis: {med['dosis']} | Tiempo: {med['tiempo_aplicacion']}")
        print("-" * 40)