
print("""Ejercicio 9. Base de datos de libros. \nCada libro tiene título, autor, año. Permite: \nañadir libro, buscar por autor, listar todos, salir.\n""")

def libro_existe(nombre, autor, año):
    for libro in lista:
        if (libro["Nombre"]== nombre and
            libro["Autor"]== autor and
            libro["Año"]==año):
            return True
    return False 
    
lista=[]


jugar= True 
while jugar :

	print("\n______MENÚ_______")
	print("1. Añadir libro")
	print ("2. Buscar")
	print("3. Listar")
	print("4. Salir")


	
	while True :
			try:
				opción=int(input("\nQué desea hacer? Introduzca un número del 1 al 4: "))
		
			except ValueError :
				print("Solo se permiten números")
				continue
			if opción not in range (1,5):
				print("Valor fuera de rango")
				continue
			break

	while opción:
			if opción==1:
				nombre_del_libro= input("\nIntroduzca el nombre del libro: ") .capitalize () .strip()
				if not nombre_del_libro.replace(" ", "").isalpha():
					print("Solo se permiten letras y espacios")
					continue
				
				autor= input("Introduzca el autor del libro: ") .title()
				if not autor.replace(" ", "").isalpha():
					print("Solo se permiten letras y espacios")
					continue
				while True:
					try:
						año= int(input("Introduzca el año del libro: "))
					except ValueError:
						print("Debe introducir un año válido")
						continue
					if año <0:
						print("Introduzca un año válido")
						continue
					break
				if libro_existe(nombre_del_libro, autor, año):
					print("El libro ya existe")
				else:
					lista.append({"Nombre": nombre_del_libro, "Autor": autor, "Año": año})
					print(f"\nSe ha añadido el libro {nombre_del_libro}, escrito por {autor} en el año {año} satisfactoriamente.")
			
				break
			elif opción==2:
				
					print("\nDesea buscar por 'Título', 'Autor' o 'Año'?\n")
					print("1. Título")
					print("2. Autor")
					print ("3. Año")
					while True :
						try:
							buscar= int(input("\n"))
						except ValueError :
							print("Introduzca un valor válido")
							continue
						if buscar <1 or buscar > 3:
							print ("Escoja una opción entre 1 y 3")
							continue
						break
					if buscar ==1:
						nombre_a_buscar= input("\nIntroduzca el nombre del libro a buscar: ") .capitalize ()
						if not nombre_a_buscar.replace(" ", "").isalpha():
							print("Solo se permiten letras y espacios")
							continue
						encontrado= False
						for libro in lista:
							if libro["Nombre"]== nombre_a_buscar:
								print(f"\nHa seleccionado el libro {libro["Nombre"]}, escrito por {libro["Autor"]} en el año {libro["Año"]}")
								encontrado= True
								opción= None
								break
								
						if not encontrado:
								print(f"\nEl libro {nombre_a_buscar.capitalize()} no está en la base de datos.")
								opción= None
								break
					

					if buscar ==2:
						autor_a_buscar= input("\nIntroduzca el autor del libro a buscar: ") .title ()
						autor_encontrado= False
						for libro in lista:
							if libro["Autor"] == autor_a_buscar:
								print(f"El libro escrito por el autor {libro["Autor"]} es {libro["Nombre"]} y fue escrito en el año {libro["Año"]}.")	
								autor_encontrado= True
								opción= None
								break
						if not autor_encontrado:
								print (f"No hay ningún libro del autor {autor_a_buscar} en la base de datos.")
								opción= None
								break
					if buscar== 3:
						while True:
							try:
								año_a_buscar= int(input("\nIntroduzca el año a buscar: "))
							except ValueError:
								print ("Introduzca un valor numérico")
								continue
							break
						libro_encontrado= False
						for libro in lista:
							if libro["Año"] == año_a_buscar:
								print (f"El libro escrito en el año {año_a_buscar} es {libro["Nombre"]} y fue escrito por {libro["Autor"]}.")
								libro_encontrado= True
								opción= None
								break
						if not libro_encontrado:
								print (f" No existe un libro escrito en el año {año_a_buscar}.")
								opción= None
								break
			elif opción==3:
				print ("\nLa relación de libros con sus autores y años de edición es la siguiente: \n")
				ordenados= sorted(lista, key= lambda x: x ["Nombre"])
    
				for i, libro in enumerate (ordenados, start=1):
					print (f"{i}. Nombre del libro: {libro["Nombre"]}, Autor: {libro["Autor"]}, Año: {libro["Año"]}")
				break
			

			elif opción ==4:
				print("\nHa salido del programa satisfactoriamente\n")
				jugar= False
				break
				
	
									
