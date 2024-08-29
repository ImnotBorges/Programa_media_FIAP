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

import subprocess
subprocess.run(['python', 'fiap_2semestre.py', str(media1)])