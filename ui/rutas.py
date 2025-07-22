import datamodels.modelsdata as models
import ui.menu2 as mainmenu
import os

def main_menu_rutas():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenido al Menú de Rutas")
    for i, opcion in enumerate(models.opcionesSkills, start=1):
        print(f"{i}. {opcion}")

    try:
        op = int(input("Seleccione una opción: ")) - 1

    except ValueError:

        print("Entrada no válida. Por favor, ingrese un número.")
        input("Presione Enter para continuar...")
        return main_menu_rutas()
    
    if (op < 0 or op >= len(models.opcionesSkills)):
        
        print("Opción no válida. Intente de nuevo.")
        return main_menu_rutas()
    
    match op:
        case 0:  # Crear ruta
            add_ruta()
            input("Presione Enter para continuar...")
            return main_menu_rutas()
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            mainmenu.main_menu()
        case _:
            print("Opción no implementada aún.")
            input("Presione Enter para continuar...")
            return main_menu_rutas()
        
def add_ruta():
        
    id = str(len(models.rutas) + 1).zfill(4)  # Generate a new ID based on the current number of routes
    print(f'Id: {id}')
    nombre_ruta = input("Ingrese el nombre de la ruta: ")
    ruta = {
        id:{
            "nombre_ruta": nombre_ruta,
            "skills": {}
        }
    }
    models.rutas.update(ruta)
    print(f"Ruta '{models.rutas}")