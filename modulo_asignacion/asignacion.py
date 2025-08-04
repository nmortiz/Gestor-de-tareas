def asignar_tarea(usuario, descripcion, tiempo_estimado, fecha_limite, prioridad):
    return {
        "usuario": usuario,
        "descripcion": descripcion,
        "tiempo_estimado": tiempo_estimado,
        "fecha_limite": fecha_limite,
        "prioridad": prioridad
    }

if __name__ == "__main__":
    tareas = []

    while True:
        print("\n=== MÓDULO DE ASIGNACIÓN DE TAREAS ===")
        print("1. Asignar nueva tarea")
        print("2. Ver tareas asignadas")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario = input("Asignar a (nombre del usuario): ")
            descripcion = input("Descripción de la tarea: ")
            tiempo = int(input("Horas estimadas: "))
            fecha = input("Fecha límite (YYYY-MM-DD): ")
            prioridad = input("Prioridad (Alta, Media, Baja): ")

            tarea = asignar_tarea(usuario, descripcion, tiempo, fecha, prioridad)
            tareas.append(tarea)
            print("\n✅ Tarea asignada correctamente.\n")

        elif opcion == "2":
            if not tareas:
                print("\n📭 No hay tareas asignadas.")
            else:
                print("\n📋 Tareas asignadas:")
                for i, t in enumerate(tareas, 1):
                    print(f"{i}. {t['usuario']} - {t['descripcion']} (Prioridad: {t['prioridad']}, Fecha límite: {t['fecha_limite']})")

        elif opcion == "3":
            print("👋 Saliendo del módulo...")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")
