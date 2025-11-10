'''
4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

'''
# Inicializa os contadores
quantidade_pares = 0
quantidade_impares = 0

print("=== Analisador de Números ===")
print("Digite os números um por um. Para encerrar, digite 'sair'.")

while True:
    entrada = input("Digite um número (ou 'sair' para terminar): ")

    if entrada.lower() == 'sair':
        break

    if entrada.isdigit():
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"{numero} é par.")
            quantidade_pares += 1
        else:
            print(f"{numero} é ímpar.")
            quantidade_impares += 1
    else:
        print("Entrada inválida. Digite apenas números ou 'sair'.")

# Exibe o resumo
print("\n=== Resultado Final ===")
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
