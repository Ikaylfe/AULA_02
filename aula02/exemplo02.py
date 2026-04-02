# nome = 'davi'
# idade = 10

# print (f'Olá {nome}!')
# print (f'Você tem {idade} anos.')

# #----------------------------------------------------
# # Atividade fixação

# nome = 'Juliana'
# bairro = 'Tijuca'
# profissao = 'Advogada'

# print(f'Nome: {nome}')
# print(f'Bairro: {bairro}')
# print(f'Profissão: {profissao}')

# #----------------------------------------------------
# # Operadores
# preco = 20
# quantidade = 3
# total = preco * quantidade

# print (f'Total é {total}')

# #----------------------------------------------------
# colaborador = 'Ana Silva'
# salario = 3000
# bonus = 880

# total = salario + bonus

# print (f'O novo salário de {colaborador} será {total} , a partir do mês de Abril.')

# #----------------------------------------------------

# Exemplo de Entrada de valores pelo usuário

# nome= input('Informe o nome:')
# print (f'Olá {nome}!')


#----------------------------------------------------
# Atividade fixação

#float - números c/ casas decimais *todos os números*
#int - somente números inteiros (sem ponto)
# string = texto (variável recebe valor de texto)
# Boleano = True or False

# colaborador=input('Informe seu nome:')
# salario=float(input('Informe seu salário atual:'))
# bonus=float(input('Informe o bônus desejado:'))
# total= salario + bonus   
# print(f'Seu novo salário {colaborador} será :{total}')


#----------------------------------------------------
#Atividade de cálculo de porcentagem

preco=float(input('Informe o preço:       '))
qtde=int(input('Informe a quantidade:     '))
total_a_bruto=preco * qtde
desconto=total_a_bruto * 0.1 # Refere-se a 10% de desconto sobre o valor total
#10 % pode ser *0.1 ou 10/100
total_a_pagar = total_a_bruto-desconto
print(f'O total a pagar será:{total_a_pagar}.')
print(f'Você recebeu o desconto de:{desconto}.')



 


