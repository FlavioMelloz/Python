print('By Flávio')

print('Bem vindo ao conversor de moedas.')
print('Por favor não use virgulas, use pontos para separar os numeros.')
print('')
print('Digite real, para converter real para euro')
print('Digite euro, para converter euro para real')

def convert(moeda2,valor2):
    valor = float(valor2)
    moeda = moeda2
    if moeda == 'euro':
        conver = float(valor2) * 6
        numero = format(conver, '.2f')
        print(f'${valor2} Euros é aproximadamente R${numero} reais')
    elif moeda == 'real':
        euro = 16
        euro = int(euro)
        valor2 = float(valor2)
        conver = (valor2) * euro / 100
        conver + 1
        conver = float(conver)
        if valor2 > 12:
            print(f'{valor2} Reais é aproximadamente ${conver} euros')
        else:
            print(f'{valor2} Reais é aproximadamente ${conver} euro')
        return
convert(moeda2=(input('Digite uma moeda para conversão: ')), valor2=input('Digite um valor para conversão: '))







