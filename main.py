import logging
from telegram.ext import *

#Archivos
import respuestas
import _gym


API_KEY = '5044549881:AAHL9I929lUDxOKb4Z8SYKgx17e3f-r3X9g'

# Set up the logging. Para poder verlo de manera mas sencilla
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
	update.message.reply_text('Hola! Me presento, soy Bob, tu pequeño bot de confianza. ¿Que tal?')

def help_command(update, context):
	update.message.reply_text('Soy un pequeño bot, con lo cual no te esperes gran cosa. Estas son las cosas con las que te puedo ayudar.')

def gym_command(update, context):
	aforo = _gym.get_usuarios_gym()
	update.message.reply_text(aforo)


def handle_messages(update, context):
	text = str(update.message.text).lower()
	respuesta = respuestas.get_respuesta(text)
	logging.info(f'User ({update.message.chat.id}) dice: {text}')

	#Bot response
	update.message.reply_text(respuesta)


def error(update, context):
	# Log errors
	logging.error(f'{update} caused error {context.error}')

if __name__ == '__main__':
	updater = Updater(API_KEY, use_context =True)
	dp = updater.dispatcher

	# Commands
	dp.add_handler(CommandHandler('start', start_command))
	dp.add_handler(CommandHandler('help', help_command))
	dp.add_handler(CommandHandler('gym', gym_command))

	# Messages
	dp.add_handler(MessageHandler(Filters.text, handle_messages))


	# Log all errors
	dp.add_error_handler(error)

	# Run the bot
	updater.start_polling(1.0)
	updater.idle()