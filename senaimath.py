def logefra(x, k=1000):   # Defino essa função para fazer o calculo mais preciso do logaritmo natural usando a séria de tylor então quanto maior o numero mais preciso será mas o padrao e em torno de 100.
    if x <= 0:     # Verifica se o valor de x é menor ou igual a 0, por conta que o logaritmo é o natural e nao aceita valores negativos e etc.
        return 0
    
    somatorio = 0
    for i in range(k + 1):
        termo = (1 / (2 * i + 1)) * (((x - 1) / (x + 1)) ** (2 * i + 1)) # Calcula o termo da série de Taylor para ln(x)
        somatorio += termo  # acumula o valor das exponenciais para obter o resultado final da série de Taylor
        
    return 2 * somatorio # Multiplicado por 2 para obter o resultado final da Formula do PDf

valor_x = float(input("Digite o valor de x (maior que 0) para calcular o ln(x): ")) 

resultado = logefra(valor_x) # chama a funcao logefra para calcular o logaritmo natural do valor de x fornecido pelo usuário

print(f"O valor aproximado de ln({valor_x}) é: {resultado}")



def PiValue(x): #X =  A numero de termos, quanto mais tiver mais preciso o resultado é 
    soma = 0 #Valor de pi que vai ser acrescido depois 
    
    for i in range(x): #aqui ele soma ate o termo informado e acresce no soma 
        soma += ((-1)**i) / (2*i + 1)  #aqui acontece a inversao dos sinais e a a soma do numero impar escolhido no input dos termos

    return 4 * soma # Multiplica tudo por 4 igual na formula 


ntermos = int(input("Insira o numero de termos que vc deseja: ")) #usuario esoclher o tanto de termos

print(PiValue(ntermos)) #print valor de pi


#/

def fatorial(x):

    resultado = 1
    for i in range(1, x + 1):
        resultado *= i

    return resultado


def cosseno(y, termos=20):

    resultado = 0

    for x in range(termos):
        conta = (-1) ** x
        resultado += conta * (y ** (2 * x)) / fatorial(2 * x)

    return resultado


valor = int(input('Digite o valor desejado em graus: '))

radiano = valor * 0.0174533

print(cosseno(radiano))
# Função que calcula uma aproximação de e^x usando a série de Taylor
def exponencial(exp):

    # Define a quantidade de termos da série que serão usados no cálculo
    # Quanto maior o número de termos, maior a precisão
    termos = int(2 * abs(exp))

    # Inicializa o fatorial com 1 (0! = 1)
    fatorial = 1

    # Inicializa a soma com 1, que é o primeiro termo da série
    soma = 1

    # Inicializa o numerador (x^n) com 1
    numerador = 1

    # Loop que calcula os termos da série
    for n in range(1, termos):

        # Calcula x^n multiplicando pelo valor de exp a cada iteração
        numerador *= exp

        # Calcula n! progressivamente
        fatorial *= n

        # Soma o termo atual da série: (x^n / n!)
        soma += numerador / fatorial

    # Retorna o valor final da soma (aproximação de e^x)
    return(soma)


# Solicita ao usuário um valor para calcular e^x
exp = float(input("Digite: "))

# Chama a função exponencial passando o valor digitado
resultado = exponencial(exp)

# Mostra o resultado final
print(resultado)
print(PiValue(ntermos)) #print valor de pi


print('----- Seno -----')

def fatorial(n): #comeca com 1 pois e a base do fatorial
    resultado = 1
 
 
    for i in range(1, n + 1): #ele vai receber um bloco de codigo e vai contar de 1 ate n
        
        resultado *= i #ele vai multiplicar acumulando, por exemplo n = 4  | 1 x 1 x 2 x 3 x 4

    return resultado
    

def seno(x, termos = 10): # definiu termos = 10 pois e um numero equilibrado para boa aproximacao
    
    soma = 0 #variavel para guardar o resultado

    
    for n in range (termos): #vai repetir quantas vezes o termos for chaamado
        
        expoente = 2 * n + 1 # vai gerar 1, 3, 4, 5, 7 | Pq e a formula do seno usa pra potencias impares

        sinal = (-1) ** n #ele vai alternar o sinal | n = 0 + 1 n 1 - 1 | vai alternar entre + e -
        
        termo = sinal * (x ** expoente) / fatorial(expoente) #vai montar cada parte da formula
                        
        soma += termo #vai somar tudo
        
    return soma
    
x = float(input('Digite o valor de x (em radianos): '))
termos = int(input('Digite a quantidade de termos da série: '))

resultado = seno(x, termos)

print("Seno aproximado:", resultado)
