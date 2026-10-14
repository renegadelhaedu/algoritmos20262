#tipos de dados
#string, float, integer, boolean

#tipos de estruturas de dados
#lista

lista_amigos = ['yan','italo','thamires','carlos']
#percorrer a lista

busca = input('digite o nome da pessoa: ')

for amigo in lista_amigos:
    if busca in amigo:
        print("seu amigo está na lista:", amigo)