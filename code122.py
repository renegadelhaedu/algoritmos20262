#dicionário + lista
alunos = dict()
alunos['93485723954'] = ['henrique', 19, 'Sousa-pb','83-98347294',True]
alunos['34345234545'] = ['marcos', 22, 'Cajazeiras-pb','83-98347294',True]
alunos['12312465867'] = ['erica', 19, 'sao jose-pb','83-98347294',True]
alunos['93857345733'] = ['josefa', 19, 'sousa-pb','83-98347294',True]

for codigo, dados in alunos.items():
    if 'sousa' in dados[2].lower():
        print(f'outro sousense: {dados[0]}')