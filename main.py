import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from questions import question_ready, question_device_choice, response_notebook, response_computer, response_invalid

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update: Update, context):
    logger.info(f"Comando /start recebido de {update.effective_user.first_name}")

    # Mensagem de boas-vindas
    welcome_message = f"Olá {update.effective_user.first_name}! Bem-vindo ao bot que vai te ajudar a escolher o notebook ou computador ideal."
    
    # Enviando a mensagem de boas-vindas
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=welcome_message
    )
    
    # Enviando a primeira pergunta
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=question_ready()
    )
    
    context.user_data['step'] = 1

# Função para lidar com mensagens de texto
def handle_message(update: Update, context):
    user_message = update.message.text.strip()
    logger.info(f"Mensagem recebida: {user_message} de {update.effective_user.first_name}")
    
    step = context.user_data.get('step', 1)

    # Pergunta 01: Pronto para começar?
    if step == 1:
        if user_message == '1':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=question_device_choice()
            )
            context.user_data['step'] = 2
        elif user_message == '2':
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Tudo bem! Quando estiver pronto, me avise."
            )
        else:
            # Resposta inválida
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Desculpe, não entendi sua resposta. Responda com 1 (Sim) ou 2 (Não)."
            )
    
    # Pergunta 02: Notebook ou Computador?
    elif step == 2:
        if user_message == '1':
            # Salvar escolha"notebook"
            context.user_data['device_choice'] = "notebook"
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=response_notebook()
            )
            context.user_data['step'] = 3
        elif user_message == '2':
            # Salvar escolha "computador"
            context.user_data['device_choice'] = "computador"
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=response_computer()
            )
            context.user_data['step'] = 3
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=response_invalid()
            )
    
    # Pergunta 03: Qual será o principal uso do dispositivo?
    elif step == 3:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Qual será o principal uso do dispositivo?\n"
                 "a) Trabalho (Escritório, Home Office)\n"
                 "b) Estudos\n"
                 "c) Edição de vídeo/imagem\n"
                 "d) Jogos\n"
                 "e) Programação"
        )
        context.user_data['step'] = 4

    # Pergunta 04: Quanto armazenamento você precisa?
    elif step == 4:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Quanto armazenamento você precisa?\n"
                 "a) Menos de 256GB (usuários leves)\n"
                 "b) 256GB - 512GB (usuários moderados)\n"
                 "c) 1TB ou mais (usuários que armazenam grandes arquivos)"
        )
        context.user_data['step'] = 5

    # Pergunta 05: Importância da duração da bateria
    elif step == 5:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Qual a importância da duração da bateria para você? (se aplicável a notebooks)\n"
                 "a) Muito importante (uso frequente fora de casa/escritório)\n"
                 "b) Moderadamente importante\n"
                 "c) Pouco importante (uso principalmente conectado à tomada)"
        )
        context.user_data['step'] = 6

    # Pergunta 06: Qualidade de resolução da tela
    elif step == 6:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Você precisa de uma tela com alta qualidade de resolução (Full HD, 4K)?\n"
                 "a) Sim, para edição de fotos/vídeos ou jogos\n"
                 "b) Sim, mas apenas para assistir a vídeos e trabalhar\n"
                 "c) Não, uma resolução padrão é suficiente"
        )
        context.user_data['step'] = 7

    # Pergunta 07: Tamanho da tela preferido
    elif step == 7:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Qual o tamanho da tela que você prefere?\n"
                 "a) Menos de 14” (portabilidade)\n"
                 "b) 14” - 15.6” (equilíbrio)\n"
                 "c) 17” ou mais (para maior visibilidade)"
        )
        context.user_data['step'] = 8

    # Pergunta 08: Necessidade de placa de vídeo dedicada
    elif step == 8:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Você vai precisar de placa de vídeo dedicada?\n"
                 "a) Sim, para jogos ou edição de vídeo\n"
                 "b) Não, uma placa gráfica integrada é suficiente"
        )
        context.user_data['step'] = 9

def main():
    try:
        TOKEN = '7506375817:AAGmJgv9h0xm0t5H5AE9nTPqe_q6voz6OFY'
        
        updater = Updater(TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))

        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

        logger.info("Bot iniciado, ouvindo mensagens...")
        updater.start_polling()
        updater.idle()

    except Exception as e:
        logger.error(f"Erro na execução do bot: {e}")

if __name__ == '__main__':
    main()
