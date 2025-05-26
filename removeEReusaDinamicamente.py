import sys

def removeGuardandoHead(arquivo, chave):
    with open(arquivo, 'r', encoding='utf-8') as f:
        animes = f.readlines()
    head = animes[0]
    for i in range(len(animes)):
        if i == chave:
            novaLinha = '*|' + head + animes[i][len('*|'+head):]
            animes[i] = novaLinha
            novaHead = str(i)

    with open('outputRemovido.txt', 'w', encoding='utf-8') as f:
        f.write(novaHead)
        for i in range(1, len(animes)):
            f.write(animes[i])
                


if __name__ == '__main__':
    removeGuardandoHead('outputAnimesComHead.txt', 7)

