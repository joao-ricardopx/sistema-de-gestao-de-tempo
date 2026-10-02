#import analisador

#import relogio2

#while True:
    #print("\n" + "="*10)
    #print ("        SISTEMA DE GESTÃO DE TEMPO - V1    ")
    #print("\n" + "="*10)
    #print(" 1. Mapear e Analisar a Rotina Diaria ")
    #print(" 2. Iniciar Ciclo Pomodoro(Cronometro de Estudos ) ")
    #print(" 0. Encerrar Sistema ")

    #opcao = input("Digite Sua opção: ")

    #if opcao == "1":
        ## estudo = float(input("Quantas horas você estudou hoje (Escola + casa ): "))
  # treino = float(input("Quantas horas você treinou/pratiou esportes hoje: "))
        #sono  = float(input("Quantas horas você dormiu na última noite: "))

        #chamar analisador 
        #analisador.calcular_eficiencia(estudo, treino, sono)
   # elif opcao == "2":
       # print("\n--- CONFIGURAÇÃO DO BLOCO DE ESTUDOS (POMODORO)")
        #tempo = int(input("deseja um bloco de quantos minutos/ Recomendação: 25 ou 45: "))

       # relogio2.iniciar_ciclo_foco(tempo)


        
        
    #elif opcao == "0":
       # print("Saindo do sistema...")
        #quit()
        
   # else:
        #print("Digite uma opção válida!\n")
        #continue

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista para salvar o histórico de ciclos na memória do servidor
historico_ciclos = []

# --- SUA FUNÇÃO ORIGINAL DO ANALISADOR (Adaptada para retornar dados) ---
def calcular_eficiencia(horas_estudo, horas_treino, hora_sono):
    horas_totais = horas_estudo + horas_treino + hora_sono
    alertas = []

    if hora_sono < 7:
        alertas.append("⚠️ Alerta sono abaixo do recomendado para estudantes. Cuidado com a fadiga mental.")
    else:
        alertas.append("✅ Sono ideal para recuperação física e mental.")

    if horas_totais > 18:
        alertas.append("🚨 Alerta de esgotamento: Sua rotina está sobrecarregada. Ache tempo para descansar.")

    tempo_util = horas_estudo + horas_treino
    porcentagem_producao = (tempo_util / 24) * 100

    return {
        "alertas": alertas,
        "porcentagem": f"{porcentagem_producao:.1f}%"
    }

# --- ROTAS DO SERVIDOR FLASK ---

# Alterado para '/dashboard' para forçar o navegador a ler o HTML novo
@app.route('/dashboard')
def index():
    return render_template('index.html')

# Rota que processa os cálculos do seu Analisador
@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.get_json()
    try:
        estudo = float(dados.get('estudo', 0))
        treino = float(dados.get('treino', 0))
        sono = float(dados.get('sono', 0))
        
        resultado = calcular_eficiencia(estudo, treino, sono)
        return jsonify(resultado)
    except ValueError:
        return jsonify({"erro": "Por favor, digite números válidos."}), 400

# Rota que recebe os eventos do seu Relógio Pomodoro
@app.route('/registrar_ciclo', methods=['POST'])
def registrar_ciclo():
    dados = request.get_json()
    evento = dados.get('evento')
    
    if evento == 'sucesso':
        mensagem = "✨ Fim do bloco de estudos. Parabéns pelo foco!"
    else:
        mensagem = "⚠️ Ciclo interrompido manualmente. Volte assim que possível."
        
    historico_ciclos.append(mensagem)
    return jsonify({"status": "sucesso", "historico": historico_ciclos})

if __name__ == '__main__':
    app.run(debug=True)