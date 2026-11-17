import matplotlib.pyplot as plt

def exibir_produtos(produtos):
    nomes =[]
    qtds = []
    for id, produto in produtos.items():
        nomes.append(produto[0])
        qtds.append(produto[2])

    plt.bar(nomes, qtds, color='#2b5c8f', width=0.6)
    plt.show()


