from persistencia import cargar_datos
from auth import iniciar_sesion
from pacientes import registrar_paciente
from diagnostico import diagnosticar_paciente
from historia_clinica import consultar_historia_clinica

def main():
    print("=== INICIANDO SISTEMA ACME CLINIC ===")
    
    datos = cargar_datos()
    usuario_actual = None
    
    while usuario_actual is None:
        usuario_actual = iniciar_sesion(datos)
  
    print(f"\n[Sesión Activa] Usuario: {usuario_actual['nombre']} | Rol: {usuario_actual.get('rol', 'administrativo').upper()}")
        
    while True:
        print("\n----------------------------")
        print("     MENÚ PRINCIPAL ACME      ")
        print("------------------------------")
        print("1. Registrar nuevo paciente")
        print("2. Diagnosticar paciente")
        print("3. Consultar historia clínica")
        print("4. Salir del sistema")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            registrar_paciente(datos)
        elif opcion == "2":
            if usuario_actual.get("rol") == "medico":
                diagnosticar_paciente(datos, usuario_actual)
            else:
                print("\n[Acceso Denegado] Solo el personal con rol de 'médico' puede realizar diagnósticos.")
        elif opcion == "3":
            consultar_historia_clinica(datos)
            
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema de ACME Clinic. Hasta luego!")
            break
            
        else:
            print("\n[Error] Opción no válida. Por favor, ingrese un número entre 1 y 4.")

if __name__ == "__main__":
    main()