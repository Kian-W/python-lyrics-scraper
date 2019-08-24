#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import os

def main():
	url = get_song_url()
	clear_console()
	get_lyrics(url)
	

def get_song_url():
	provided_artist = input('Enter artist name: ')
	provided_song = input('Enter song name: ')

	# Convert list back to string
	artist = convert_user_param_to_genius_url_param(provided_artist)
	song = convert_user_param_to_genius_url_param(provided_song)

	# Create final url
	url = 'https://genius.com/' + artist + song + 'lyrics'

	return url

def get_lyrics(url):
	print('Gathering lyrics...')

	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')

	clear_console()

	try:
		lyrics = soup.find('div', {'class' : 'lyrics'}).text
	except AttributeError:
		print('Error: song may not exist, check for typos.')
		input('Press any key to continue')
		clear_console()
		main()


	print(lyrics)

	input('Press any key to continue')
	clear_console()
	main()


def convert_user_param_to_genius_url_param(user_param):
	user_param_list = user_param.split()

	for i in range(len(user_param_list)):
		user_param_list[i] += '-'

	genius_url_param = ''.join(user_param_list)

	return genius_url_param




def clear_console():
	os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
	main()