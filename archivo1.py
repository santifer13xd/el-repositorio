def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))

    imc = calcular_imc(peso, altura)
    print("Tu índice de masa corporal es:", imc)

    if imc < 18.5:
        print("Estás bajo peso.")
    elif imc < 25:
        print("Tienes un peso normal.")
    elif imc < 30:
        print("Tienes sobrepeso.")
    else:
        print("Tienes obesidad.")

if __name__ == "__main__":
    main()
