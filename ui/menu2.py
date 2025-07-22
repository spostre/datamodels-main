import os
import datamodels.modelsdata as models
import ui.rutas as rt
import ui.skills as sk

def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenido al Menú Principal")
    for i, opcion in enumerate(models.opcionesMenu, start=1):
        print(f"{i}. {opcion}")
    try:
        op = int(input("Seleccione una opción: ")) - 1
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        input("Presione Enter para continuar...")
        return main_menu()
    if op < 0 or op >= len(models.opcionesMenu):
        print("Opción no válida. Intente de nuevo.")
        return main_menu()
    match op:
        case 0:  # Administrar rutas
            rt.main_menu_rutas()
            return main_menu()
        case 1:
            pass
        case 2:  
            sk.main_menu_skills()
            return main_menu()
        case 3:
            pass