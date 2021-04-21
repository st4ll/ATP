print('Bom dia, boa tarde ou boa noite! Esta é minha loja Floreios e Borrões, seja muito bem vindo, meu nome é Jaime Filho!')
print('Preciso fazer uma análise de crédito sua. Para isso, preciso que me informe o seu cargo na empresa em que trabalha, o seu salário e o ano em que nasceu.')

cargo = input('Informe seu cargo: ')
salario = int(input('Informe o seu salário: '))
ano = int(input('Informe o ano de nascimento: '))
idade = 2021-ano
limite = (salario*(idade/1000))+100

print('O seu cargo é {}, o seu salário é {} e o ano em que nasceu é {}.' .format(cargo, salario, ano))
print('Você tem {} anos.' .format(idade))
print('Na nossa loja, o limite de crédito para pessoas com a sua idade e sua faixa salarial é de {}.' .format(limite))

nome = input('Informe o nome do produto: ')
preco = float(input('Informe o preço do produto: '))

if preco <= limite*0.6:
    print('Liberado!')
elif preco > limite*0.6 and preco <= limite*0.9:
    print('Liberado para parcelar em até 2x!')
elif preco > limite*0.9:
    print('Liberado para parcelar em até 3x!')
else:
    print('Bloqueado.')