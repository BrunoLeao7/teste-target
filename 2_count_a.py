def contar_letras_a(s):
    # Converte a string para minúscula
    s = s.lower()
    
    # Conta o número de "a"
    contagem = s.count('a')
    
    return contagem

# Entrada do usuário
entrada = input("Digite uma string para verificar a ocorrência da letra 'a': ")
contagem = contar_letras_a(entrada)

if contagem > 0:
    print(f"A letra 'a' aparece {contagem} vez(es) na string.")
else:
    print("A letra 'a' não aparece na string.")
