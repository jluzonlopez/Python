#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import flask
import sys
import json
import time
import requests

#timpo de delay en minutos
DELAY_BIT = 5
DELAY_DIV = 1440
app=flask.Flask(__name__)

cach_bit = {}
cach_div = {}

#http://api.fixer.io/latest?base=CNY (precio en yuanes chinos de las monedas)
#https://data.btcchina.com/data/ticker?market=btccny (precio en BTC de los yuanes)

def cambbtc(coin):
	url = "https://data.btcchina.com/data/ticker?market=btccny"
	my_timeout=5
	r=requests.get(url,timeout=my_timeout)
	if r.status_code==200:
		prc = r.json()
		buyprice = prc['ticker']
		total = float(coin)*float(buyprice['buy'])
		return total


def cambyuan(precoin,typeresult):
	url = "http://api.fixer.io/latest?base=CNY"
	my_timeout=5
	r=requests.get(url,timeout=my_timeout)
	if r.status_code==200:
		resp = r.json()
		rates = resp['rates']
		total = float(precoin)*float(rates[typeresult])
		return total

def mos_bit(coin,query,val,buyprice):
	cach_bit["XBT"+coin+query] = {time.time():{"XBT"+coin:val,"XBT":query,coin:buyprice}}

def mos_div(coin,rate):
	cach_div["XBT"+coin] = {time.time():cambbtc(rate)}


#/exchange/XBTEUR (ejemplo de peticion)
#/XBTEUR?amount=5.23 (cuantos euros hacen falta para comprar 5.23 bitcoin

@app.route('/exchange/XBT<coin>')
def cambio(coin):
	query_string = flask.request.args
	#preguntas bitcoin
	if flask.request.args:
		url = "https://data.btcchina.com/data/ticker?market=btccny"
		my_timeout=5
		r=requests.get(url,timeout=my_timeout)
		if r.status_code==200:
			prc = r.json()
			keys = cach_bit.keys()	
			buyprice = prc['ticker']
			result = float(query_string['amount'])*float(buyprice['buy'])
			if not "XBT"+coin+str(query_string['amount']) in keys:
				print "Without Cache"
				if coin == "CNY":
					mos_bit(coin,query_string['amount'],result,buyprice['buy'])
				else:
					mos_bit(coin,query_string['amount'],cambyuan(result,coin),buyprice['buy'])	
			else:
				print "With Cache"
				clave = cach_bit["XBT"+coin+str(query_string['amount'])].keys()
				if (time.time()-clave[0])/60 < DELAY_BIT:
					print "Delay: "+ str((time.time()-clave[0])/60) + " min"
					print "In time"
				else:
					print "Delay: "+ str((time.time()-clave[0])/60) + " min"
					print "Not in time"
					if coin == "CNY":
						mos_bit(coin,query_string['amount'],result,buyprice['buy'])
					else:
						mos_bit(coin,query_string['amount'],cambyuan(result,coin),buyprice['buy'])

			clave = cach_bit["XBT"+coin+str(query_string['amount'])].keys()
			return json.dumps(cach_bit["XBT"+coin+str(query_string['amount'])][clave[0]])

	#preguntas divisa
	else:
		url = "http://api.fixer.io/latest?base=CNY"
		my_timeout=5
		r=requests.get(url,timeout=my_timeout)
		if r.status_code==200:
			resp = r.json()
			keys = cach_div.keys()
			if not "XBT"+coin in keys:
				print "Without Cache"
				if coin == "CNY":
					mos_div(coin,1)
				else:
					rates = resp['rates']
					mos_div(coin,rates[coin])
			else:
				print "With Cache"
				clave = cach_div["XBT"+coin].keys()
				if (time.time()-clave[0])/60 < DELAY_DIV:
					print "Delay: "+ str((time.time()-clave[0])/60) + " min"
					print "In time"
				else:
					print "Delay: "+ str((time.time()-clave[0])/60) + " min"
					print "Not in time"
					if coin == "CNY":
						mos_div(coin,1)
					else:
						rates = resp['rates']
						mos_div(coin,rates[coin])

			clave = cach_div["XBT"+coin].keys()
			return json.dumps({"XBT"+coin:cach_div["XBT"+coin][clave[0]]})
			
if __name__ == '__main__':
	app.run(debug=True)
