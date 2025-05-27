import sys

def removeGuardandoHead(arquivo, chave):
    with open(arquivo, 'r', encoding='utf-8') as f:
        animes = f.readlines()
    head = animes[0]
    for i in range(len(animes)):
        if i == chave:
            novaLinha = head
            animes[i] = novaLinha
            novaHead = str(i)

    with open('outputRemovidoComHead.txt', 'w', encoding='utf-8') as f:
        f.write(novaHead+'\n')
        for i in range(1, len(animes)):
            f.write(animes[i])
                

def inserirRegistroComReuso (arquivo, registro):
    with open(arquivo, 'r', encoding='utf-8') as f:
        animes = f.readlines()
    head = animes[0]
    if int(head) == -1:
        for i in range(1, len(animes)):
            f.write(animes[i])
        f.write(registro)

    novaHead = animes[int(head)]
    animes[int(head)] = registro
    head = novaHead
    with open('outputRemovidoComHead.txt', 'w', encoding='utf-8') as f:
        f.write(novaHead+'\n')
        for i in range(1, len(animes)):
            f.write(animes[i])




if __name__ == '__main__':
    removeGuardandoHead('outputAnimesComHead.txt', 7)
    

