######################## LISTA 2 ############################
#ENGENHARIA E ANALISE DE DADOS 2025.1
#THIAGO FORNELOS DE ALBUQUERQUE


######### QUESTAO 1 #########################################
estado_civil = input("informe seu estado civil o (Solteiro, Casado, Viúvo, Divorciado): ").lower()[0]
if estado_civil not in ['s','c','v','d']:
    print("Entrada Invalida!")
else:
    match estado_civil:
        case 's':
            print("Solteiro")
        case 'c':
            print("Casado")
        case 'v':
            print("Viúvo")
        case 'd':
            print("Divorciado")
#############################################################
            
######### QUESTAO 2 #########################################
tabela_cargo = {1:45.0, 2:35.0, 3:25, 4:15, 5:0}

def calculaSalario(salario, cod_cargo):
  perc = tabela_cargo[cod_cargo]
  valor_aumento = salario * (perc/100)
  salario += valor_aumento
  return salario

tabela ="""
        Código do Cargo   Cargo        Aumento
            1         Secretário        45%
            2         Tesoureio         35%
            3         Professor         25%
            4         Coordenador       15%
            5         Diretor           0%
"""
print(tabela)
codigo = int(input("Selecione o codigo do cargo: "))
if codigo not in [1,2,3,4,5]:
    print("Opção Invalida!")
else:
    salario = float(input("Informe o salário : "))
    novo_salario = calculaSalario(salario,codigo)
    print(f'Salário atualizado: {novo_salario}')
#############################################################
    
######### QUESTAO 3 #########################################
dia_da_semana =('Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sábado')
dia = int(input('Selecione um numero de 1 a 7: '))
if dia not in [1,2,3,4,5,6,7]:
    print("Opção Invalida!")
else:
    print(dia_da_semana[dia-1])
 #############################################################

 ######### QUESTAO 4 #########################################
try:
    quantidade_infracoes = int(input('Insira o número de infrações que cometeu no último ano  : '))
    if quantidade_infracoes == 0:
        print("Motorista Exemplar!")
    elif quantidade_infracoes > 0 and quantidade_infracoes <=3:
        print("Motorista Atento!")
    elif quantidade_infracoes > 4 and quantidade_infracoes <=6:
        print("Motorista Desatento!")
    else:
        print("Motorista Perigoso!")
except:
    print("Valor invalido!")
#############################################################
    
######### QUESTAO 5 #########################################
DESCONTO = 10.0
QUANTIDADE_DIARIA = 5
suite_maximo_diarias = {1:15,2:10,3:7}
suite_valores ={1:250.00,2:500.00,3:1200.00}

def checarDescontoSuite(quant_diarias):
    if quant_diarias >= QUANTIDADE_DIARIA:
        return True
    else:
        return False

def checarQuantidadeDiarias(opcao,quant_diarias):
    if quant_diarias <= suite_maximo_diarias[opcao]:
        return True
    else:
        return False
    
def retornaTotalDiaria (opcao,quant_diarias):
    total_sem_desconto = quant_diarias * suite_valores[opcao]
    valor_desconto = total_sem_desconto * (DESCONTO /100)
    total_com_Desconto = total_sem_desconto - valor_desconto
    return total_com_Desconto ,total_sem_desconto 

suites ="""
 
     Opção       Suite           Preço    Limite de diárias
       1         Standard         250,00          15
       2         Luxo             500,00          10
       3         Presidencial     1200,00          7
"""
print(suites)
try:
    opcao_suite = int(input("Informe a opção de desejada: "))
    if opcao_suite not in [1,2,3]:
       print("Opção Invalida!")
    else:
        quantiadade_diarias = int(input("Informe quantidades de diarias / noites : "))
        if not checarQuantidadeDiarias(opcao_suite,quantiadade_diarias):
            print("Limite de noites atingido.!")
        else: 
            total_com_desconto ,total_sem_desconto  = retornaTotalDiaria(opcao_suite,quantiadade_diarias)
            if checarDescontoSuite(quantiadade_diarias):
                print("Valor total da estadia R$ {} :".format(total_com_desconto))
            else:
                print("Valor total da estadia R$ {} :".format(total_sem_desconto))
