######################## LISTA 6 ############################
#ENGENHARIA E ANALISE DE DADOS 2025.1
#THIAGO FORNELOS DE ALBUQUERQUE
######### QUESTAO 1 #########################################

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
    print(lista_cor)
    for cor , rgb in lista_cor:
      if cor == busca_cor:
       print('Valores RGB para a cor {}: Red={}, Green={}, Blue={}'.format(cor,rgb[0],rgb[1],rgb[2]))

except:
    print("Erro!")
############################################################
