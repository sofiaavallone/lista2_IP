print("Começa agora o treinamento para grande final mundial de cabo de guerra!")
quant_partidas = 0
while quant_partidas%2 == 0:
    if quant_partidas != 0:
        print("Não deverá haver empates! O número de partidas deverá ser ímpar.")
    quant_partidas = int(input())
print(f"Eles batalharão em {quant_partidas} longas partidas.")

forca_arthur = int(input())
forca_joao = int(input())
resistencia_inicial = int(input())

resistencia_arthur = resistencia_inicial
resistencia_joao = resistencia_inicial
pontos_rodada_joao = 0
pontos_rodada_arthur = 0
pontos_partida_joao = 0
pontos_partida_arthur = 0

i=0
vencedor_pontos = 0
while (i <= quant_partidas) and (quant_partidas-vencedor_pontos > quant_partidas-i):
    i+=1
    print(f"Começa a {i}ª partida!")
    print(f"Placar geral: {pontos_partida_arthur} X {pontos_partida_joao}")

    while resistencia_arthur != 0 and resistencia_joao != 0:
        primo = False
        num = int(input())
        for i in range(num-1, 2):
            if num % i == 0:
                primo = True
        
        if primo == True: # João
            resistencia_joao+=1
            resistencia_joao-=1
            pontos_rodada_joao+=1
            print("O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
        elif type(num**0.5) == int: # Arthur
            resistencia_arthur+=1
            resistencia_arthur-=1
            pontos_rodada_arthur+=1
            print("O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
        else:
            if forca_arthur>forca_joao:
                resistencia_arthur+=1
                resistencia_joao-=1
                pontos_rodada_arthur+=1
                print("Arthur é o mais forte! João não consegue segurar.")
            else:
                resistencia_joao+=1
                resistencia_arthur-=1
                pontos_rodada_joao+=1
                print("João é o mais forte! Arthur não consegue segurar.")
    
    if pontos_rodada_joao>pontos_partida_arthur:
        pontos_rodada_joao+=1
        print("João usa seus talentos de mangueboy e leva essa para casa!")
    else:
        pontos_partida_arthur+=1
        print("Arthur dá orgulho para Maceió e ganha a partida!")
    
    if pontos_partida_arthur>pontos_partida_joao:
        vencedor = pontos_partida_arthur
    else:
        vencedor_pontos = pontos_partida_joao

print()
print("Agora eles estão prontos para o mundial!")
print(f"Placar final: {resistencia_arthur} X {resistencia_joao}")
if vencedor_pontos == pontos_partida_joao:
    perdedor = "Arthur"
    vencedor = "João"
elif vencedor_pontos == pontos_partida_arthur:
    perdedor = "João"
    vencedor = "Arthur"

if perdedor == "Arthur" and pontos_partida_arthur == 0:
    print(f"{perdedor} não teve chance! {vencedor} venceu todas as partidas.")
elif perdedor == "João" and pontos_partida_joao == 0:
    print(f"{perdedor} não teve chance! {vencedor} venceu todas as partidas.")
elif vencedor == "Arthur":
    print(f"O ganhador foi {vencedor} com uma diferença de {pontos_partida_arthur} partidas.")
else:
    print(f"O ganhador foi {vencedor} com uma diferença de {pontos_partida_joao} partidas.")

