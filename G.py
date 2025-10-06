print("Começa agora o treinamento para grande final mundial de cabo de guerra!")
quant_partidas = 0
while quant_partidas%2 == 0:
    print("Não deverá haver empates! O número de partidas deverá ser ímpar.")
    quant_partidas = int(input())
print(f"Eles batalharão em {quant_partidas} longas partidas.")

forca_arthur = int(input())
forca_joao = int(input())
resistencia_inicial = int(input())

pontos_arthur = 0
pontos_joao = 0

for i in range(1, quant_partidas):
    print(f"Começa a {i}ª partida!")
    print(f"Placar geral: {pontos_arthur} X {pontos_joao}")

    #if type(i ** 2) == int:
