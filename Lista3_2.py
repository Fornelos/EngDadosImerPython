######################## LISTA 3 parte 2 ############################
#ENGENHARIA E ANALISE DE DADOS 2025.1
#THIAGO FORNELOS DE ALBUQUERQUE


######### QUESTAO 5 #########################################
nomes = []
idades =[]
alturas = []

for i in range(5):
    nome = input('Informe o nome {}: '.format(i+1))
    idade = int(input('Informe a Idade da pessoa {} :'.format(i+1)))
    altura = float(input('Informe a altura da pessoa {} :'.format(i+1)))
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)

maior_altura = max(alturas)
index = alturas.index(maior_altura)
print('{}, com {} anos e {:.3f} m, é a pessoa mais alta do grupo.'.format(nomes[index],idades[index],alturas[index]))
#############################################################

######### QUESTAO 6 #########################################

numeros = []
for i in range(10):
    numero = int(input('Informe o número {} : '.format(i+1)))
    numeros.append(numero)

lista_par = [x for x in numeros if x%2 ==0 ]
lista_par.sort(reverse=True)
print('Maior número par: {}'.format(lista_par[0]))

#############################################################

######### QUESTAO 7 #########################################
codigos = []
alturas = []
pesos =[]
try:
    quantidade_clientes = int(input('Informe a quantidade de clientes: '))

    for i in range(quantidade_clientes):
        codigo = input('Informe o codigo do cliente {}: '.format(i+1))
        altura = float(input('Informe a altura do cliente {} :'.format(i+1)))
        peso = int(input('Informe o peso do cliente {} :'.format(i+1)))
        codigos.append(codigo)
        alturas.append(altura)
        pesos.append(peso)

    maior_altura = max(alturas)
    menor_altura = min(alturas)
    maior_peso = max(pesos)
    menor_peso = min(pesos)
    index_altura_maior = alturas.index(maior_altura)
    index_altura_menor = alturas.index(menor_altura)
    index_peso_maior = pesos.index(maior_peso)
    index_peso_menor = pesos.index(menor_peso)
    media_altura = sum(alturas) / len(alturas)
    media_peso = sum(pesos) / len(pesos)

    print(f'O cliente mais alto tem: código {codigos[index_altura_maior]} altura {alturas[index_altura_maior]} m e peso {pesos[index_altura_maior]} kg')
    print(f'O cliente mais baixo tem: código {codigos[index_altura_menor]}, altura {alturas[index_altura_menor]} m e peso {pesos[index_altura_menor]} kg.')
    print(f'O cliente mais leve tem: código {codigos[index_peso_menor]}, altura {alturas[index_peso_menor]} m e peso {pesos[index_peso_menor]} kg.')
    print(f'O cliente mais pesado tem: código {codigos[index_peso_maior]}, altura {alturas[index_peso_maior]} m e ppeso {pesos[index_peso_maior]} kg.')
    print(f'A média das alturas é: {media_altura}.')
    print(f'A média dos pesos é: {media_peso}.')

except:
    print("error")
#############################################################
    
######### QUESTAO 8 #########################################
lista_clientes_bonus = {}
total_bonus=0
PERCBONUS = 15
def calcularBonus(valor):
    bonus = valor * (PERCBONUS/100)
    return bonus

try:
    quantidade_clientes = int(input('Informe a quantidade de clientes em loja? : '))
    for i in range(quantidade_clientes):
        nome = input('Informe o nome do cliente: ').lower()
        valor_compras_anual= float(input('Informe o valor das compras: '))
        if nome in lista_clientes_bonus:
            print('Cliente ja cadastrado!')
            continue
        elif valor_compras_anual >= 2000:
            print('Cliente apto para receber o bônus!')
            bonus = calcularBonus(valor_compras_anual)
            total_bonus +=bonus
            lista_clientes_bonus[nome] = bonus

    print(f'Clientes: {len(lista_clientes_bonus)}')
    print(f'Total: {total_bonus}')
except:
    print('Error')  
 #############################################################  
    
######### QUESTAO 9 ##########################################
vendas_ano = []
meses = ('Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
try:
    for i in meses:
        valor_mes = float(input(f'Informe o valor do mes de {i}: '))
        vendas_ano.append(valor_mes)

    maior_valor_mes = max(vendas_ano)
    menor_valor_mes = min(vendas_ano)
    mes_maior = vendas_ano.index(maior_valor_mes)
    mes_menor = vendas_ano.index(menor_valor_mes)
    total_ano = sum(vendas_ano)
    media_ano = total_ano / len(meses)

    print(f'Mês com a maior venda: {meses[mes_maior]} R${(maior_valor_mes)}')
    print(f'Mês com a menor venda: {meses[mes_menor]} R${(menor_valor_mes)}')
    print(f'Média de vendas ao longo do ano: R$ {media_ano}')
    print(f'Total de vendas no ano: R$ {total_ano}')
      
except:
    print('Error!')
###############################################################
    
######### QUESTAO 10 ##########################################

lista_numero_fibonacci = []
PARADA = 20
def Fibonacci(num1,num2,parada):
    proximo_valor = num1 + num2
    lista_numero_fibonacci.append(proximo_valor)
    parada +=1
    if parada == PARADA:
        return 
    return Fibonacci (num2 , proximo_valor,parada)


num1 = int(input(('Informe o primeiro número: ')))
num2 = int(input(('Informe o segundo número: ')))
lista_numero_fibonacci.append(num1)
lista_numero_fibonacci.append(num2)
Fibonacci(num1,num2,0)
print(lista_numero_fibonacci)

###############################################################



