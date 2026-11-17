def escrever_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto + '\n')
    print(f"Texto gravado com sucesso em '{nome_arquivo}'.")

def adicionar_linha(nome_arquivo, texto):
    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(texto + '\n')

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(f"\n--- Conteúdo de {nome_arquivo} ---")
        print(conteudo.strip())


arquivo_txt = "diario.txt"
