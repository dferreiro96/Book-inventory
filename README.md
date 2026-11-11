# Book Database / Base de Datos de Libros

A Python CLI program to manage a small library: add books, search by title/author/year, list all books, and export to CSV.

Un programa de línea de comandos en Python para gestionar una pequeña biblioteca: añadir libros, buscar por título/autor/año, listar todos los libros y exportar a CSV.

## Features / Funcionalidades

- **Object-Oriented Design:** Uses a `Libro` class and a `Biblioteca` class to encapsulate logic and data. / **Diseño Orientado a Objetos:** Usa una clase `Libro` y una clase `Biblioteca` para encapsular la lógica y los datos.
- Add books with title, author, and year / Añadir libros con título, autor y año
- Validate that books are not duplicated / Validar que los libros no estén duplicados
- Search by title, author, or year / Buscar por título, autor o año
- List all books sorted alphabetically by title / Listar todos los libros ordenados alfabéticamente por título
- **Automatic Persistence:** Saves the library data to a JSON file automatically. / **Persistencia Automática:** Guarda los datos de la biblioteca en un archivo JSON automáticamente.
- **CSV Export:** Export the book list to a CSV file for Excel. / **Exportación a CSV:** Exporta la lista de libros a un archivo CSV para Excel.
- Menu-driven interface / Interfaz con menú
- Input validation for numbers and text / Validación de entrada para números y texto
- Clean exit / Salida limpia

## Requirements / Requisitos

- Python 3.10 or higher.

## What I Learned / Lo que Aprendí

- **Object-Oriented Programming (Classes and Objects)** / **Programación Orientada a Objetos (Clases y Objetos)**
- **Encapsulation:** Keeping data and functions together in classes / **Encapsulamiento:** Mantener datos y funciones juntos en clases.
- **File handling:** Reading and writing JSON and CSV files / **Manejo de archivos:** Leer y escribir archivos JSON y CSV.
- **Using `__dict__`** to easily convert objects to dictionaries for JSON / **Usar `__dict__`** para convertir objetos a diccionarios para JSON fácilmente.
- Validating user input with try/except / Validar entradas del usuario con try/except
- Using sorted() with lambda to sort a list of objects / Usar sorted() con lambda para ordenar una lista de objetos
- Using if __name__ == "__main__" to run the main function / Usar if __name__ == "__main__" para ejecutar la función principal


## Author / Autor

[dferreiro96]

## How to Run / Cómo Ejecutar

```bash
python Inventario_de_libros.py