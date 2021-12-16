from bs4 import BeautifulSoup
import requests
import re

from datetime import datetime


def get_usuarios_gym():
	url = 'https://carnesweb.um.es/pls/suma/pls_pci.get_info_gimnasio'
	html_text = requests.get(url).text


	soup = BeautifulSoup(html_text, "lxml")
	cadena = soup.find('body').text

	n_personas = re.search("Actualmente hay \d+ usuarios", cadena).group()

	now = datetime.now()

	print(f'{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}:{now.second}')
	print(f'{n_personas} en la sala de musculación.')

	aforo_gym = n_personas + ' en la sala de musculacion.'
	return aforo_gym