print('\n --- CALCULADORA DE IMC ---')
nome = input('Digte seu nome ')
altura = float(input('Digite sua altura (m) '))
peso = float(input('Dgite seu peso (kg) '))
imc = peso / (altura **2)

print(f'\n --- Resultado do seu IMC {nome} \n')
print(f'seu imc é {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 24.9:
    print('Você está dentro do peso')
elif 25 <= imc < 29.9:
    print('Você está com sobrepeso')
elif 30 <= imc < 34.9:
    print('Você está com obesidade grau 1')
elif 35 <= imc < 39.9:
    print('Você está com obesidade grau 2')
else: 
    print('Você está com obesidade grau 3')

print(f'\n --- Fim do Calculo de IMC ---')
    