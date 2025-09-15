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
