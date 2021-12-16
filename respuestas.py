import re

# De ayuda
def procesar_mensajes(mensaje, array_respuestas, respuesta):

	# Splits the mensaje and the puntuation into an array (list)
	list_message = re.findall(r"[\w']+|[.,!?;]", mensaje.lower())

	#Scores the amount of words in the mensaje
	score = 0
	for word in list_message:
		if word in array_respuestas:
			score = score + 1



	#Returns the response and the score of the responses
	print(score, respuesta)
	return [score, respuesta]

# La buena
def get_respuesta(message):
	# Add custom responses here
	response_list = [
		procesar_mensajes(message.lower(), ['hola', 'hey', 'hi', 'ey'], 'Hola!, ¿Que tal?'),
		procesar_mensajes(message.lower(), ['adios', 'bye', 'marchar', 'irme', 'ir'], 'Adios! Espero verte pronto'),
		procesar_mensajes(message.lower(), ['estas', 'encuentras', 'cuentas'], 'Bastante bien por aqui, y tu?'),
		procesar_mensajes(message.lower(), ['nombre', 'llamas'], 'Me llamo Bob, soy tu asistente inteligente'),
		procesar_mensajes(message.lower(), ['apellido', 'segundo'], 'No tengo apellido. Como mucho me puedes llamar Bob Esponja, pero no te pases'),
		procesar_mensajes(message.lower(), ['help', 'ayuda', 'ayudar', 'entiendo'], '¿En que te puedo ayudar?'),
		procesar_mensajes(message.lower(), ['gym', 'gimnasio', 'gente', 'hay'], 'No se si lo sabes pero con el comando /gym puedes ver cuanta gente hay en el gimnasio de la UMU')
		# Add more responses here
	]


	# Checks all of the response scores and returns the best matching response
	# Tuplas [Score, respuesta] --> [2, "Hola buenos dias"], [0, "Adios"]
	response_scores = []
	for response in response_list:
		response_scores.append(response[0])

	respuesta_ganadora = max(response_scores)
	matching_response = response_list[response_scores.index(respuesta_ganadora)]

	# Return the matching response to the user
	if respuesta_ganadora == 0:
		bot_response = 'Lo siento pero no te he entendido. Soy todavia pequeño y me estan entrenando, ten paciencia conmigo. ¿Puedes expresarlo de otra forma?. Si crees que esto se trata de un error, por favor hazmelo saber con el comando /error'
	else:
		bot_response = matching_response[1]

	print ('Respuesta de Bob: ', bot_response)
	return bot_response


# Test
