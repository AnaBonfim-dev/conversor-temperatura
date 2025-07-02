def converter_temperatura(valor, unidade):
    if unidade == "C":
        f = valor * 9/5 + 32
        k = valor + 273.15
        return f"{valor}°C = {f:.2f}°F | {k:.2f}K"
    elif unidade == "F":
        c = (valor - 32) * 5/9
        k = c + 273.15
        return f"{valor}°F = {c:.2f}°C | {k:.2f}K"
    elif unidade == "K":
        c = valor - 273.15
        f = c * 9/5 + 32
        return f"{valor}K = {c:.2f}°C | {f:.2f}°F"
    else:
        return "Unidade inválida. Use C, F ou K."

def main():
    print("CONVERSOR DE TEMPERATURA")
    try:
        temp = float(input("Digite a temperatura: "))
        unidade = input("Qual a unidade? (C/F/K): ").upper()
        resultado = converter_temperatura(temp, unidade)
        print("\nResultado:", resultado)
    except ValueError:
        print("Erro: Digite um número válido.")

if __name__ == "__main__":
    main()
