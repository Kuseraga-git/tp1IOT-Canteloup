#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import requests

def user_input() :
	user = input("Entrez la crypto-monnaie dont vous voulez connaitre le prix")

def disp_price(user):
	req = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+monnaie+'&tsyms=BTC,USD,EUR').json()
	prix = str(req["EUR"])
	print(": " + prix + " Euros.")
	user_input()

def main():
	try:
		req = requests.get('https://www.cryptocompare.com/api/data/coinlist/').json()["Data"]
		for value in req.values():
			print(value['FullName'])
		user_input()	
	except Exception as err:
		print(err)
		print("Il y a eu une erreur")

main()