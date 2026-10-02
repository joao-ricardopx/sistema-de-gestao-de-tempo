import time 
import sys

def iniciar_ciclo_foco(minutos_em_foco):
    print("\n--- CRONOMETRO DE ESTUDOS---")
    print(f" Foco totsl iniciado por {minutos_em_foco} minuto. Mantenha o foco ")
    segundos_totais = int (minutos_em_foco) 

    try:
        while segundos_totais:
            print(f"tempo restante simulado : {segundos_totais:02d} segundos...", end="\r", flush=True)
            time.sleep(1)
            segundos_totais += -1
            

        print("\n\n Fim do bloco de estudos parabens pelo foco ")
    except KeyboardInterrupt:
        print("ciclo interrompido manualmente. Volte assim que possivel") 