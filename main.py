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

	list_artist = provided_artist.split()
	list_song = provided_song.split()

	list_artist = convert_user_param_to_genius_url_param(list_artist)
	list_song = convert_user_param_to_genius_url_param(list_song)


	# Convert list back to string
	artist = ''.join(list_artist)
	song = ''.join(list_song)

	# Create final url
	url = 'https://genius.com/' + artist + song + 'lyrics'

	return url

def get_lyrics(url):
	source = requests.get(url).text
	soup = BeautifulSoup(source, 'lxml')

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


def convert_user_param_to_genius_url_param(list_to_convert):
	for i in range(len(list_to_convert)):
		list_to_convert[i] += '-'

	return list_to_convert




def clear_console():
	os.system('cls' if os.name=='nt' else 'clear')


if __name__ == '__main__':
	main()