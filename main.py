import random
oportunidades = 0
print('Hola, como te llamas??')
name = input()
numero = random.randint(1, 50)
print('Bienvenido, ' + name + ', dime en que número estoy pensando del 1 al 50, solo tienes 6 oportunidades.')

for x in range(1, 51):
    x = input()
    x = int(x)
    if x > numero:
        oportunidades += 1
        print('Demasiado alto.')
    if x < numero:
        oportunidades += 1
        print('Demasiado bajo.')
    if x == numero:
        print('ganaste')
        oportunidades += 1
    if oportunidades == 6:
        break
if oportunidades == 6:
    x != numero
    print('perdiste el numero era ' + str(numero))
