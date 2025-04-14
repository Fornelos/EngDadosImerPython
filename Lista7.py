######################## LISTA 7 ############################
#ENGENHARIA E ANALISE DE DADOS 2025.1
#THIAGO FORNELOS DE ALBUQUERQUE
import os
import time
######### QUESTAO 1 #########################################

dict_quadrado ={}

def quadrado(x):
    for i in range(x):
        dict_quadrado[i+1]=(i+1)**2
    return

def main():
    quadrado(15)
    print(dict_quadrado)

if __name__ == "__main__":
    main()
############################################################
    
######### QUESTAO 2 #########################################
NUMERO_DE_VOLTAS = 3
NUMERO_DE_CORREDORES = 4


dict_corredor ={}

def calcular_media(lista_tempos):
    media_tempo_corredor = sum(lista_tempos) / len(lista_tempos)
    return media_tempo_corredor


def  encontrar_campeao(corredor):
    menor_media = float('inf')  # Inicializa com um valor muito alto
    for nome, lista in corredor.items():
      media = calcular_media(lista)
      if media < menor_media: 
            menor_media = media
            nome_campeao = nome
    return nome_campeao, menor_media


def main():
    for co in range(NUMERO_DE_CORREDORES):
        lista_tempos_corredor = []
        nome = input('Informe o nome do corredor(a) {}: '.format(co+1)).strip().upper()
        for nv in range(NUMERO_DE_VOLTAS):
            tempo_segundos = float(input('Informe o tempo sem segundos da volta {} do corredor {} : '.format(nv+1,nome)).strip())
            while tempo_segundos <=0 or tempo_segundos >60:
                print('Tempo invalido! informe o tempo entre 1 e 60 segundos: ')
                tempo_segundos = float(input('Informe o tempo sem segundos da volta {} do corredor {} : '.format(nv+1,nome)).strip())
            lista_tempos_corredor.append(tempo_segundos)
        dict_corredor[nome] = lista_tempos_corredor
        del lista_tempos_corredor
    nome_campeao, menor_media = encontrar_campeao(dict_corredor)
    print(f'O campeão é {nome_campeao} com média de tempo de {menor_media:.2f} segundos.')

if __name__ == "__main__":
    main()
#############################################################
    
######### QUESTAO 3 #########################################
TEMPO_SLEEP =2
dict_agenda ={}

def incluirAlterarContato():
    nome = input('Informe o nome: ').strip().upper()
    if nome in dict_agenda:
        alterar = input('Contato ja existe, deseja atualizar número? [S] ou [N]: ').strip().lower()
        if alterar == 's':
           novo_telefone = input('Informe o telefone : ').strip()
           dict_agenda[nome] = novo_telefone
           print('Contato alterado com sucesso!')
           sleep()
    else:
        novo_telefone = input('Informe o telefone : ').strip()
        dict_agenda[nome] = novo_telefone
        print('Contato adicionado com sucesso!')
        sleep()
    return

def excluirContato():
    nome = input('Informe o nome: ').strip().upper()
    valor_removido = dict_agenda.get(nome, 'não encontrado')
    if valor_removido == 'não encontrado':
        print(f'{nome} - {valor_removido}')
        sleep()
    else:
        valor_removido = dict_agenda.pop(nome, 'não encontrado')
        print('{} removido com sucesso!'.format(nome))
        sleep()
    return

def buscarContato():
    nome = input('Informe o nome que deseja procurar: ').strip().upper()
    valor_procurado = dict_agenda.get(nome,'Não encontrado')
    if valor_procurado == 'Não encontrado':
       print(f'{nome} - {valor_procurado}')
       sleep()
    else:
        print('Número de telefone de {} é {}'.format(nome,valor_procurado))
        sleep()
    return

def sair():
    print('Programa finalizado.')
    sleep()
    print(dict_agenda)


def limpartela():
    os.system('cls')

def sleep():
    time.sleep(TEMPO_SLEEP)
    limpartela()


menu ="""
    1. Incluir contato
    2. Excluir contato
    3. Buscar contato
    4. Sair
    """
def main():
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

if __name__ == "__main__":
    main()
#############################################################

######### QUESTAO 4 #########################################
numeros_maria = {'a': 100, 'b': 200, 'c': 300}
numeros_sara = {'a': 300, 'b': 200, 'd': 400, 'c': 500, 'e': 250}

def atualizar_numeros (dict1, dict2):
    if len(dict1) > len (dict2): 
     maior_dict =  dict2.copy()
    else:
     maior_dict = numeros_maria.copy()

    for chave, _ in maior_dict.items():
        numeros_maria[chave] = numeros_sara[chave]
    return numeros_maria

def main():
    atualizar_numeros(numeros_maria, numeros_sara)
    print('Os valores do dicionário numeros_maria são {}'.format(numeros_maria))

if __name__ == "__main__":
    main()

#############################################################