except:
    print("Valor Inválido!")
#############################################################
    
######### QUESTAO 6 #########################################
DESCONTO = 50.0
IDADE_CRIANCA = 12
IDADE_IDOSO = 65
sala_valor_ingresso = {1:20,2:25,3:30}

def checarDescontoIdade(idade):
    if idade <= IDADE_CRIANCA or idade >=IDADE_IDOSO:
        return True
    else:
        return False

def calcularDesconto(opcao):
    total_sem_desconto = sala_valor_ingresso[opcao]
    valor_desconto = total_sem_desconto * (DESCONTO /100)
    total_com_Desconto = total_sem_desconto - valor_desconto
    return total_com_Desconto ,total_sem_desconto 


salas ="""
 
     Opção       Sala                Preço  
       1         Sessão Matinê       20,00       
       2         Sessão Vespertina   25,00  
       3         Sessão Noturna      30,00
"""
print(salas)

try:
    opcao_sala = int(input("Informe a opção de desejada: "))
    if opcao_sala not in [1,2,3]:
       print("Opção Invalida!")
    else:
        idade = int(input("Informe sua idade : "))
        total_com_desconto ,total_sem_desconto  = calcularDesconto(opcao_sala) 
        if not checarDescontoIdade(idade):
            estudante = input('Você é estudante? SIM ou NÃO: ').lower()[0]
            if estudante =='s':
                print('Valor do ingresso: R$ {}'.format(total_com_desconto))
            else:
                print('Valor do ingresso: R$ {}'.format(total_sem_desconto))
        else:
            print('Valor do ingresso: R$ {}'.format(total_com_desconto))
except:
    print("Valor Inválido!")
#############################################################


######### QUESTAO 7 #########################################
VALOR_ADD_MINUTO = 1
VALOR_ADD_GIGAS10GB = 10
valor_minuto_adicional = 0
valor_giga_adicional = 0

plano_valor = {1:50,2:80,3:120}  
plano_minutos = {1:100,2:300,4:500}
plano_gigas = {1:5,2:10,3:20}

def verificaFranquiaMinutosGigas(plano,minutos,gigas):
    if plano == 1:
        minutos_adcionais = minutos - plano_minutos[plano]
        gigas_adionais = gigas - plano_gigas[plano]
    elif plano == 2:
        minutos_adcionais = minutos - plano_minutos[plano]
        gigas_adionais = gigas - plano_gigas[plano]
    else:
        minutos_adcionais = minutos - plano_minutos[plano]
        gigas_adionais = gigas - plano_gigas[plano]

    if minutos_adcionais <=0:
      minutos_adcionais = 0
    if gigas_adionais <= 0:
      gigas_adionais = 0

    return minutos_adcionais, gigas_adionais

def CalcularValorMinutoAdicional(minutos_adicionais):
    valor = minutos_adicionais * VALOR_ADD_MINUTO
    return valor

def CalcularValorGigaAdicional(gigas_adicionais):
    valor = gigas_adicionais * VALOR_ADD_GIGAS10GB
    return valor


planos ="""
 
     Opção       Sala                 Preço  
       1         Plano Básico         50,00       
       2         Plano Intermediário  80,00  
       3         Plano Avançado       120,00
"""
print(planos)

try:
    opcao_plano = int(input("Escolha o plano desejado: "))
    if opcao_sala not in [1,2,3]:
       print("Opção Invalida!")
    else:
        minutos_utilizados = int(input("Quantos minutos foram utlizados? "))
        gigas_utilizados = int(input("Quantos Gigas foram utlizados? "))

        minutos_adcionais,gigas_adionais = verificaFranquiaMinutosGigas(opcao_plano,minutos_utilizados,gigas_utilizados)
        if minutos_adcionais >= 0:
            valor_minuto_adicional = CalcularValorMinutoAdicional(minutos_adcionais)
        if gigas_adionais >= 0:
            valor_giga_adicional = CalcularValorGigaAdicional(gigas_adionais)

        total_fatura = plano_valor[opcao_plano] + valor_minuto_adicional + valor_giga_adicional
        print("Valor da fatura: R$ {}".format(total_fatura))
except:
    print("Valor Inválido!")

#############################################################