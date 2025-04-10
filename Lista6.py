######################## LISTA 6 ############################
#ENGENHARIA E ANALISE DE DADOS 2025.1
#THIAGO FORNELOS DE ALBUQUERQUE
######### QUESTAO 1 #########################################
import os
import time

lista_cor = []
try:
    quantidade_cor = int(input('Informe a quantidade de cores: '))
    for i in range(quantidade_cor):
        nome_cor = input('Informe o nome da cor: ').strip().capitalize()
        red = int(input('Informe a cor RED do RGB: ').strip())
        green = int(input('Informe a cor GREEN do RGB: ').strip())
        blue  = int(input('Informe a cor BLUE do RGB: ').strip())
        lista_cor.append((nome_cor,(red,green,blue)))
    busca_cor = input('Informe o nome a ser pesquisada: ').strip().capitalize()
    #print(lista_cor)
    for cor , rgb in lista_cor:
      if cor == busca_cor:
       print('Valores RGB para a cor {}: Red={}, Green={}, Blue={}'.format(cor,rgb[0],rgb[1],rgb[2]))
       break
      else:
        print('A cor {} não foi encontrada na lista.'.format(busca_cor))
except:
    print("Erro!")
############################################################
    
######### QUESTAO 2 #########################################
lista_coordenadas = []
def distanciaEuclidiana(lista):
   x1, y1, z1 = lista[0]
   x2, y2, z2 = lista[1]
   d =  ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
   return d
   
try:
    for i in range(2):
        x = float(input('Informe a coordenada x do ponto {}: '.format(i+1)).strip())
        y = float(input('Informe a coordenada y do ponto {}: '.format(i+1)).strip())
        z  = float(input('Informe a coordenada z do ponto {}: '.format(i+1)).strip())
        lista_coordenadas.append((x,y,z))
    d = distanciaEuclidiana(lista_coordenadas)
    print('A distância entre os dois pontos é: {:.2f}'.format(d))
       
except:
    print("Erro!")
############################################################
    
######### QUESTAO 3 #########################################
tupla_escala = ([],[])
tupla_par =([],[])
tupla_impar =([],[])
dia = None
QTDE_FUNCIONARIOS = 30

def ordenar_inserir(tupla):
    for i in range(3):
        menor_valor = min(tupla[1])
        indice_dia = tupla[1].index(menor_valor)
        nome = tupla[0][indice_dia]
        del tupla[1][indice_dia]
        if menor_valor % 2 == 0:
            tupla_par[0].append(nome)
            tupla_par[1].append(menor_valor)
        else:
            tupla_impar[0].append(nome)
            tupla_impar[1].append(menor_valor)


def verificaFuncinarioJaEscolhido(nome):
    if nome in tupla_escala[0]:
        return False
    else:
        return True
def verificaDiaJaEscolhido(dia):
    if dia in tupla_escala[1]:
        return False
    else:
        return True

try:
    for i in range(QTDE_FUNCIONARIOS):

        nome = input('Informe o nome do enfermeiro(a) {}: '.format(i+1)).strip() 
        while not verificaFuncinarioJaEscolhido(nome):
            print('Nome ja consta na escala, Digite outro nome: ')
            nome = input('Informe o nome do enfermeiro(a) {}: '.format(i+1)).strip() 

        dia = int(input('Informe do dia de trabalho: ').strip())
        while (dia <= 0 or dia > 30) or not verificaDiaJaEscolhido(dia):
            if not verificaDiaJaEscolhido(dia):
               print('Dia inválido! ja possui funcionario ligado a este dia!')
            else:  
                print('Dia inválido! Digite um dia entre 1 e 30!')
            dia = int(input('Informe do dia de trabalho: ').strip())

        tupla_escala[0].append(nome)
        tupla_escala[1].append(dia)


    print('Pessoas no plantão ')
    print((tupla_escala))
    ordenar_inserir(tupla_escala)
    print('Pessoas no plantão (dias pares):')
    print(tupla_par)
    print('Pessoas no plantão (dias ímpares):')
    print(tupla_impar)
except:
    print("Erro!")
############################################################
    
######### QUESTAO 4 #########################################
CHAVES = 15
dict_valorQuadrado = {}
for i in range(CHAVES):
   dict_valorQuadrado[i+1] = (i+1) **2
print(dict_valorQuadrado)
############################################################

######### QUESTAO 5 #########################################
NUMERO_DE_VOLTAS = 3
NUMERO_DE_CORREDORES = 4
dict_corredor ={}
lista_tempo = []
media_geral = []
nomes_corredor =[]
for co in range(NUMERO_DE_CORREDORES):
    lista_tempo =[]
    nome = input('Informe o nome do corredor(a) {}: '.format(co+1)).strip().upper()
    for nv in range(NUMERO_DE_VOLTAS):
        tempo_segundos = int(input('Informe o tempo sem segundos da volta {} do corredor {} : '.format(nv+1,nome)).strip())
        while tempo_segundos <=0 or tempo_segundos >60:
            print('Tempo invalido! informe o tempo entre 1 e 60 segundos: ')
            tempo_segundos = int(input('Informe o tempo sem segundos da volta {} do corredor {} : '.format(nv+1,nome)).strip())
        lista_tempo.append(tempo_segundos)
    dict_corredor[nome] = lista_tempo
    del lista_tempo
