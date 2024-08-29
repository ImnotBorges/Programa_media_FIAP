# Programa feito para calcular a média na FIAP
#1° Semestre
check1 = float(input('Nota checkpoint 1: '))
check2 = float(input('Nota checkpoint 2: '))
check3 = float(input('Nota checkpoint 3: '))

check_menor1 = min(check1,check2,check3)

if check_menor1 == check1:
    soma_check1 = check2 + check3
elif check_menor1 == check2:
    soma_check1 = check1 + check3
else:
    soma_check1 = check1 + check2

checkpoint = soma_check1 * 0.1
print(f'Nota checkpoint 1° semestre: {checkpoint}')

sprint1 = float(input('Nota sprint 1: '))
sprint2 = float(input('Nota sprint 2: '))

soma_sprint1 = (sprint1 + sprint2)*0.1
print(f'Nota Sprints do 1° semestre: {soma_sprint1}')

global1 = float(input('Nota da Global Solution: '))
gs1 = global1*0.6
print(f'Nota do primeiro Global Solution: {gs1}')

media1 = (checkpoint + soma_sprint1 + gs1)*0.4
print(f'Sua nota do primeiro semestre foi: {media1}')

#2° Semestre
check4 = float(input('Nota checkpoint 4: '))
check5 = float(input('Nota checkpoint 5: '))
check6 = float(input('Nota checkpoint 6: '))

check_menor2 = min(check4,check5,check6)

if check_menor2 == check4:
    soma_check2 = check5 + check6
elif check_menor2 == check5:
    soma_check2 = check4 + check6
else:
    soma_check2 = check4 + check5

checkpoint2 = soma_check2 * 0.1
print(f'Nota checkpoint 1° semestre: {checkpoint2}')

sprint3 = float(input('Nota sprint 3: '))
sprint4 = float(input('Nota sprint 4: '))

soma_sprint2 = (sprint3 + sprint4)*0.1
print(f'Nota Sprints do 1° semestre: {soma_sprint2}')

global2 = float(input('Nota da Global Solution: '))
gs2 = global2*0.6
print(f'Nota do segundo Global Solution: {gs2}')

media2 = (checkpoint2 + soma_sprint2 + gs2)*0.6
print(f'Sua nota do segundo semestre foi: {media2}')

#Nota Final
media_final = (media1 + media2)
print(f'Sua média final é: {media_final}')
if media_final >= 60:
    print('VOCê PASSOU')
elif media_final >= 40:
    print('VOCÉ ESTA DE EXAME')
else:
    print('VOCÊ REPROVOU')