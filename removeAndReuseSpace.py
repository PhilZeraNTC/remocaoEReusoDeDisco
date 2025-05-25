def removeRegistro(arquivo, chave):
    for i in range(len(animes)):
        if i == chave:
            novaLinha = '*|' + arquivo[i][2:]
            arquivo[i] = novaLinha
    return arquivo
            
    
if __name__ == '__main__':
    with open('outputAnimes.txt', 'r', encoding='utf-8') as f:
        animes = f.readlines()
        
    animes = removeRegistro(animes, 5)
    
    with open('outputRemovido.txt', 'w', encoding='utf-8') as f:
        for registro in animes:
            print(registro)
            f.write(str(registro))
    
    
        
