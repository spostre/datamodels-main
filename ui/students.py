import os
import datamodels.modelsdata as models

def añadir_estudiante():
    """Pide los datos de un nuevo estudiante y lo añade al campus."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Añadir Nuevo Estudiante ---")
    
    estudiante = models.estudiante_plantilla.copy()

    id_estudiante = input("Ingrese el ID del Estudiante: ")
    estudiante['nombre'] = input("Ingrese el Nombre del Estudiante: ")
    estudiante['edad'] = int(input("Ingrese la Edad del Estudiante: "))
    estudiante['email'] = input("Ingrese el Email del Estudiante: ")
    estudiante['telefono'] = input("Ingrese el Telefono del Estudiante: ")

    models.campus.update({id_estudiante: estudiante})
    print("\nEstudiante añadido correctamente.")

def muestra_estudiantes():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Lista de Estudiantes Registrados ---")
    
    if not models.campus:
        print("No hay estudiantes registrados.")
        return 

    for id_estudiante, datos_estudiante in models.campus.items():
        print("-" * 30)
        print(f"ID:       {id_estudiante}")
        print(f"Nombre:   {datos_estudiante['nombre']}")
        print(f"Edad:     {datos_estudiante['edad']}")
        print(f"Email:    {datos_estudiante['email']}")
        print(f"Teléfono: {datos_estudiante['telefono']}")
    
    print("-" * 30)