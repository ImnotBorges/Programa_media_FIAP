#Nota Final
# fiap_final.py
import sys

if len(sys.argv) != 3:
    print("Usage: python fiap_notafinal.py <media1> <media2>")
    sys.exit(1)

media1 = float(sys.argv[1])
media2 = float(sys.argv[2])

# Nota Final
media_final = (media1 + media2)
print(f'Sua média final é: {media_final}')

if media_final >= 60:
    print('VOCÊ PASSOU')
elif media_final >= 40:
    print('VOCÊ ESTÁ DE EXAME')
else:
    print('VOCÊ REPROVOU')