from colorama import Fore, Style


def print_color(text, color):
    print(color + text + Style.RESET_ALL)


print_color("Problema: Crescimento Exponencial de População", Fore.BLUE)

# Dados população Inicial
initialPop = int(input("Insira a atual quantidade populacional da cidade: "))

# Taxa de Crescimento identificada  
rate = 0.03

# Quantidade de anos que deseja fazer o levantamento
Yresearch = int(input("Insira a quantidade de anos para o Levantamento: "))

# Calculando a população após os anos especificados
rateResult = initialPop * (1 + rate) ** Yresearch

# Diminuindo os valores
pct = rateResult - initialPop

# Retorno do Cálculo
print_color("Aumento populacional em " + str(Yresearch) +
            " anos pode ser de aproximadamente " + str(round(pct)) + " pessoas.", Fore.GREEN)
