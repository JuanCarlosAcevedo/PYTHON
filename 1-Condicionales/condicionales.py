# Se solicita al usuario que ingrese su nombre, apellido, edad y email.
# Si no hay espacios en blanco en nombre, apellido, email y la edad es mayor a 18, se imprime en pantalla los datos
# Si los datos estan en blancos o la edad es menor a 18, se imprime ERROR!

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
email = input("Ingrese su email: ")

if ((nombre != "" and apellido != "" and email != "") and (edad > 18)):
    print ("Su nombre y apellido son: ", nombre, apellido)
    print ("Su edad es: ", edad)
    print ("Su email es:", email)
else:
    print ("ERROR!")
