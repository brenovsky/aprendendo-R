outputs = []
N = int(input())

while (N > 0):
    word = []
    M = input()

    for i in range(len(M)):
        word.append(M[i]) # separa os caracteres do string (é só para ser capaz de alterar o valor de cada letra)

    #parte 1 (andar 3)
    for i in range(len(word)):
        if(word[i].isalpha()): # se o caractere for uma letra
            novo = ord(word[i])+ 3 # anda 3 na tabela ascii
            word[i] = chr(novo)  #retorna o caractere novo

    #parte 2 (inverter)
    word.reverse() # inverte a lista

    # parte 3
    metade = len(word) // 2 # metade truncada = parte inteira da metade (divisao de inteiros)

    for i in range(metade, len(word)): # contador vai da metade até o fim da palavra
        novo = ord(word[i]) - 1 # volta 1 na tabela ascii
        word[i] = chr(novo) # converte o código para caractere e adiciona na palavra

    word = ''.join(word) # junta todos os caracteres em uma string
    outputs.append(word)

    N -= 1

for i in range(len(outputs)):
    print(outputs[i])

