#pip install requests
import requests


saida = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/PB/municipios')
maior = 0
nome_maior = ''

for mun in saida.json():
    if len(mun['nome']) > maior:
        maior = len(mun['nome'])
        nome_maior = mun['nome']

print(f'{nome_maior} - {maior}')
