CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite o seu nome
nome_usurario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salario
# converte a entrada para u numero de ponto flutuante
salario_usuario = float(input("Digite o seu salário: "))

# 3) Solicita ao  usuário que digite o valor  do bônus recebido
#converte a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o seu bônus: "))

# 4) Calcule o valor do bônus final
valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"O usuário {nome_usurario} possui o bonus de {valor_bonus} ")