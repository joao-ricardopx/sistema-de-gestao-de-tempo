import analisador

import relogio2

while True:
    print("\n" + "="*10)
    print ("        SISTEMA DE GESTÃO DE TEMPO - V1    ")
    print("\n" + "="*10)
    print(" 1. Mapear e Analisar a Rotina Diaria ")
    print(" 2. Iniciar Ciclo Pomodoro(Cronometro de Estudos ) ")
    print(" 0. Encerrar Sistema ")

    opcao = input("Digite Sua opção: ")

    if opcao == "1":
        print("\n --- Entrada de dados : da rotina ---")
        estudo = float(input("Quantas horas você estudou hoje (Escola + casa ): "))
        treino = float(input("Quantas horas você treinou/pratiou esportes hoje: "))
        sono  = float(input("Quantas horas você dormiu na última noite: "))

        #chamar analisador 
        analisador.calcular_eficiencia(estudo, treino, sono)
    elif opcao == "2":
        print("\n--- CONFIGURAÇÃO DO BLOCO DE ESTUDOS (POMODORO)")
        tempo = int(input("deseja um bloco de quantos minutos/ Recomendação: 25 ou 45: "))

        relogio2.iniciar_ciclo_foco(tempo)


        
        
    elif opcao == "0":
        print("Saindo do sistema...")
        quit()
        
    else:
        print("Digite uma opção válida!\n")
        continue



