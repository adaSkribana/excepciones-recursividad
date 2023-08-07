#la recursividad es una funcion llamada si misma dentro del cuerpo de la funcion

def countdown(num):
    if num == 0:
        print("kabo0m")
    else:
        print(num)
        countdown(num-1)

def countdown2(num):
    for num in range(num):
        if num == 0:
            print("KaboOm")
        else:
            print(num)
    