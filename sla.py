pessoas = []
limc = []

def imc(peso,altura):
    return peso / altura**2
    
qtd = int(input('Quantas pessoas vão calcular o imc? '))

if qtd <= 0:
    print('Obrigado!')
else:
    for i in range(0,qtd):
        nome = input('Digite seu nome. ')
        pessoas.append(nome)
        alt = float(input('Digite sua altura. '))
        pes = float(input('Digite seu peso. '))
        
        limc.append(imc(pes,alt))
    final = dict(zip(pessoas,limc))

    print(final)
        