nomes_corredor = [nome for nome in dict_corredor.keys()]
media_geral = [sum(media) / len(media) for _ , media in dict_corredor.items()]
menor_media = min(media_geral)
index_nomes_corredor = media_geral.index(min(media_geral))
nome_ganhador = nomes_corredor[index_nomes_corredor]
print('O campeão é {} com média de tempo de {:.2f} segundos.'.format(nome_ganhador,menor_media))
############################################################

######### QUESTAO 6 #########################################
numeros_maria = {'a': 100, 'b': 200, 'c': 300}
numeros_sara = {'a': 300, 'b': 200, 'd': 400, 'c': 500, 'e': 250}

if len(numeros_maria) > len (numeros_sara): 
   maior_dict =  numeros_sara.copy()
else:
    maior_dict = numeros_maria.copy()

for chave, valor in maior_dict.items():
    numeros_maria[chave] = numeros_sara[chave]

print('Os valores do dicionário numeros_maria são {}'.format(numeros_maria))
############################################################

######### QUESTAO 7 #########################################

dict_agenda ={}

def incluirAlterarContato():
    nome = input('Informe o nome: ').strip().upper()
    if nome in dict_agenda:
        alterar = input('Contato ja existe, deseja atualizar número? [S] ou [N]: ').strip().lower()
        if alterar == 's':
           novo_telefone = input('Informe o telefone : ').strip()
           dict_agenda[nome] = novo_telefone
           print('Contato alterado com sucesso!')
           input('') 
    else:
        novo_telefone = input('Informe o telefone : ').strip()
        dict_agenda[nome] = novo_telefone
        print('Contato adicionado com sucesso!')
        input('')
    return

def excluirContato():
    nome = input('Informe o nome: ').strip().upper()
    valor_removido = dict_agenda.pop(nome, 'não encontrado')
    if valor_removido == None:
        print(valor_removido)
    else:
        print('{} removido com sucesso!'.format(nome))
        input('')
    return

def buscarContato():
    nome = input('Informe o nome que deseja procurar: ').strip().upper()
    valor_procurado = dict_agenda.get(nome,'Não encontrador')
    if valor_procurado == None:
        print(valor_procurado)
    else:
        print('Número de telefone de {} é {}'.format(nome,valor_procurado))
        input('')
    return

def sair():
    print('Programa finalizado.')
    input('')
    exit()

def limpartela():
    os.system('cls')


menu ="""
    1. Incluir contato
    2. Excluir contato
    3. Buscar contato
    4. Sair
    """

while True:
    print(menu)
    op = int(input('Informe a opção: '))
    if op == 1:
       incluirAlterarContato()
    elif op == 2:
        excluirContato() 
    elif op == 3:
        buscarContato()
    else:
        sair()
    limpartela()
    print('Agenda:')
    print(dict_agenda)

############################################################
    
######### QUESTAO 8 #########################################
estoque_produto = {}
TEMPO_SLEEP = 2
def adicionar_produto(nome):
    if nome in estoque_produto:
        atualizar_estoque(nome)
    else:
        estoque = input('Informe a quantidade de estoque: ').strip()
        preco_uni = float(input('Informe o preço unitario do {} :'.format(nome)).strip())
        estoque_produto[nome] = [estoque,preco_uni]
        print('Produto {} adicionado ao estoque.!'.format(nome))
        sleep()
    return

def excluir_produto(nome):
    valor_removido = estoque_produto.pop(nome, 'não encontrado')
    if valor_removido == None:
        print(valor_removido)
    else:
        print('{} removido com sucesso!'.format(nome))
        sleep()
    return

def atualizar_estoque(nome):
     if nome in estoque_produto:
         alterar = input('Produto {} ja existe, deseja atualizar o estoque? [S] ou [N]: '.format(nome)).strip().lower()
         if alterar == 's':
            estoque = input('Informe a quantidade de estoque para atualização : ').strip()
            estoque_produto[nome][0] = estoque
            print('Estoque de {} atualizado para {} unidades'.format(nome,estoque))
            sleep()
     else:
        inserir = input('Produto {} NÃO existe, deseja inserir no  estoque? [S] ou [N]: '.format(nome)).strip().lower()
        if inserir == 's':
            adicionar_produto(nome)
        else:
            print('Obrigado!')
            sleep()

