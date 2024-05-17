class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print("Tarea agregada.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            print("Tarea eliminada.")
        else:
            print("Índice de tarea fuera de rango.")

    def mostrar_tareas(self):
        if self.tareas:
            print("Tareas pendientes:")
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea}")
        else:
            print("No hay tareas pendientes.")

def main():
    lista_tareas = ListaDeTareas()

    while True:
        print("\n1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar tareas")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            tarea = input("Ingrese la nueva tarea: ")
            lista_tareas.agregar_tarea(tarea)
        elif opcion == "2":
            indice = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
            lista_tareas.eliminar_tarea(indice)
        elif opcion == "3":
            lista_tareas.mostrar_tareas()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
