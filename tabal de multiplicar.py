# for es un ciclo que se ejecuta un determinado numero de veces

try:
    numer_to = int(input("Ingresa un numero: "))

    # 0 -> 1
    # 1 -> 2
    # 2 -> 3
    # 3 -> 4
    # 4 -> 5

# Tablas de multiplicar del 1 al numero ingresado por el usuario, ademas el usuario no debe ingresar
# numeros mayores 10

    if numer_to < 11:
        for j in range (1, numer_to + 1, 1):
            print("------------------")
            for i in range(1, 11, 1):
                if i == 10:
                    print("|", j, " * ", i, "  = ", i * j)
                else:
                    print("|", j, " * ", i, "  =  ", i * j)
            print("------------------")
    else:
        print("EL numero no es valido")
except:
    print("EL valor ingresado no es valido")

# input = 11
# error, es un numero no permitido

# input = 2
# 1, 2

# input = 5
# 1, 2, 3, 4, 5
try:
    numer_to = int(input("Ingresa un número: "))

    # Verificar si el número es menor o igual a 10
    if numer_to < 11:
        for j in range(1, numer_to + 1, 1):
            print(f"Tabla del {j}")
            print("------------------")
            for i in range(1, 11, 1):  # Solo hasta la tabla del 10
                if i == 10:
                    print("|", j, " * ", i, "  = ", i * j)
                else:
                    print("|", j, " * ", i, "  =  ", i * j)
            print("------------------")
    else:
        print("El número no es válido, por favor ingresa un número menor o igual a 10")
except ValueError:
    print("El valor ingresado no es válido. Por favor ingresa un número entero.")