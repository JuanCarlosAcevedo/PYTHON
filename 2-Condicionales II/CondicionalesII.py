nombre=input("Ingrese su nombre y apellido: ").strip().title()
edad=input("Ingrese su edad: ")
email=input("Ingrese su correo electronico: ")
if edad.isdigit():
    edad=int(edad)
    if edad < 15:
        print("Su nombre es: ", nombre)
        print("El correo electronico es: ", email)
        print("Niño")
    elif edad < 18:
        print("Su nombre es: ", nombre)
        print("El correo electronico es: ", email)
        print("Adolescente")
    else :
        print("Su nombre es: ", nombre)
        print("El correo electronico es: ", email)
        print("Adulto")
else:
    print("Error de formato en edad")
