#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import requests
import argparse
import json
import sys


def msgs(userid,username):
	url = "http://jsonplaceholder.typicode.com/posts"
	payload={}
	payload["market"] = "all"
	my_timeout = 5
	r=requests.get(url,params=payload, timeout=my_timeout)
	if r.status_code==200:
		posts = r.json()
		for x in posts:
			if x['userId'] == userid:
				sys.stdout.write("De: " + username + "\n" + x['title'] + "\n") 
				sys.stdout.write("------------------------------------------" + "\n")	
				sys.stdout.write(x['body'] + "\n\n")
	else:
		sys.stderr.write("Error" + "\n")


usage = "%prog [opciones]"
parser = argparse.ArgumentParser(description = "Short sample app")
parser.add_argument("-u", "--user",action ="store", dest = "user",help = "-u [user] para mostrar los mensajes un usuario en concreto")

args = parser.parse_args()

url = "http://jsonplaceholder.typicode.com/users"
payload={}
payload["market"]="all"
my_timeout=5

exist = False
r=requests.get(url,params=payload, timeout=my_timeout)
if r.status_code==200:
	users = r.json()
	if args.user:
		for x in users:
			if x['username'] == args.user.capitalize():
				msgs(x['id'],x['username'])
				exist = True
	else:
		for x in users:
			msgs(x['id'],x['username'])
else:
	sys.stderr.write("Error " + str(r.status_code) + "\n")

if not exist:
	sys.stderr.write("Usuario no existe"+ "\n")

