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
        print ("Não é possiel dividir por 0")
        return "Erro na divisão"
    result = num1 / num2
    return result

def porcentagem(num1, perc):
    result = num1 * (perc / 100)
    return result
    
# 90 x 20 
# resultado / 100 
