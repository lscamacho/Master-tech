def somar(valor1, valor2):

    resultado = valor1 + valor2
    return resultado

 

valor1 = int(input('Digite o valor 1: '))
valor2 = int(input('Digite o valor 2: '))

result = somar(valor1, valor2)

if result > 40:
   print('O valor da soma é: {}'.format(result))
    
else:
    print ('Ops, só retorno valores maiores que 40')


