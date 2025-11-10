'''
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
'''
'''from datetime import datetime

# Solicita a data de nascimento do usuário
data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte a string para um objeto de data
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Obtém a data atual
data_atual = datetime.now()

# Calcula a diferença em dias
dias_vivo = (data_atual - data_nascimento).days

# Exibe o resultado
print(f"Você está vivo há {dias_vivo} dias.")'''

from datetime import datetime

dia = int(input("Digite seu dia de nascimento: "))
mes = int(input("Digite seu mês de nascimento: "))
ano = int(input("Digite seu ano de nascimento: "))

nascimento = datetime(ano, mes, dia)
hoje = datetime.now()
vivo = (hoje - nascimento).days

print("Você já viveu", vivo, "dias.")
