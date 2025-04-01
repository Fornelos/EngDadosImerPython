######################## LISTA 5 ############################
#ENGENHARIA E ANALISE DE DADOS 2025.1
#THIAGO FORNELOS DE ALBUQUERQUE
######### QUESTAO 1 #########################################
email = input('Informe um email valido!').strip().lower()
if '@' in email:
        print('E-mail válido!')
else:
    print('E-mail inválido!')
############################################################
    
######### QUESTAO 2 #########################################
frase = input('Informe uma frase: ').strip().upper()
palavra = input('Informe uma palavra contida na frase: ').strip().upper()
outra_palavra = input('Informe outra palavra que ele deseja substituir no lugar da primeira palavra inserida: ').strip().upper()
print(frase.replace(palavra,outra_palavra))
#############################################################

######### QUESTAO 3 #########################################
meses_do_ano = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
data_nasc = input('Informe a data de nascimento dd/mm/aaaa: ').strip().lower()
dia = int(data_nasc[0:2])
mes = int(data_nasc[3:5])
ano = int(data_nasc[6:])
print('Você nasceu em {} de {} de {}'.format(dia,meses_do_ano[mes-1],ano))

#############################################################

######### QUESTAO 4 #########################################
data_nasc = input('Informe a data de nascimento dd/mm/aaaa: ').strip().lower()
dia = data_nasc[0:2]
mes = data_nasc[3:5]
ano = data_nasc[6:]
senha = mes + '$' + dia[::-1] + '#' + dia + '!' + mes[::-1] + '*' + ano
print(senha)

#############################################################

######### QUESTAO 5 #########################################
numero_cel = input('Informe o numero de celular: ').strip().lower()
if '-' in numero_cel and len(numero_cel) == 9:
    numero_cel = '9' + numero_cel
elif '-' not in numero_cel and len(numero_cel) == 8:
    numero_cel = '9' + numero_cel
elif '-' in numero_cel and len(numero_cel) == 10:
    pass
print(numero_cel)
#############################################################

######### QUESTAO 6 #########################################
alunos =[]
notas =[]

for i in range(3):
     lista_temp =[]
     nome = input('Nome do aluno: {} '.format(i+1))
     alunos.append(nome)
     for j in range(3):
        nota = float(input('Informe a nota {} do aluno {}: '.format(j+1,i+1)))
        lista_temp.append(nota)
     notas.append(lista_temp)
     del lista_temp

for i , aluno in enumerate(alunos):
    media = sum(notas[i]) / len(notas[i])
    nome = str(aluno).capitalize()
    if media >=7.0:
        situacao = 'aprovado(a)'
    else:
        situacao = 'reprovado(a)'
    print('A média de {} é {:.2f} e ele(a) está {}'.format(nome,media,situacao))
#############################################################


