######################## LISTA 4 ############################
#ENGENHARIA E ANALISE DE DADOS 2025.1
#THIAGO FORNELOS DE ALBUQUERQUE


######### QUESTAO 1 #########################################

lista_idade =[]
PARADA = -1
while True:
    try:
        idade = int(input('Informe a idade: '))
        if idade == PARADA:
            break
        else:
            lista_idade.append(idade)
        print('Quantidade de idades válidas: {}'.format(len(lista_idade)))
        print('Idades armazenadas: {}'.format(lista_idade))
        media = sum(lista_idade) / len(lista_idade)
        print('Média das idades: {}'.format(media))
        lista_idade_acima_media = [idade for idade in lista_idade if idade > media]
        print('Quant. de idades acima da média: {}'.format(len(lista_idade_acima_media)))
        print('Maior idade: {}'.format(max(lista_idade)))
        print('Menor idade: {}'.format(min(lista_idade)))
        lista_idade_menos_18 = [idade for idade in lista_idade if idade <18]
        print('Quant. de idades abaixo de 18: {}'.format(len(lista_idade_menos_18)))
    except:
      print('Error!')
#############################################################

######### QUESTAO 2 #########################################

lista_medias =[]
try:
    for i in range(5):
        nota1 = int(input('Informe a Nota 1 do Aluno {}: '.format(i+1)))
        nota2 = int(input('Informe a Nota 2 do Aluno {}: '.format(i+1)))
        media = (nota1 + nota2) / 2
        lista_medias.append(media)
    print('Médias: {}'.format(lista_medias))
    lista_media_acima_7 =[media for media in lista_medias if media>=7.0]
    print('Número de estudantes com média >= 7: {}'.format(len(lista_media_acima_7)))
except:
    print('Error!')
#############################################################
    
######### QUESTAO 3 #########################################
lista_geral =[]

try:
    for i in range(10):
        numero = int(input('Informe o numero {}: '.format(i+1)))
        lista_geral.append(numero)
    
    lista_par = [numero for numero in lista_geral if numero % 2==0]
    lista_impar = [numero for numero in lista_geral if numero % 2!=0]
    print('Números: {}'.format(lista_geral))
    print('Pares: {}'.format(lista_par))
    print('Ímpares: {}'.format(lista_impar))
except:
    print('Error!')

#############################################################

######### QUESTAO 4 ######################################### 
meses_do_ano = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
dict_media_temp ={}
try:
    for i ,mes in enumerate(meses_do_ano):
        temperatura = float(input('Informe a media de temperatura do mês {}: '.format(meses_do_ano[i])))
        dict_media_temp[mes] = temperatura
    media_anual = sum(dict_media_temp.values()) / len(dict_media_temp)
    print('\nMédia Anual de Temperaturas: {:.2f}'.format(media_anual))
    acima_da_media = {mes:temp for mes, temp in dict_media_temp.items() if temp > media_anual}
    #print(acima_da_media)
    print('\nMeses com temperaturas acima da média:\n')
    for mes, valor in acima_da_media.items():
       print('{}'.format(mes))
except:
     print('Error!')
        
#############################################################
    
######### QUESTAO 5 #########################################

vendas_vendedor ={}
try:
    quantidade_vendedor = int(input('Informe a quantidade de vendedor(es) :'))
    for i in range(quantidade_vendedor):
        nome = input('Informe o nome do vendedor: ')
        vendas_ano = float(input('Informe o valor de venda anual: '))
        vendas_vendedor[nome] = vendas_ano
    menor_valor_vendas = min(vendas_vendedor.values())
    maior_valor_vendas = max(vendas_vendedor.values())

    for nome, valor in vendas_vendedor.items():
        if valor <= menor_valor_vendas:
            print('{}: {} - Menor volume de vendas!'.format(nome,valor))
        elif valor >= maior_valor_vendas:
            print('{}: {} - Maior volume de vendas!'.format(nome,valor))
        else:
            print('{}: {}'.format(nome,valor))
except:
    print('Error!')
#############################################################
    
######### QUESTAO 6 #########################################
dict_restaurantes ={}
nome_restaurante = ''
def novaMediaRestaurante(restaurante,mediaAnterior,numeroAvaliacoes,novaNota):
    nova_media = (mediaAnterior * numeroAvaliacoes + novaNota) / (numeroAvaliacoes + 1)
    dict_restaurantes[restaurante] = [nova_media,numeroAvaliacoes + 1]
    return

try:
    while True:
        nome_restaurante = input('Informe o nome do restaurante ou PARE para sair: ').strip().lower()
        if nome_restaurante == 'pare':
            break
        nota = int(input('Informe nota para o restaurante {} :'.format(nome_restaurante)))
        if nota != 0 and  nota != 1 and  nota != 2 and  nota != 3 and  nota != 4 and  nota != 5:
            print('Digite uma nota de 0 a 5!')
            continue
        if nome_restaurante in dict_restaurantes:
            novaMediaRestaurante(nome_restaurante,dict_restaurantes[nome_restaurante][0],dict_restaurantes[nome_restaurante][1],nota)
        else:
            dict_restaurantes[nome_restaurante] = [nota,1]

    chaves = list(dict_restaurantes.keys())
    lista_media = [dict_restaurantes[chave][0] for chave in chaves]
    maior = max(lista_media)
    menor = min(lista_media)
    indice_maior_nota = lista_media.index(maior)
    indice_menor_nota = lista_media.index(menor)

    print('Restaurante com a maior nota:  {} - Nota média: {}'.format(chaves[indice_maior_nota],maior))
    print('Restaurante com a menor nota:  {} - Nota média: {}'.format(chaves[indice_maior_nota],menor))
except:
    print('Error!')
#############################################################













