nomes = ['italo', 'andre', 'jao']

for i in range(len(nomes)):
    print (nomes[i])
    nomes.append('oi')
print(nomes)

print('______________________________________________________________-')

#Exercício:

listaDeConvidados = ['eu']

for i in listaDeConvidados and len(listaDeConvidados) < 20:
    pessoaConvidada = input('qual o seu nome? ')
    listaDeConvidados.append(pessoaConvidada)
    print('já tem', len(listaDeConvidados), 'pessoas na festa')
    print('Bem vindo(a) á minha festa!!')
    print(listaDeConvidados)