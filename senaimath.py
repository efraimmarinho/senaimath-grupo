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