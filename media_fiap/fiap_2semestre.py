import sys

if len(sys.argv) != 2:
    print("Usage: python fiap_semester2.py <media1>")
    sys.exit(1)

media1 = float(sys.argv[1])

# 2° Semestre
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
print(f'Nota checkpoint 2° semestre: {checkpoint2}')

sprint3 = float(input('Nota sprint 3: '))
sprint4 = float(input('Nota sprint 4: '))

soma_sprint2 = (sprint3 + sprint4)*0.1
print(f'Nota Sprints do 2° semestre: {soma_sprint2}')

global2 = float(input('Nota da Global Solution: '))
gs2 = global2*0.6
print(f'Nota do segundo Global Solution: {gs2}')

media2 = (checkpoint2 + soma_sprint2 + gs2)*0.6
print(f'Sua nota do segundo semestre foi: {media2}')

import subprocess
subprocess.run(['python', 'fiap_notafinal.py', str(media1), str(media2)])