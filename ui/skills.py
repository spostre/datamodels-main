import datamodels.modelsdata as models
import ui.menu2 as menu
import os


def main_menu_skills():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Bienvenido al Menú de Rutas")
    for i, opcion in enumerate(models.opcionesSkills, start=1):
        print(f"{i}. {opcion}")

    try:
        op = int(input("Seleccione una opción: ")) - 1

    except ValueError:

        print("Entrada no válida. Por favor, ingrese un número.")
        input("Presione Enter para continuar...")
        return main_menu_skills()
    
    if (op < 0 or op >= len(models.opcionesSkills)):
        
        print("Opción no válida. Intente de nuevo.")
        return main_menu_skills()
    
    match op:
        case 0:  # Crear ruta
            add_skill()
            input("Presione Enter para continuar...")
            return main_menu_skills()
        case 1:
            edit_skill()
            input("Presione Enter para continuar...")
            return main_menu_skills()
        case 2:
            list_skills()
            input("Presione Enter para continuar...")
            return main_menu_skills()
        case 3:
            delete_skill()
            input("Presione Enter para continuar...")
            return main_menu_skills()
        case 4:
            menu.main_menu()
        case _:
            print("Opción no implementada aún.")
            input("Presione Enter para continuar...")
            return main_menu_skills()
    
def add_skill():
    skill = {
        "nombre":"",
        "proyectos": {
            "nota": 0.0
        },
        "examenes": {
            "nota": 0.0
        },
        "actividades": {
            "notas": {
                "quices": [],
                "retos": [],
                "tarea": []
            }
        }       
    }
    id = str(len(models.skills) + 1).zfill(4)  # Generate a new ID based on the current number of routes
    print(f'Id: {id}')
    
    skill['nombre'] = input("Ingrese el nombre de la skill: ")
    models.skills.update({id: skill})
    print(f'Skill {models.skills}')
    
    input("Presione Enter para continuar...")

def edit_skill():

    if (not models.skills):
        print("No hay skills creadas todavía.")
        return

    print('--Selecione que quiere editar de skill--')
    print('1. nombre')
    print('2. nota de proyecto')
    print('3. nota de examen')
    print('4. nota de actividades')

    try:

        opcion = input(' : ')

        if (opcion == 1):
            
            n = str(input('nombre: '))
            models.skills['nombre'] += n
            print('Cambio de nombre completado')
            input('Presione Enter para continuar...')
            return main_menu_skills()
        
        elif (opcion == 2):

            p = float(input('nota: '))
            models.skills['proyectos']['nota'] += p
            print('Cambio de nota de proyecto completado')
            print(models.skills['proyectos']['nota'])
            input('Presione Enter para continuar')
            return main_menu_skills()
        
        elif (opcion == 3):
            e = float(input('nota: '))
            models.skills['examenes']['nota'] += e
            print('Cambio de nota de examen completado')
            print(models.skills['examenes']['nota'])
            input('Presione Enter para continuar')
            return main_menu_skills()

        else:
            print('Opcion no existe')
            input('Presione Enter para continuar')
            return edit_skill()

    except ValueError:
        print('Ingrese un valor valido')
        input('Presione Enter para continuar...')
        return edit_skill()
    
def delete_skill():
 
    list_skills() 
    
    if not models.skills:
        input("Presione Enter para continuar...")
        return 

    id = input("\n Ingrese el ID de la skill que desea eliminar: ")
    

    if (id in models.skills):
       
        skill_eliminada = models.skills[id]['nombre']
        confirmacion = input(f"¿Está seguro de que desea eliminar la skill Y(yes)/N(no)'{skill_eliminada}'? (y/n): ").lower()
        if confirmacion == 'y':
            del models.skills[id]
            print("Skill eliminada exitosamente.")
        else:
            print("Operación cancelada.")
            return main_menu_skills()
    else:
        print("Error: El ID ingresado no existe.")



def list_skills():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Listado de Skills ---")
    
    if (not models.skills):
        print("No hay skills creadas todavía.")
        return

    
    for id, skill_data in models.skills.items():
        print(f"ID: {id} - Nombre: {skill_data['nombre']}")


