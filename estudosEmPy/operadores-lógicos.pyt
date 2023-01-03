var_verdade = True
var_false = False

if var_verdade == True:
    print('var_true, é verdadeiro')

print('___________________________________')

print('se a opção escolhida for:\n 1 = escreve guilherme\n 2 = escreve pedro\n 3 = escreve andré')

opcao = input('escolha um opção: ')

if opcao == '1':
    print('você escolheu o guilherme')
    
elif opcao == '2':
    print('você escolheu o pedro')
    
elif opcao == '3':
    print('você escolheu o andre')
else:
    print('opção inválida')

print('___________________________________')

idade = 50

if not idade == 50:
    print('você não tem 50 anos')
else: 
    print("você tem 50 anos")

print('___________________________________')

idade = input('qual a sua idade: ')
peso = input('qual o seu peso: ')
altura = input('qual a sua altura: ')

if idade >'18':
    print('você não pode entrar no exército!1')
elif peso < '60':
    print('você não pode entrar no exército!2')
elif altura > '1,70':
    print('você não pode entrar no exército!3')
else: 
    print('Parabábens Soldado!')


 