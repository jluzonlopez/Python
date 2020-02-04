#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

nota = float(raw_input("Mete una nota: "))
modo = str(raw_input("Mete una modo: "))
def resultado(nota, modo):
	if nota <= 10.0 and nota >= 0.0:
		if "estricto" ==  modo: 
			if nota < 5.0:
				return "suspenso"
			elif nota >=5.0 and nota <=8.0:
				return "notable"
			elif nota > 8.0:
				return "sobresaliente"
		elif "laxo" == modo:
			if nota < 4.6:
				return "suspenso"
			elif nota >= 4.6 and nota <= 6:
				return "aprobado"
			elif nota >= 8.0:
				return "sobresaliente"
		elif "normal" == modo:
			if nota >= 5.0:
				return "aprobado"
			else:
				return "suspenso"

print resultado(nota,modo)

