import json
import os
from datetime import datetime

# Nombre del archivo donde guardamos las notas
ARCHIVO_NOTAS = "notas.json"

def cargar_notas():
    """
    Carga las notas del archivo JSON.
    Si el archivo no existe, devuelve una lista vacía.
    """
    if os.path.exists(ARCHIVO_NOTAS):
        with open(ARCHIVO_NOTAS, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    return []

def guardar_notas(notas):
    """
    Guarda las notas en el archivo JSON.
    """
    with open(ARCHIVO_NOTAS, 'w', encoding='utf-8') as archivo:
        json.dump(notas, archivo, ensure_ascii=False, indent=2)

def crear_nota(notas):
    """
    Crea una nueva nota y la añade a la lista.
    """
    print("\n--- CREAR NUEVA NOTA ---")
    titulo = input("Escribe el título de la nota: ")
    contenido = input("Escribe el contenido de la nota: ")
    
    # Creamos un diccionario con los datos de la nota
    nueva_nota = {
        "id": len(notas) + 1,
        "titulo": titulo,
        "contenido": contenido,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    
    notas.append(nueva_nota)
    guardar_notas(notas)
    print("✅ ¡Nota creada exitosamente!")

def ver_todas_notas(notas):
    """
    Muestra todas las notas guardadas.
    """
    print("\n--- VER TODAS LAS NOTAS ---")
    
    if len(notas) == 0:
        print("❌ No tienes notas guardadas aún.")
        return
    
    for nota in notas:
        print(f"\n📌 ID: {nota['id']}")
        print(f"   Título: {nota['titulo']}")
        print(f"   Contenido: {nota['contenido']}")
        print(f"   Fecha: {nota['fecha']}")
        print("   " + "-" * 40)

def buscar_nota(notas):
    """
    Busca una nota por título.
    """
    print("\n--- BUSCAR NOTA ---")
    busqueda = input("Escribe el título a buscar: ").lower()
    
    encontradas = []
    for nota in notas:
        if busqueda in nota['titulo'].lower():
            encontradas.append(nota)
    
    if len(encontradas) == 0:
        print("❌ No se encontraron notas con ese título.")
    else:
        print(f"✅ Se encontraron {len(encontradas)} nota(s):\n")
        for nota in encontradas:
            print(f"📌 ID: {nota['id']}")
            print(f"   Título: {nota['titulo']}")
            print(f"   Contenido: {nota['contenido']}")
            print(f"   Fecha: {nota['fecha']}")
            print("   " + "-" * 40)

def eliminar_nota(notas):
    """
    Elimina una nota por su ID.
    """
    print("\n--- ELIMINAR NOTA ---")
    
    if len(notas) == 0:
        print("❌ No tienes notas para eliminar.")
        return
    
    ver_todas_notas(notas)
    
    try:
        id_eliminar = int(input("\nEscribe el ID de la nota a eliminar: "))
        
        nota_encontrada = False
        for i, nota in enumerate(notas):
            if nota['id'] == id_eliminar:
                notas.pop(i)
                guardar_notas(notas)
                print("✅ ¡Nota eliminada exitosamente!")
                nota_encontrada = True
                break
        
        if not nota_encontrada:
            print("❌ No se encontró una nota con ese ID.")
    
    except ValueError:
        print("❌ Por favor, ingresa un número válido.")

def menu_principal():
    """
    Muestra el menú principal y controla el flujo del programa.
    """
    print("\n" + "=" * 50)
    print("     📝 SISTEMA DE NOTAS Y TAREAS")
    print("=" * 50)
    print("1. Crear nueva nota")
    print("2. Ver todas las notas")
    print("3. Buscar nota")
    print("4. Eliminar nota")
    print("5. Salir")
    print("=" * 50)
    
    opcion = input("Elige una opción (1-5): ")
    return opcion

def main():
    """
    Función principal que controla el programa.
    """
    while True:
        notas = cargar_notas()
        opcion = menu_principal()
        
        if opcion == "1":
            crear_nota(notas)
        elif opcion == "2":
            ver_todas_notas(notas)
        elif opcion == "3":
            buscar_nota(notas)
        elif opcion == "4":
            eliminar_nota(notas)
        elif opcion == "5":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Por favor, elige entre 1 y 5.")

# Esto ejecuta el programa cuando lo corres
if __name__ == "__main__":
    main()