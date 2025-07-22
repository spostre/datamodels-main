import ui.students as st 
import ui.menu2 as models

def menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar estudiante")
        print("2. Mostrar todos los estudiantes")
        print('3. Matricular estudiante')
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if (opcion == '1'):
            st.añadir_estudiante()
            input("\nPresione Enter para continuar...")
        
        elif (opcion == '2'):
            st.muestra_estudiantes()
            input("\nPresione Enter para continuar...")
        
        elif (opcion == '3'):
            models.main_menu()

        elif (opcion == '4'):
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()