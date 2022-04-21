def escrever_arquivo(texto):
    arquivo = open('padaria.txt' , 'w')
    arquivo.write(texto)
    arquivo.close()
def arquivo_atualizar(texto):
    arquivo = open('padaria.txt' ,'a')
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo( nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    arquivo.close()
def separar_arquivo():
    arquivo = open('padaria.txt' ,'r')
    padaria_arquivo = arquivo.read()
    padaria_arquivo = padaria_arquivo.split("\n")
    print(padaria_arquivo)
    lista = []
    for x in padaria_arquivo:
        lista_quantidade = x.split(',')
        produto = lista_quantidade[0]
        lista_quantidade.pop(0)
        print(lista_quantidade)
        for y in lista:
            if y <2:
                print('há falta de produtos no estoque')
    return lista

escrever_arquivo('pao, 4')
arquivo_atualizar('leite, 3')
separar_arquivo()