import csv
import json


class Libro:
    def __init__(self, nombre, año, autor):
        self.nombre = nombre
        self.año = año
        self.autor = autor
        
    def __str__ (self):
        return f"{self.nombre} escrito por {self.autor} en el año {self.año}"
        

class Biblioteca:
    def __init__(self):
        self.lista_de_libros = []

    def libro_existe(self, nombre, autor, año):
        for libro in self.lista_de_libros:
            if libro.nombre == nombre and libro.autor == autor and libro.año == año:
                return True
        return False

    def buscar_elemento_por_nombre(self, nombre):
        encontrado = False
        for libro in self.lista_de_libros:
            if libro.nombre == nombre:
                print(
                    f"\nHa seleccionado el libro {libro}\n"
                )
                encontrado = True
        if not encontrado:
            print(f"\nEl libro {nombre} no está en la base de datos.\n")

    def buscar_elemento_por_autor(self, autor):
        encontrado = False
        for libro in self.lista_de_libros:
            if libro.autor == autor:
                print(
                    f"\nHa seleccionado el libro {libro}\n"
                )
                encontrado = True
        if not encontrado:
            print(
                f"\nNo se encuentra ningún libro escrito por {autor} en la base de datos.\n"
            )

    def buscar_elemento_por_año(self, año):
        encontrado = False
        for libro in self.lista_de_libros:
            if libro.año == año:
                print(
                    f"\nHa seleccionado el libro {libro}\n"
                )
                encontrado = True
        if not encontrado:
            print(
                f"\nNo se encuentra ningún libro escrito en el año {año} la base de datos.\n"
            )

    def añadir_libro(self, libro):
        self.lista_de_libros.append(libro)

    def mostrar_libros_ordenados(self):
        ordenados = sorted(self.lista_de_libros, key=lambda x: x.nombre)
        for i, libro in enumerate(ordenados, start=1):
            print(
                f"{i}. Nombre del libro: {libro}"
            )

    def convertir_datos_a_diccionario(self):
        lista_de_diccionarios = []
        for libro in self.lista_de_libros:
            diccionario_libro = libro.__dict__.copy()
            lista_de_diccionarios.append(diccionario_libro)
        return lista_de_diccionarios

    def guardar_datos(self):
        datos_para_json = self.convertir_datos_a_diccionario()
        with open("Registro_de_libros.json", "w", encoding="utf-8") as archivo:
            json.dump(datos_para_json, archivo, ensure_ascii=False, indent=4)

    def descargar_datos(self):
        try:
            with open("Registro_de_libros.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                lista_reconstruida = []
                for libro in datos:
                    objeto_libro = Libro(libro["nombre"], libro["año"], libro["autor"])
                    lista_reconstruida.append(objeto_libro)
                return lista_reconstruida

        except FileNotFoundError:
            print("\nNo se encontró la base de datos, se creará una nueva.")
            return []
        except json.JSONDecodeError:
            print("\nLa base de datos está corrupta, se creará una nueva.")
            return []

    def exportar(self):
        with open(
            "Registro en tabla de la biblioteca.csv", "w", encoding="utf-8", newline=""
        ) as archivo:
            columnas = ["Nombre del libro", "Autor", "Año"]
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            for libro in self.lista_de_libros:
                escritor.writerow(
                    {
                        "Nombre del libro": libro.nombre,
                        "Autor": libro.autor,
                        "Año": libro.año,
                    }
                )


def pedir_numero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            return num
        except ValueError:
            print("\nNo válido")


def pedir_texto(mensaje):
    respuesta = input(mensaje).capitalize().strip()
    return respuesta


def menu():
    print("\n______MENÚ_______")
    print("1. Añadir libro")
    print("2. Buscar")
    print("3. Listar")
    print("4. Exportar a .csv")
    print("5. Salir")


def menu_búsqueda():
    print("\nDesea buscar por 'Título', 'Autor' o 'Año'?\n")
    print("1. Título")
    print("2. Autor")
    print("3. Año")


def encontrar(opcion, opciones):
    while True:
        if opcion in opciones:
            return opcion
        else:
            print("Valor fuera de rango.")
            opcion = pedir_numero(
                "\nQué desea hacer? Introduzca un número del 1 al 5: "
            )


def jugar():
    mi_biblioteca = Biblioteca()
    lista_reconstituida = mi_biblioteca.descargar_datos()
    mi_biblioteca.lista_de_libros = lista_reconstituida
    
    print(
        """\nEjercicio: Base de datos de libros. \nCada libro tiene título, autor, año. Permite: \nañadir libro, buscar por autor, listar todos, salir.\n"""
    )
    if mi_biblioteca.lista_de_libros:
        print("\nDatos recuperados")
    while True:
        menu()
        opciones = [1, 2, 3, 4, 5]
        opción = pedir_numero("\nQué desea hacer? Introduzca un número del 1 al 5: ")
        seleccion = encontrar(opción, opciones)

        if seleccion == 1:
            nombre_del_libro = (
                pedir_texto("\nIntroduzca el nombre del libro: ").capitalize().strip()
            )
            autor = pedir_texto("Autor del libro: ").title()
            año = pedir_numero("Año del libro: ")
            while 0 > año or año > 2026:
                print("\nIntroduzca un año válido")
                año = pedir_numero("Introduzca el año del libro: ")

            if mi_biblioteca.libro_existe(nombre_del_libro, autor, año):
                print("El libro ya existe")
            else:
                mi_libro = Libro(nombre_del_libro, año, autor)
                mi_biblioteca.añadir_libro(mi_libro)
                mi_biblioteca.guardar_datos()
                print(
                    f"\nSe ha añadido y guardado el libro {mi_libro.nombre}, escrito por {mi_libro.autor} en el año {mi_libro.año}.\n"
                )

        elif seleccion == 2:
            menu_búsqueda()
            buscar = pedir_numero("\n")
            while buscar < 1 or buscar > 3:
                print("Escoja una opción entre 1 y 3")
                buscar = pedir_numero("\n")

            if buscar == 1:
                nombre = pedir_texto("\nNombre del libro a buscar: ")
                mi_biblioteca.buscar_elemento_por_nombre(nombre)

            elif buscar == 2:
                autor_buscado = pedir_texto("\nAutor: ")
                mi_biblioteca.buscar_elemento_por_autor(autor_buscado)

            elif buscar == 3:
                año_buscado = pedir_numero("\nAño del libro: ")
                mi_biblioteca.buscar_elemento_por_año(año_buscado)

        elif seleccion == 3:
            if not mi_biblioteca.lista_de_libros:
                print("\nNo ha guardado ningún libro.")
            else:
                print(
                    "\nLa relación de libros con sus autores y años de edición es la siguiente: \n"
                )
                mi_biblioteca.mostrar_libros_ordenados()

        elif seleccion == 4:
            mi_biblioteca.exportar()
            print("\nDatos exportado correctamente.\n")

        else:
            print("\nHa salido del programa satisfactoriamente\n")
            return


def main():
    jugar()


if __name__ == "__main__":
    main()
