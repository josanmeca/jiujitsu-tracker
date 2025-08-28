from db import create_tables, add_session, get_all_sessions, delete_session

def menu():
    while True:
        print("\n=== Jiujitsu Training Tracker ===")
        print("1. Añadir sesión")
        print("2. Ver todas las sesiones")
        print("3. Borrar sesión")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            fecha = input("Fecha (YYYY-MM-DD): ")
            tipo = input("Tipo (clase, sparring, competicion): ")
            duracion = int(input("Duración (minutos): "))
            sensaciones = input("Sensaciones (opcional): ")
            add_session(fecha, tipo, duracion, sensaciones)
            print("✅ Sesión añadida correctamente.")

        elif opcion == "2":
            sesiones = get_all_sessions()
            print("\n--- Sesiones registradas ---")
            for s in sesiones:
                print(f"[{s[0]}] {s[1]} | {s[2]} | {s[3]} min | {s[4]}")
        
        elif opcion == "3":
            session_id = int(input("ID de la sesión a borrar: "))
            delete_session(session_id)
            print("🗑️ Sesión eliminada.")

        elif opcion == "4":
            print("👋 Hasta luego!")
            break

        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    create_tables()
    menu()
