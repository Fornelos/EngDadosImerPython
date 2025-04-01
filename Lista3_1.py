######################## LISTA 3 parte 1 ############################
#ENGENHARIA E ANALISE DE DADOS 2025.1
#THIAGO FORNELOS DE ALBUQUERQUE


######### QUESTAO 1 #########################################
lista_idades =[]
i = 1

while True:
    try:
        idade = int(input('Informe a idade {}: '.format(i)))
        if idade == -1:
            break
        else:
            lista_idades.append(idade)
        if lista_idades:
            total_idades = len(lista_idades)
            media_idade = sum(lista_idades) / total_idades
            lista_maior_25 = [idade for idade in lista_idades if idade >= 25]
            lista_menor_25 = [idade for idade in lista_idades if idade < 25]

            print('Total de idades : {}'.format(total_idades))
            print('Média das idades: {}'.format(media_idade))
            print('Maiores e iguais a 25 anos: {}'.format(len(lista_maior_25)))
            print('Menores de 25 anos: {}'.format(len(lista_menor_25)))
    except:
      print('Entrada Invalida!')

#############################################################

######### QUESTAO 2 #########################################
lista_notas =[]
i = 1
while True:
    nota = int(input('Informe a nota {}: '.format(i)))
    if nota == -1:
        break
    elif nota not in(1,2,3,4,5):
        print('Nota inválida!')
        continue
    else:
        lista_notas.append(nota)
        i+=1
if lista_notas:
    media_notas = sum(lista_notas) / len(lista_notas)
    print('Média das notas {}:'.format(media_notas))

#############################################################

######### QUESTAO 3 #########################################
dict_produto = {}
while True:
    produto = input('Informe o nome do produto ou FIM para sair: ').lower()
    if 'fim' in produto:
        break
    quantidade = int(input('Informe a quantidade: '))
    if quantidade <=0:
        print('Não é possível cadastro de estoque zero ou negativo.!')
        continue
    else:
        #Trecho não pede na questao, mas se o produto ja estiver no dicionario ele soma a quantidade ja existente.
        if produto in dict_produto:
            dict_produto[produto] += quantidade
        else:
            dict_produto[produto] = quantidade

print('Tipos de produtos cadastrados: {}'.format(len(dict_produto)))
print(dict_produto)

#############################################################

######### QUESTAO 4 #########################################
pet_servicos ={}
lista_servicos =['banho','tosa','banho e tosa','outros']
for i in range(10):
    servicos = """
    Escolha a opçõa do serviço {}:
    1 - banho
    2 - tosa
    3 - banho e tosa
    4- outros. 
    """.format(i+1)
    print(servicos)
    opcao = int(input(''))
    if opcao not in(1,2,3,4):
        print('Opçao inválida!')
        continue
    elif lista_servicos[opcao-1]  in pet_servicos:
        pet_servicos[lista_servicos[opcao-1]] += 1
    else:
        pet_servicos[lista_servicos[opcao-1]] = 1
print(pet_servicos)
#############################################################
        


    




