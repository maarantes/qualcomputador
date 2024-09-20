# Pergunta 01: Pronto para começar?
def question_ready():
    return "Você está pronto para começar?\nResponda com 1 (Sim) ou 2 (Não)."

# Pergunta 02: Preferência entre notebook ou computador
def question_device_choice():
    return ("Você prefere ou possui a necessidade de ter um dispositivo que possa ser levado para qualquer lugar ou um dispositivo fixo, porém mais eficiente?\nOpções:\n1 (Notebook)\n2 (Computador)")

# Pergunta 02 > Notebook:
def response_notebook():
    return "Você escolheu um notebook! Ótimo para quem precisa de mobilidade."

# Pergunta 02 > Computador
def response_computer():
    return "Você escolheu um computador! Perfeito para quem precisa de mais desempenho."

# Resposta Inválida
def response_invalid():
    return "Desculpe, eu não entendi sua resposta. Por favor, responda com 1 (Notebook) ou 2 (Computador)."
