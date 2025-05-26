import sys

def removeRegistro(arquivo, chave):
    with open(arquivo, 'r', encoding='utf-8') as f:
        animes = f.readlines()

    for i in range(len(animes)):
        if i == chave:
            novaLinha = '*|' + animes[i][2:]
            animes[i] = novaLinha

    with open('outputRemovido.txt', 'w', encoding='utf-8') as f:
        for registro in animes:
            f.write(registro)
    
            
def compactacaoDados(entrada, saida):
    indicesVazios = []
    with open(entrada, 'r') as base:
        with open(saida, 'w') as saida:
            for i,b in enumerate(base):
                if '*|' not in b:
                    dadoCopido = b
                    saida.write(dadoCopido)
                else:
                    indicesVazios.append(i)
    

if __name__ == '__main__':
    removeRegistro('outputAnimes.txt', 8)

    compactacaoDados('outputRemovido.txt', 'outputCompactado.txt')
    
        
