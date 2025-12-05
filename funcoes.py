def somar(num1, num2): 
    result = num1 + num2
    return result

def subtrair(num1, num2): 
    result = num1 - num2
    return result

def multiplicar(num1, num2): 
    result = num1 * num2
    return result

def dividir(num1, num2):
    if num2 == 0:
        return "Erro"
    result = num1 / num2
    return result

def porcentagem(num1, perc):
    if num1 == 0:
        return perc/100
    return num1 * (perc / 100)
# 90 x 20 
# resultado / 100 
