#errores fecuentes 
fruits =["banana", "apple", "watermelon", "pineapple"]
while True:
    user_option = input("ingrese un numero entre 0 y 3 para saber la fruta sorpresa, 'q' para salir: ")

    if user_option == "q":
        break
    try:
        print(fruits[int(user_option)])
     
    except ValueError as valueerror:
        print("El elemento ingresado no es un numero entero",valueerror)

    except IndexError as indexerror:
            print("El numero ingresado exede nuestro indice ", indexerror)
    