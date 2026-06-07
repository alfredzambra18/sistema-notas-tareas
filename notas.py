import json
import os
from datetime import datetime
import platform

# Nombre del archivo donde guardamos las notas
ARCHIVO_NOTAS = "notas.json"

# Colores para la terminal
class Colores:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

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
    limpiar_pantalla()
    print(f"{Colores.CYAN}{'=' * 60}{Colores.RESET}")
    print(f"{Colores.BOLD}{Colores.YELLOW}✏️  CREAR NUEVA NOTA{Colores.RESET}")
    print(f"{Colores.CYAN}{'=' * 60}{Colores.RESET}\n")
    
    titulo = input(f"{Colores.BLUE}📌 Título de la nota: {Colores.RESET}")
    
    if not titulo.strip():
        print(f"\n{Colores.RED}❌ Error: El título no puede estar vacío.{Colores.RESET}")
        input(f"\n{Colores.YELLOW}Presiona Enter para volver al menú...{Colores.RESET}")
        return
    
    contenido = input(f"{Colores.BLUE}📝 Contenido de la nota: {Colores.RESET}")
    
    if not contenido.strip():
        print(f"\n{Colores.RED}❌ Error: El contenido no puede estar vacío.{Colores.RESET}")
        input(f"\n{Colores.YELLOW}Presiona Enter para volver al menú...{Colores.RESET}")
        return
    
    # Creamos un diccionario con los datos de la nota
    nueva_nota = {
        "id": len(notas) + 1,
        "titulo": titulo,
        "contenido": contenido,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    
    notas.append(nueva_nota)
    guardar_notas(notas)
    
    print(f"\n{Colores.GREEN}{Colores.BOLD}✅ ¡Nota creada exitosamente!{Colores.RESET}")
    print(f"{Colores.CYAN}ID de la nota: {Colores.BOLD}{nueva_nota['id']}{Colores.RESET}")
    input(f"\n{Colores.YELLOW}Presiona Enter para volver al menú...{Colores.RESET}")

def ver_todas_notas(notas):
    """
    Muestra todas las notas guardadas.
    """
    limpiar_pantalla()
    print(f"{Colores.CYAN}{'=' * 60}{Colores.RESET}")
    print(f"{Colores.BOLD}{Colores.YELLOW}📚 VER TODAS LAS NOTAS{Colores.RESET}")
    print(f"{Colores.CYAN}{'=' * 60}{Colores.RESET}\n")
    
    if len(notas) == 0:
        print(f"{Colores.RED}❌ No tienes notas guardadas aún.{Colores.RESET}\n")
        input(f"{Colores.YELLOW}Presiona Enter para volver al menú...{Colores.RESET}")
        return
    
    print(f"{Colores.GREEN}Total de notas: {len(notas)}{Colores.RESET}\n")
    
    for i, nota in enumerate(notas, 1):
        print(f"{Colores.BOLD}{Colores.CYAN}{'─' * 60}{Colores.RESET}")
        print(f"{Colores.BOLD}{Colores.BLUE}📌 Nota #{nota['id']}{Colores.RESET}")
        print(f"{Colores.BOLD}Título:{Colores.RESET} {Colores.YELLOW}{nota['titulo']}{Colores.RESET}")
        print(f"{Colores.BOLD}Contenido:{Colores.RESET} {nota['contenido']}")
        print(f"{Colores.BOLD}Fecha:{Colores.RESET} {Colores.GREEN}{nota['fecha']}{Colores.RESET}")
    
    print(f"\n{Colores.CYAN}{'─' * 60}{Colores.RESET}\n")
    input(f"{Colores.YELLOW}Presiona Enter para volver al menú...{Colores.RESET}")

def buscar_nota(notas):
    """
    Busca una nota por título.
    """
    limpiar_pantalla()
    print(f"{Colores.CYAN}{'=' * 60}{Colores.RESET}")
    print(f"{Colores.BOLD}{Colores.YELLOW}🔍 BUSCAR NOTA{Colores.RESET}")
    print(f"{Colores.CYAN}{'=' * 60}{Colores.RESET}\n")
    
    busqueda = input(f"{Colores.BLUE}Escribe el título a buscar: {Colores.RESET}").lower()
    
    encontradas = []
    for nota in notas:
        if busqueda in nota['titulo'].lower():
            encontradas.append(nota)
    
    print()
    
    if len(encontradas) == 0:
        print(f"{Colores.RED}❌ No se encontraron notas con ese título.{Colores.RESET}\n")
    else:
        print(f"{Colores.GREEN}✅ Se encontraron {len(encontradas)} nota(s):{Colores.RESET}\n")
        
        for nota in encontradas:
            print(f"{Colores.BOLD}{Colores.CYAN}{'���' * 60}{Colores.RESET}")
            print(f"{Colores.BOLD}{Colores.BLUE}📌 Nota #{nota['id']}{Colores.RESET}")
            print(f"{Colores.BOLD}Título:{Colores.RESET} {Colores.YELLOW}{nota['titulo']}{Colores.RESET}")
            print(f"{Colores.BOLD}Contenido:{Colores.RESET} {nota['contenido']}")
            print(f"{Colores.BOLD}Fecha:{Colores.RESET} {Colores.GREEN}{nota['fecha']}{Colores.RESET}")
        
        print(f"\n{Colores.CYAN}{'─' * 60}{Colores.RESET}\n")
    
    input(f"{Colores.YELLOW}Presiona Enter para volver al menú...{Colores.RESET}")

def eliminar_nota(notas):
    """
    Elimina una nota por su ID.
    """
    limpiar_pantalla()
    print(f"{Colores.CYAN}{'=' * 60}{Colores.RESET}")
    print(f"{Colores.BOLD}{Colores.YELLOW}🗑️  ELIMINAR NOTA{Colores.RESET}")
    print(f"{Colores.CYAN}{'=' * 60}{Colores.RESET}\n")
    
    if len(notas) == 0:
        print(f"{Colores.RED}❌ No tienes notas para eliminar.{Colores.RESET}\n")
        input(f"{Colores.YELLOW}Presiona Enter para volver al menú...{Colores.RESET}")
        return
    
    print(f"{Colores.GREEN}Tus notas disponibles:{Colores.RESET}\n")
    
    for nota in notas:
        print(f"{Colores.BLUE}ID: {nota['id']}{Colores.RESET} - {Colores.YELLOW}{nota['titulo']}{Colores.RESET}")
    
    print()
    
    try:
        id_eliminar = int(input(f"{Colores.BLUE}Escribe el ID de la nota a eliminar: {Colores.RESET}"))
        
        nota_encontrada = False
        for i, nota in enumerate(notas):
            if nota['id'] == id_eliminar:
                titulo_eliminado = nota['titulo']
                notas.pop(i)
                guardar_notas(notas)
                print(f"\n{Colores.GREEN}{Colores.BOLD}✅ ¡Nota eliminada exitosamente!{Colores.RESET}")
                print(f"{Colores.YELLOW}'{titulo_eliminado}'{Colores.RESET} ha sido eliminada.\n")
                nota_encontrada = True
                break
        
        if not nota_encontrada:
            print(f"\n{Colores.RED}❌ No se encontró una nota con ese ID.{Colores.RESET}\n")
    
    except ValueError:
        print(f"\n{Colores.RED}❌ Por favor, ingresa un número válido.{Colores.RESET}\n")
    
    input(f"{Colores.YELLOW}Presiona Enter para volver al menú...{Colores.RESET}")

def menu_principal():
    """
    Muestra el menú principal y controla el flujo del programa.
    """
    limpiar_pantalla()
    print(f"{Colores.BOLD}{Colores.CYAN}{'╔' + '═' * 58 + '╗'}{Colores.RESET}")
    print(f"{Colores.BOLD}{Colores.CYAN}║{Colores.RESET}" + f"{Colores.BOLD}{Colores.YELLOW}{'📝 SISTEMA DE NOTAS Y TAREAS'.center(58)}{Colores.RESET}" + f"{Colores.BOLD}{Colores.CYAN}║{Colores.RESET}")
    print(f"{Colores.BOLD}{Colores.CYAN}{'╚' + '═' * 58 + '╝'}{Colores.RESET}\n")
    
    print(f"{Colores.BOLD}{Colores.GREEN}¿Qué quieres hacer?{Colores.RESET}\n")
    
    print(f"{Colores.BLUE}  {Colores.BOLD}1{Colores.RESET}{Colores.BLUE}  ✏️  Crear nueva nota{Colores.RESET}")
    print(f"{Colores.BLUE}  {Colores.BOLD}2{Colores.RESET}{Colores.BLUE}  📚 Ver todas las notas{Colores.RESET}")
    print(f"{Colores.BLUE}  {Colores.BOLD}3{Colores.RESET}{Colores.BLUE}  🔍 Buscar nota{Colores.RESET}")
    print(f"{Colores.BLUE}  {Colores.BOLD}4{Colores.RESET}{Colores.BLUE}  🗑️  Eliminar nota{Colores.RESET}")
    print(f"{Colores.RED}  {Colores.BOLD}5{Colores.RESET}{Colores.RED}  👋 Salir{Colores.RESET}")
    
    print(f"\n{Colores.CYAN}{'─' * 60}{Colores.RESET}")
    opcion = input(f"{Colores.BOLD}{Colores.YELLOW}Elige una opción (1-5): {Colores.RESET}")
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
            limpiar_pantalla()
            print(f"{Colores.BOLD}{Colores.CYAN}{'╔' + '═' * 58 + '╗'}{Colores.RESET}")
            print(f"{Colores.BOLD}{Colores.CYAN}║{Colores.RESET}" + f"{Colores.BOLD}{Colores.YELLOW}{'👋 ¡HASTA LUEGO!'.center(58)}{Colores.RESET}" + f"{Colores.BOLD}{Colores.CYAN}║{Colores.RESET}")
            print(f"{Colores.BOLD}{Colores.CYAN}{'╚' + '═' * 58 + '╝'}{Colores.RESET}\n")
            print(f"{Colores.GREEN}Gracias por usar el Sistema de Notas y Tareas 📝{Colores.RESET}\n")
            break
        else:
            limpiar_pantalla()
            print(f"{Colores.RED}{Colores.BOLD}❌ Opción no válida.{Colores.RESET}")
            print(f"{Colores.YELLOW}Por favor, elige entre 1 y 5.{Colores.RESET}\n")
            input(f"{Colores.YELLOW}Presiona Enter para intentar de nuevo...{Colores.RESET}")

# Esto ejecuta el programa cuando lo corres
if __name__ == "__main__":
    main()
