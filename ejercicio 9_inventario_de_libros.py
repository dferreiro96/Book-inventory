
def libro_existe(nombre, autor, año, biblioteca):
    for libro in biblioteca:
        if (libro["Nombre"]== nombre and
            libro["Autor"]== autor and
            libro["Año"]==año):
            return True
    return False 
    
def pedir_numero(mensaje):
    while True:
        try:
            num= int(input(mensaje))
            return num
        except ValueError:
            print("\nNo válido")
            
def guardar_datos(mensaje):
        respuesta= input(mensaje)
        while not respuesta.replace(" ", "").isalpha():
            print("Solo se permiten letras y espacios")
            respuesta= input(mensaje)
        return respuesta

def menu():
    print("\n______MENÚ_______")
    print("1. Añadir libro")
    print ("2. Buscar")
    print("3. Listar")
    print("4. Salir")            

def encontrar(opcion, opciones):
    while True:
        if opcion in opciones:
            return opcion
        else:
            print("Valor fuera de rango.")
            opcion= pedir_numero("\nQué desea hacer? Introduzca un número del 1 al 4: ")

def buscar_elemento(guardar_datos, mensaje, buscado, biblioteca):
    lo_que_se_busca = guardar_datos(mensaje)
    for libro in biblioteca:
        if libro[buscado] == lo_que_se_busca:
            return(f"\nHa seleccionado el libro {libro[buscado]}, escrito por {libro["Autor"]} en el año {libro["Año"]}\n")
    return(f"\nEl libro {lo_que_se_busca} no está en la base de datos.\n")

def jugar(biblioteca):
    print("""\nEjercicio 9. Base de datos de libros. \nCada libro tiene título, autor, año. Permite: \nañadir libro, buscar por autor, listar todos, salir.\n""")
    while True:
      
            menu() 
            opciones = [1, 2, 3, 4]
            opción= pedir_numero("\nQué desea hacer? Introduzca un número del 1 al 4: ")
            seleccion= encontrar(opción, opciones)
            
            
            if seleccion == 1:
                nombre_del_libro= guardar_datos("\nIntroduzca el nombre del libro: ") .capitalize() .strip()
                autor= guardar_datos ("Introduzca el autor del libro: ") .title()
        
                año= pedir_numero("Introduzca el año del libro: ")
                while año <0:
                    print("Introduzca un año válido")
                    año= pedir_numero("Introduzca el año del libro: ")
                        
                if libro_existe(nombre_del_libro, autor, año, biblioteca):
                    print("El libro ya existe")
                else:
                    biblioteca.append({"Nombre": nombre_del_libro, "Autor": autor, "Año": año})
                    print(f"\nSe ha añadido el libro {nombre_del_libro}, escrito por {autor} en el año {año} satisfactoriamente.\n")
                
            elif seleccion == 2:
                
                    print("\nDesea buscar por 'Título', 'Autor' o 'Año'?\n")
                    print("1. Título")
                    print("2. Autor")
                    print ("3. Año")

                    buscar= pedir_numero("\n")

                    while buscar <1 or buscar > 3:
                            print ("Escoja una opción entre 1 y 3")
                            buscar= pedir_numero("\n")
                        
                    if buscar ==1:
                        buscar_elemento("\nIntroduzca el nombre del libro a buscar: ".capitalize(), "Nombre", biblioteca)
                        
                    elif buscar == 2:
                        buscar_elemento("\nIntroduzca el autor del libro a buscar: ".title(), "Autor", biblioteca)
                                
                    elif buscar == 3:
                        buscar_elemento("\nIntroduzca el año a buscar: ", "Año", biblioteca)
                        
                                
            elif seleccion == 3:
                if biblioteca ==[]:
                    print ("\nNo ha guardado ningún libro.")
                else:
                    print ("\nLa relación de libros con sus autores y años de edición es la siguiente: \n")
                    ordenados= sorted(biblioteca, key= lambda x: x ["Nombre"])
                    for i, libro in enumerate (ordenados, start=1):
                        print (f"{i}. Nombre del libro: {libro["Nombre"]}, Autor: {libro["Autor"]}, Año: {libro["Año"]}")
                
            elif seleccion == 4:
                print("\nHa salido del programa satisfactoriamente\n")
                return
            
        
def main():
    biblioteca = []
    jugar(biblioteca)
 
if __name__=="__main__":
    main()