def pertence_fibonacci(numero):
    # Exclui negativos
    if numero < 0:
        return False

    # Denomina od dois primeiros numeros da sequência
    a, b = 0, 1
    
    # Checa para 0 e 1
    if numero == a or numero == b:
        return True
    
    # Checa se o número digitado pertence à sequência
    while b < numero:
        a, b = b, a + b
        if b == numero:
            return True
    
    return False

# Entrada do usuário
try:
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número válido.")
