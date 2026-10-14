#questao 10

gostam_prog = []
gostam_redes = []
print('amam codar')
for i in range(10):
    nome= input('diga seu nome: ')
    gostam_prog.append(nome)

print('amam redes de computadores')
for i in range(10):
    nome= input('diga seu nome: ')
    gostam_redes.append(nome)

ambos = []
for i in range(10):
    if gostam_prog[i] in gostam_redes:
        ambos.append(gostam_prog[i])




