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
            edit_ruta()
            input("Presione Enter para continuar...")
            return main_menu_rutas()
        case 2:
            delete_ruta()
            input("Presione Enter para continuar...")
            return main_menu_rutas()
        case 3:
            list_rutas()
            input("Presione Enter para continuar...")
            return main_menu_rutas()
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

def list_rutas():
    """Muestra todas las rutas existentes. Devuelve True si hay rutas, False si no."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Listado de Rutas de Aprendizaje ---")
    
    if not models.rutas:
        print("No hay rutas creadas todavía.")
        return False

    print(f"{'ID':<10} | {'Nombre de la Ruta':<25}")
    print('-' * 40)
    for id, data in models.rutas.items():
        print(f"{id:<10} | {data['nombre_ruta']:<25}")
    print('-' * 40)
    return True

def edit_ruta():
   
    if (not list_rutas()):
        input("Presione Enter para continuar...")
        return main_menu_rutas()

    id = input("\nIngrese el ID de la ruta que desea editar: ")

    if (id in models.rutas):
        print(f"Nombre actual: {models.rutas[id]['nombre_ruta']}")
        nuevo_nombre = input("Ingrese el nuevo nombre de la ruta: ")
        

        models.rutas[id]['nombre_ruta'] = nuevo_nombre
        
        print("\n¡Nombre de la ruta actualizado exitosamente!")
    else:
        print("Error: El ID ingresado no existe.")
    input("Presione Enter para continuar...")

def delete_ruta():

    if not list_rutas(): 
        input("Presione Enter para continuar...")
        return main_menu_rutas()

    id = input("\nIngrese el ID de la ruta que desea eliminar: ")

    if id in models.rutas:
        nombre_ruta = models.rutas[id]['nombre_ruta']
        confirmacion = input(f"¿Está seguro de que quiere eliminar la ruta '{nombre_ruta}'? (s/n): ").lower()
        
        if confirmacion == 's':
            del models.rutas[id]
            print("Ruta eliminada exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Error: El ID ingresado no existe.")
    input("Presione Enter para continuar...")
