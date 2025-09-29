nome1 = input()
nome2 = input()
nome3 = input()

cont_achados = 0

for i in range(2):
    resposta = "Achou uma pessoa!"
    while resposta != "Fim da busca nesse prédio.": #CFCH
        resposta = input()
        if resposta == "Achou uma pessoa!":
            cont_achados