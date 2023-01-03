#Saída

print("Hello World!") 

#Variáveis ///

nome = input("escreva seu nome: ")
idade = input("escreva sua idade: ")
altura = input("escreva sua altura: ")
tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)

print("________________")
print(nome)
print(idade)
print(altura)
print("________________")
print(tipo_nome)
print(tipo_idade)
print(tipo_altura)
print("________________")
print(nome, "tem: ", idade, "anos, ", "e", altura, "de altura!")
print("________________")

'''
 EXERCÍCIO: Faça um formulário que pergunte o nome,CPF, endereço, idade, altura e telefone. 
 E imprima isso em um relatório organizado 
'''
nome = input("escreva seu nome: ")
idade = input("escreva sua idade: ")
altura = input("escreva sua altura: ")
endereço = input("escreva seu endereço: ")
cpf = input("escreva sua CPF: ")
telefone = input("escreva sua telefone: ")

print('o seu nome é: ', nome,
'\n'
'sua idade é: ', idade,
'\n'
'sua altura é: ', altura,
'\n'
'seu endereço é: ', endereço,
'\n'
'o seu CPF é: ', cpf,
'\n'
'seu telefone é: ', idade,
)
