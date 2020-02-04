#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import datetime
import argparse
import time
import sys
import pytz
import types

usage = "%prog [opciones]"
parser = argparse.ArgumentParser(description = "Short sample app")
parser.add_argument("-t", "--timezone",action ="store", dest = "timezone",help = "-t [lugar] zona en la que quieres que te muestre la hora")

args = parser.parse_args()

fichero = open("fechas.txt","r")

def esta_bien(fecha):
	if len(fecha) > 2:
		anno = fecha[1].split("-")
		if len(anno[0]) == 4 and len(anno[1]) == 2 and len(anno[2]) == 2:
			hour = fecha[2]
			hour = hour[:-1]
			hour = hour.split(":")
			if len(hour[0]) == 2 and len(hour[1]) == 2 and len(hour[2]) == 2:
				if not(fecha[3] == "Madrid" or fecha[3] == "New_York" or fecha[3] == "Londres" or fecha[3] == "Tokio" or fecha[3] == "Moscu" or fecha[3] == "UTC"):
					print "aqui"
					sys.stderr.write("Fecha no permitida" + "\n")
					raise SystemExit
			else:
				sys.stderr.write("Fecha no permitida" + "\n")
				raise SystemExit
		else:
			sys.stderr.write("Fecha no permitida" + "\n")
			raise SystemExit
	else:
		try:
			fecha = [int(i) for i in fecha]
		except ValueError:
			sys.stderr.write("Fecha no permitida" + "\n")
			raise SystemExit
		if not (type(fecha[0]) == types.IntType and type(fecha[1]) == types.IntType):
			sys.stderr.write("Fecha no permitida" + "\n")
			raise SystemExit

for linea in fichero:
	fecha = linea[:-1].split(" ")
	esta_bien(fecha)
	if len(fecha) > 2:
		anno = fecha[1].split("-")
		hour = fecha[2].split(":")
		seg = hour[2]
		seg = seg[:-1]
		if fecha[3] == "Madrid":
			zona_horaria = pytz.timezone("Europe/Madrid")
		if fecha[3] == "New_York":
			zona_horaria = pytz.timezone("America/New_York")
		if fecha[3] == "Londres":
			zona_horaria = pytz.timezone("Europe/London")
		if fecha[3] == "Tokio":
			zona_horaria = pytz.timezone("Asia/Tokyo")
		if fecha[3] == "Moscu":
			zona_horaria = pytz.timezone("Europe/Moscow")
		if fecha[3] == "UTC":
			zona_horaria = pytz.utc
		try:
			fech = datetime.datetime(int(anno[0]),int(anno[1]),int(anno[2]),int(hour[0]),int(hour[1]),int(seg),tzinfo=zona_horaria)
			fech = fech.astimezone(pytz.utc)
			tsfech = time.mktime(fech.timetuple())
		except ValueError:
			sys.stderr.write("Fecha no permitida" + "\n")
			raise SystemExit
	else:
		#fech = datetime.datetime.fromtimestamp(float(fecha[1]))
		#fech = pytz.utc.localize(fech)
		tsfech = float(fecha[1])
	

	if args.timezone:
		fech=datetime.datetime.fromtimestamp(tsfech)
		fech = pytz.utc.localize(fech)
		if args.timezone == "madrid":
			dt=fech.astimezone(pytz.timezone("Europe/Madrid"))
		if args.timezone == "new_york":
			dt=fech.astimezone(pytz.timezone("America/New_York"))
		if args.timezone == "londres":
			dt=fech.astimezone(pytz.timezone("Europe/London"))
		if args.timezone == "tokio":
			dt=fech.astimezone(pytz.timezone("Asia/Tokyo"))
		if args.timezone == "moscu":
			dt=fech.astimezone(pytz.timezone("Europe/Moscow"))
		if args.timezone == "utc":
			dt=fech.astimezone(pytz.utc)
		if args.timezone == "epoch":
			dt=time.mktime(fech.timetuple())
	else:
		dt=fech.astimezone(pytz.utc)
	print fecha[0],dt
fichero.close()
