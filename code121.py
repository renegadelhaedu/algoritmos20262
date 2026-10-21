#criar
#inserir
#atualizar
#remover

disciplinas = {'poo':'luciano','compt grafica e jogos':'erlon', 'eng soft 1': 'jose neto', 'eng de requisitos':'samira'}
#disciplinas.pop('poo')

del(disciplinas['poo'])

print(disciplinas)

#atualizar
disciplinas['poo'] = 'Luciano Tavares'


#buscar
for disciplina, professor in disciplinas.items():
    print(f'{disciplina}: {professor}')









