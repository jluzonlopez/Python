#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

caja01 = []
caja02 = []
print "Caja 1"
print caja01
print "Caja 2"
print caja02

caja01.append("Julian")
caja01.append("Pepe")
caja01.append("Juan")
caja01.append("Laura")
caja01.append("Jaime")
caja01.append("Ernesto")
caja02.append("Federico")
caja02.append("Paco")
caja02.append("Carmen")
caja02.append("Lucia")
caja02.append("Lirico")
caja02.append("Evaristo")
print "Caja 1"
print caja01
print "Caja 2"
print caja02

caja01.remove("Julian")
caja02.remove("Paco")
print "Caja 1"
print caja01
print "Caja 2"
print caja02

caja02.insert(0,"Sergio")
caja03 = []
caja03.append(caja02[1])
caja03.append(caja02[3])
caja03.append(caja02[5])


print "Caja 1"
print caja01
print "Caja 2"
print caja02
print "Caja 3"
print caja03

caja01.reverse()
print caja01


if "Ernesto" in caja01:
	caja01.remove("Ernesto")
	caja01.insert(0,"Ernesto")
	

print "Caja 1"
print caja01

linea_de_cajas = (caja01,caja02,caja03)

print "Caja 1"
print caja01
print "Caja 2"
print caja02
print "Caja 3"
print caja03
print "Linea de cajas"
print linea_de_cajas

x = len(linea_de_cajas)
for x in linea_de_cajas:
	print x

