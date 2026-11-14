def iniciar_sesion(datos):
    print("\n=== INICIO DE SESIÓN ===")
    email_ingresado = input("Ingrese su e-mail: ").strip()
    password_ingresado = input("Ingrese su contraseña: ").strip()

    for usuario in datos["usuarios"]:
        if usuario["email"] == email_ingresado and usuario["password"] == password_ingresado:
            print(f"\n¡Bienvenido/a, {usuario['nombre']} {usuario['apellidos']}!")
            return usuario

    print("\n[Error] E-mail o contraseña incorrectos. Intente nuevamente.")
    return None