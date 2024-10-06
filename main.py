import logging
import requests
import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from questions import (question_ready, question_device_choice, question_usage,
                       question_storage, question_resolution, 
                       question_screen_size, question_graphics, response_invalid)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

openai.api_key = "CHAVE-API-AQUI"

# Função para fazer perguntas ao ChatGPT usando a nova interface da API da OpenAI (>=1.0.0)
def ask_chatgpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Usando o modelo de chat
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": question}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        logger.error(f"Erro ao fazer pergunta ao ChatGPT: {e}")
        return "Não foi possível processar sua solicitação no momento."


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
    context.user_data['answers'] = ""

# Função para lidar com mensagens de texto
def handle_message(update: Update, context):
    user_message = update.message.text.strip().lower()
    logger.info(f"Mensagem recebida: {user_message} de {update.effective_user.first_name}")
    
    step = context.user_data.get('step', 1)

    # Etapa 1: Pergunta "Pronto para começar?"
    if step == 1:
        if user_message == '1':
            context.bot.send_message(chat_id=update.effective_chat.id, text=question_device_choice())
            context.user_data['step'] = 2
        elif user_message == '2':
            context.bot.send_message(chat_id=update.effective_chat.id, text="Tudo bem! Quando estiver pronto, me avise.")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Responda com 1 (Sim) ou 2 (Não).")
    
    # Etapa 2: Escolha entre Notebook ou Computador
    elif step == 2:
        if user_message == '1':
            context.user_data['answers'] += "Notebook\n"
            context.bot.send_message(chat_id=update.effective_chat.id, text=question_usage())
            context.user_data['step'] = 3
        elif user_message == '2':
            context.user_data['answers'] += "Computador\n"
            context.bot.send_message(chat_id=update.effective_chat.id, text=question_usage())
            context.user_data['step'] = 3
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=response_invalid())

    # Etapa 3: Uso principal
    elif step == 3:
        if user_message == 'a':
            context.user_data['answers'] += "Para Trabalhar i3 8GB RAM\n"
        elif user_message == 'b':
            context.user_data['answers'] += "Para Estudar i3 4GB RAM\n"
        elif user_message == 'c':
            context.user_data['answers'] += "Para Edição de Video e Imagem i7 16GB RAM\n"
        elif user_message == 'd':
            context.user_data['answers'] += "Para Jogos i7 16GB RAM\n"
        elif user_message == 'e':
            context.user_data['answers'] += "Para Programação i5 8GB RAM\n"
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=response_invalid())
            return

        context.bot.send_message(chat_id=update.effective_chat.id, text=question_storage())
        context.user_data['step'] = 4

    # Etapa 4: Armazenamento
    elif step == 4:
        if user_message == 'a':
            context.user_data['answers'] += "Armazenamento 256GB\n"
        elif user_message == 'b':
            context.user_data['answers'] += "Armazenamento 512GB\n"
        elif user_message == 'c':
            context.user_data['answers'] += "Armazenamento 1TB\n"
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=response_invalid())
            return

        context.bot.send_message(chat_id=update.effective_chat.id, text=question_resolution())
        context.user_data['step'] = 5

    # Etapa 5: Qualidade de resolução da tela
    elif step == 5:
        if user_message == 'a':
            context.user_data['answers'] += "Resolução Full HD 4K\n"
        elif user_message == 'b':
            context.user_data['answers'] += "Resolução moderada\n"
        elif user_message == 'c':
            context.user_data['answers'] += "Resolução padrão\n"
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=response_invalid())
            return

        context.bot.send_message(chat_id=update.effective_chat.id, text=question_screen_size())
        context.user_data['step'] = 6

    # Etapa 6: Tamanho da tela preferido
    elif step == 6:
        if user_message == 'a':
            context.user_data['answers'] += "Tela Menos de 14 polegadas\n"
        elif user_message == 'b':
            context.user_data['answers'] += "Tela 14 a 15.6 polegadas\n"
        elif user_message == 'c':
            context.user_data['answers'] += "Tela maior que 17 polegadas\n"
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=response_invalid())
            return

        context.bot.send_message(chat_id=update.effective_chat.id, text=question_graphics())
        context.user_data['step'] = 7

    # Etapa 7: Necessidade de placa de vídeo dedicada
    elif step == 7:
        if user_message == 'a':
            context.user_data['answers'] += "Placa de vídeo Dedicada\n"
        elif user_message == 'b':
            context.user_data['answers'] += "Placa de vídeo Integrada\n"
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=response_invalid())
            return

        # Exibir as respostas armazenadas
        final_message = "Suas respostas:\n" + context.user_data['answers']
        context.bot.send_message(chat_id=update.effective_chat.id, text=final_message)

        # Perguntar ao ChatGPT por 5 notebooks com base nas especificações
        query = f"Procure 5 nomes de dispositivos que se adequem às especificações que eu preciso e não me responda nada além do nome dos dispositivos. Pesquise apenas nas seguintes lojas virtuais brasileiras: Carrefour, Extra, Shoptime, Pontofrio, Casas Bahia, Submarino, Americanas, Magazine Luiza, Amazon e Mercado Livre. Especificações: {context.user_data['answers']}"
        gpt_response = ask_chatgpt(query)

        # Enviar a resposta do ChatGPT
        context.bot.send_message(chat_id=update.effective_chat.id, text=gpt_response)

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
