def calcular_eficiencia (horas_estudo, horas_treino, hora_sono):
    print("\n---Diagnostico de rendimento---")
    horas_totais = horas_estudo + horas_treino + hora_sono

    #alerta de sono 
    if hora_sono < 7:
        print("Alerta sono abaixo do recomendado para estudantes. Cuidado com a fadiga mental")
    else:
        print("Sono ideal para recuperação fisica e mental.")

    #Alerta rotina 
    if horas_totais> 18:
        print("Alerta de esgotamento : Sua rotina está sobrecarregada. Ache tempo para descansar")

    #calculo tempo de produtividade 

    tempo_util = horas_estudo + horas_treino
    porcentagem_producao = (tempo_util/24) * 100

    print(f" Seu dia foi {porcentagem_producao:.1F}% Focado em atividades produtivas (Estudo + Treino)")

    
