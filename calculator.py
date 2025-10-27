def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Error: División por cero no permitida.")
        return None
    return a / b

exit2 = False
historial = ""

while not exit2:
    exit = False
    try:
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa otro número: "))
    except ValueError:
        print("Entrada no válida, ingresa números enteros.")
        continue

    condicion = input("¿Quieres sumar(+), restar(-), dividir(/) o multiplicar(*)? ")

    historial += f"{num1} {condicion} {num2} = "

    resultado = None
    if condicion == "+":
        resultado = sumar(num1, num2)
    elif condicion == "-":
        resultado = restar(num1, num2)
    elif condicion == "/":
        resultado = division(num1, num2)
        if resultado is None:
            continue
    elif condicion == "*":
        resultado = multiplicacion(num1, num2)
    else:
        print("Operación no válida.")
        continue

    print("Resultado:", resultado)
    historial += str(resultado) + "\n"
    num1 = resultado  # Actualizar num1 para la siguiente operación

    while not exit:
        confirmar = input("¿Quieres ver el historial? (Y/N) ").strip().upper()
        if confirmar == "Y":
            print("\nHistorial de operaciones:")
            print(historial)

        confirmar = input("¿Quieres reiniciar la calculadora? (Y/N) ").strip().upper()
        if confirmar == "Y":
            exit = True
            break

        confirmar = input("¿Quieres seguir calculando? (Y/N) ").strip().upper()
        if confirmar == "N":
            exit = True
            exit2 = True
        elif confirmar == "Y":
            try:
                num2 = int(input("Ingresa un número: "))
            except ValueError:
                print("Entrada no válida, ingresa un número entero.")
                continue

            condicion = input("¿Quieres sumar(+), restar(-), dividir(/) o multiplicar(*)? ")

            historial += f"{num1} {condicion} {num2} = "

            resultado = None
            if condicion == "+":
                resultado = sumar(num1, num2)
            elif condicion == "-":
                resultado = restar(num1, num2)
            elif condicion == "/":
                resultado = division(num1, num2)
                if resultado is None:
                    continue
            elif condicion == "*":
                resultado = multiplicacion(num1, num2)
            else:
                print("Operación no válida.")
                continue

            print("Resultado:", resultado)
            historial += str(resultado) + "\n"
            num1 = resultado
        else:
            print("Opción no válida, por favor responde Y o N.")

print("Programa terminado.")
