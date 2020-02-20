"""import math

def area_do_circulo(raio):
    
    area = (math.pi) * pow(raio,2)
    return area

def comprimento_do_circulo(raio):
    comprimento = 2 *  (math.pi * raio)
    return comprimento


i = 0
while i == 0:
    try:
        raio = float(input('Digite o raio do circulo: '))
    except ValueError:
        print('Digite um FLOAT SEU ANIMAL!!')
    else:
        i = 1

result_area = area_do_circulo(raio)
result_comprimento = comprimento_do_circulo(raio)

print('A área do circulo é: {}'.format(result_area))
print('O comprimento do circulo é: {}'.format(result_comprimento))

"""
nome = 'LUANA'
print('{:=^50}'.format(nome))