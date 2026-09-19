import time 
import sys

def iniciar_ciclo_foco(minutos_em_foco):
    print("\n--- CRONOMETRO DE ESTUDOS---")
    print(f" Foco totsl iniciado por {minutos_em_foco} minuto. Mantenha o foco ")
    segundos_totais = minutos_em_foco 

    try:
        for segundo in range (segundos_totais, 0, -1):
            sys.stdout.write(f"tempo restante simulado : {segundos_totais:02d} segundos...")
            sys.stdout.flush()
            time.sleep(1)

        print("\n\n Fim do bloco de estudos parabens pelo foco ")
    except KeyboardInterrupt:
        print("ciclo interrompido manualmente. Volte assim que possivel") 