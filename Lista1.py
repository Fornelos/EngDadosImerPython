######################## LISTA 1 ############################
#ENGENHARIA E ANALISE DE DADOS 2025.1
#THIAGO FORNELOS DE ALBUQUERQUE

######### QUESTAO 1 #########################################
PI = 3.14
def calculaRadiano(grau):
  return (grau * PI) / 180

grau = float(input('Informe o grau a ser convertido para radianos:'))
radiano =calculaRadiano(grau)
print('{} graus em radianos é {}.'.format(grau,radiano))


#############################################################

######### QUESTAO 2 #########################################
def calculaDesconto(valor, percDesconto):
  valor -= (valor * (percDesconto/100))
  return valor 

valor_original = float(input('Informe o valor original:'))
porcentagem_desconto = float(input('Informe a % de desconto:'))
valor_com_desconto = calculaDesconto(valor_original,porcentagem_desconto)
print('Valor com desconto é: {}.'.format(valor_com_desconto))

#############################################################

######### QUESTAO 3 #########################################

def areaHeron(*arg):
  a,b,c = arg
  s = (a+b+c)/2
  raiz = s *((s-a)*(s-b)*(s-c))
  raiz = raiz**0.5
  return raiz

a = float(input('Informe o valor de a:'))
b= float(input('Informe o valor de b:'))
c= float(input('Informe o valor de c:'))
print('Area do triangulo é : {}.'.format(areaHeron(a,b,c)))

#############################################################

######### QUESTAO 4 #########################################

def valorFuturo(valor_inicial,tx_juros,tempo):
  juros_dia = valor_inicial * (tx_juros/100)
  juros_tempo = juros_dia * tempo
  valor_inicial += juros_tempo
  return   valor_inicial 

valor = float(input('Informe o valor R$:'))
juros = float(input('Informe a taxa de juros:'))
tempo = int(input('Informe o tempo em dias:'))

print('O valor corrigido foi de: {}.'.format(valorFuturo(valor,juros,tempo)))
#############################################################

######### QUESTAO 5 #########################################

def calculaComissao(valor, percomissao):
  valor *= (percomissao/100)
  return valor 

valor_original = float(input('Informe o valor das vendas :'))
comissao = float(input('Informe a % de comissão :'))
valor_comissao = calculaComissao(valor_original,comissao)
print('Valor com desconto é: {}.'.format(valor_comissao))
#############################################################

######### QUESTAO 6 #########################################
PI = 3.14
def areaCirculo(raio):
  area = PI * raio**2
  return area
try:
 raio = float(input('Informe o raio: '))
 print('Para ao raio {} a Area é de {}'.format(raio, areaCirculo(raio)))
except:
  print('Valor Invalido!')
#############################################################
  
######### QUESTAO 7 #########################################
def calculaLucroBruto(*args):
  custo, venda = args
  lucro_bruto = venda - custo
  return lucro_bruto

try:
  custo = float(input('Informe o custo de produção : '))
  venda = float(input('Informe o valor de venda : '))
  print('Seu custo foi de R$: {} e o valor de venda foi de R$: {}. Lucro Bruto R$: {}'.format(custo,venda, calculaLucroBruto(custo,venda)))
except:
  print('Valor Invalido!')
#############################################################
  
######### QUESTAO 8 #########################################
def celsiusFahrenheit(c):
  f = (9 / 5) * c + 32
  return f

try:
  celsius = float(input('Informe o grau Celsius : '))
  print('A conversão de {} grau CELSIUS para FAHENHEIT é {} graus'.format(celsius,celsiusFahrenheit(celsius)))
except:
  print('Valor Invalido!')
############################################################
  
######### QUESTAO 9 #########################################
def calculaImposto(valor, imposto):
  valor *= (imposto/100)
  return valor 
try:
  valor_produto = float(input('Informe o valor do produto :'))
  imposto = float(input('Informe a % de imposto :'))
  valor_do_imposto = calculaImposto(valor_produto,imposto)
  print('Valor final com Imposto R$: {}.'.format(valor_produto + valor_do_imposto))
except:
  print('Valor Invalido!')
############################################################

######### QUESTAO 10 ########################################
def calculaValorParcela(valor, parcela):
   valor_parcela = valor / parcela
   return valor_parcela
try:
  valor_compra = float(input('Informe o valor da compra :'))
  parcela = float(input('Informe a quantidade de parcelas :'))
  if(parcela <=0):
     pass
  else:
    valor_da_parcela = calculaValorParcela(valor_compra,parcela)
    
  print('Valor de cada parcela R$: {}.'.format(valor_da_parcela))
except:
  print('Valor Invalido!')
############################################################





  











































