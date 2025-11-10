'''
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
'''
'''senha = input("Diggite uma senha alfanumerica: ")
tamanho_senha = len(senha) >= 8
numero_senha = any(s.isdigit() for s in senha)
if tamanho_senha and numero_senha:
    print("Senha válida")
else:
    print("Senha inválidda") '''

'''# Função para verificar se a senha é segura
def senha_segura(senha):
    # Verifica se tem pelo menos 8 caracteres
    comprimento_ok = len(senha) >= 8

    # Verifica se tem pelo menos um número
    contem_numero = any(caractere.isdigit() for caractere in senha)

    # Retorna True se atender aos dois critérios
    return comprimento_ok and contem_numero

# Programa principal
print("=== Verificador de Senha Segura ===")
senha_digitada = input("Digite sua senha: ")

if senha_segura(senha_digitada):
    print("✅ Sua senha é considerada segura.")
else:
    print("❌ Sua senha não atende aos critérios mínimos de segurança.")'''


def validar_senha(senha):
    return len(senha) >= 8 and any(s.isdigit() for s in senha)
senha = input("Digite uma senha: ")
while not validar_senha(senha):
    print("Senha inválida, Tente outra.")
    senha = input("Digite uma senha: ")
print("Senha correta.")
