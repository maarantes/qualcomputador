# Pergunta 01: Pronto para começar?
def question_ready():
    return "Você está pronto para começar?\nResponda com 1 (Sim) ou 2 (Não)."

# Pergunta 02: Preferência entre notebook ou computador
def question_device_choice():
    return ("Você prefere ou possui a necessidade de ter um dispositivo que possa ser levado para qualquer lugar ou um dispositivo fixo, porém mais eficiente?\n"
            "Opções:\n1 (Notebook)\n2 (Computador)")

# Pergunta 02 > Notebook:
def response_notebook():
    return ("Você escolheu um notebook! Ótimo para quem precisa de mobilidade.\n"
            "Agora, me diga: Qual será o principal uso do dispositivo?\n"
            "a) Trabalho (Escritório, Home Office)\n"
            "b) Estudos\n"
            "c) Edição de vídeo/imagem\n"
            "d) Jogos\n"
            "e) Programação")

# Pergunta 02 > Computador
def response_computer():
    return ("Você escolheu um computador! Perfeito para quem precisa de mais desempenho.\n"
            "Agora, me diga: Qual será o principal uso do dispositivo?\n"
            "a) Trabalho (Escritório, Home Office)\n"
            "b) Estudos\n"
            "c) Edição de vídeo/imagem\n"
            "d) Jogos\n"
            "e) Programação")

# Pergunta de armazenamento
def question_storage():
    return ("Quanto armazenamento você precisa?\n"
            "a) Menos de 256GB (usuários leves)\n"
            "b) 256GB - 512GB (usuários moderados)\n"
            "c) 1TB ou mais (usuários que armazenam grandes arquivos)")

# Pergunta sobre duração da bateria (para notebooks)
def question_battery():
    return ("Qual a importância da duração da bateria para você? (se aplicável a notebooks)\n"
            "a) Muito importante (uso frequente fora de casa/escritório)\n"
            "b) Moderadamente importante\n"
            "c) Pouco importante (uso principalmente conectado à tomada)")

# Pergunta sobre qualidade de resolução da tela
def question_resolution():
    return ("Você precisa de uma tela com alta qualidade de resolução (Full HD, 4K)?\n"
            "a) Sim, para edição de fotos/vídeos ou jogos\n"
            "b) Sim, mas apenas para assistir a vídeos e trabalhar\n"
            "c) Não, uma resolução padrão é suficiente")

# Pergunta sobre tamanho da tela
def question_screen_size():
    return ("Qual o tamanho da tela que você prefere?\n"
            "a) Menos de 14” (portabilidade)\n"
            "b) 14” - 15.6” (equilíbrio)\n"
            "c) 17” ou mais (para maior visibilidade)")

# Pergunta sobre placa de vídeo dedicada
def question_graphics():
    return ("Você vai precisar de placa de vídeo dedicada?\n"
            "a) Sim, para jogos ou edição de vídeo\n"
            "b) Não, uma placa gráfica integrada é suficiente")

# Resposta Inválida
def response_invalid():
    return "Desculpe, eu não entendi sua resposta. Por favor, tente novamente."
