def soma(num1, num2): 
    result = num1 + num2
    return result

def sub(num1, num2): 
    result = num1 - num2
    return result

def multi(num1, num2): 
    result = num1 * num2
    return result

def divi(num1, num2):
    if num2 == 0:
        print ("Não é possiel dividir por 0")
        return "Erro na divisão"
    result = num1 / num2
    return result