def listar_produtos_estoque():
   lista = """\n Lista de Produtos em Estoque: \n"""
   print(lista)
   for produto, inf in estoque_produto.items():
       print('Nome: {}'.format(produto))
       print('Quantidade em Estoque: {}'.format(inf[0]))
       print('Preço Unitario: {:.2f}'.format(inf[1]))

  
  
def valor_total_estoque():
    total = 0
    for _, inf in estoque_produto.items():
       total += float(inf[0]) * float(inf[1])
       print('Valor total do Estoque: {:.2f}'.format(total))
      
def sair():
    print('Programa finalizado.')
    sleep()
    print(estoque_produto)

def limpartela():
    os.system('cls')

def sleep():
    time.sleep(TEMPO_SLEEP)
    limpartela()


menu_estoque ="""
    ############################
      CONTROLE DE ESTOQUE v1.0
    ############################
      
    1. Incluir produto
    2. Excluir produto
    3. Atualizar estoque
    4. Exibir todo o estoque
    5. Calcular valor total do estoque
    6. Sair
    """
while True:
    print(menu_estoque)
    op = int(input('Informe a opção: '))

    if op == 1:
        nome = input('\n\nInforme o nome do produto: ').strip().upper()
        adicionar_produto(nome)
    elif op == 2:
        nome = input('\n\nInforme o nome do produto: ').strip().upper()
        excluir_produto(nome)
    elif op == 3:
        nome = input('\n\nInforme o nome do produto: ').strip().upper()
        atualizar_estoque(nome)
    elif op == 4:
        listar_produtos_estoque()
    elif op == 5:
        valor_total_estoque()
    elif op == 6:
        sair()
        break
  
############################################################
    
######### QUESTAO 9 #########################################
conta_banco = {}
TEMPO_SLEEP = 2
def adicionar_conta(conta):
    if conta in conta_banco:
        verifica_conta(conta)
    else:
        nome_titular = input('Informe o nome do titular  da conta {} :'.format(conta)).strip()
        saldo = float(input('Informe o saldo da conta {} :'.format(conta)).strip())
        conta_banco[conta] = {}
        conta_banco.get(conta, {}).update({'Nome': nome_titular})
        conta_banco.get(conta, {}).update({'Saldo': saldo})
        print('Conta criada com sucesso.')
        sleep()
    return

def verifica_conta(conta):
    print('Conta {} existente, você sera redirecionado ao menu para outras operações'.format(conta))
    sleep()
    

def realizar_saque(conta):
    if conta in conta_banco:
        valor_saque = float(input('Informe o valor de deseja sacar da conta {} :'.format(conta)).strip())
        if valor_saque > retorna_saldo(conta):
            print('Saldo insuficiente! Refaça a operação!.')
            sleep()
        else:
          valor = retorna_saldo(conta) - valor_saque
          conta_banco.get(conta, {}).update({'Saldo': valor})
          print('Saque de R$ {} efetuado com sucesso!'.format(valor_saque))
          print('você sera redirecionado para o menu incial.')
          sleep()

def retorna_saldo(conta):
    saldo = conta_banco.get(conta, {}).get('Saldo')
    return saldo

def realizar_deposito(conta):
    if conta in conta_banco:
        valor_deposito = float(input('Informe o valor de deseja depositar na conta {} :'.format(conta)).strip())
        valor = retorna_saldo(conta) + valor_deposito
        conta_banco.get(conta, {}).update({'Saldo': valor})
        print('Deposito de R$ {} efetuado com sucesso!'.format(valor_deposito))
        print('você sera redirecionado para o menu incial.')
        sleep()

def consultar_saldo(conta):
    print('Saldo da conta {} é R$: {:.2f}'.format(conta,retorna_saldo(conta)))
    print('você sera redirecionado para o menu incial.')
    sleep()

          
def sair():
    print('Programa finalizado.')
    sleep()
    print(conta_banco)

def limpartela():
    os.system('cls')

def sleep():
    time.sleep(TEMPO_SLEEP)
    limpartela()


menu_estoque ="""
    #################################
    CONTROLE DE CONTAS BANCARIAS v1.0
    #################################
      
    1. Criar uma nova conta
    2. Consultar o saldo de uma conta específica
    3. Realizar um saque em uma conta
    4. Realizar um depósito em uma conta
    5. Sair do programa
    """
while True:
    print(menu_estoque)
    op = int(input('Informe a opção: '))

    if op == 1:
        conta = input('\n\nInforme o número da conta: ').strip().upper()
        adicionar_conta(conta)
    elif op == 2:
        conta = input('\n\nInforme o número da conta: ').strip().upper()
        consultar_saldo(conta)
    elif op == 3:
        conta = input('\n\nInforme o número da conta: ').strip().upper()
        realizar_saque(conta)
    elif op == 4:
        conta = input('\n\nInforme o número da conta: ').strip().upper()
        realizar_deposito(conta)
    elif op == 5:
        sair()
        break
      
############################################################