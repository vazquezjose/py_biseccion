'''
*	Obtención de raíces usando el método de bisección
*	Autor: José Isaías Vázquez Macías
'''

import math

'''
*	Descripción:
*	Función para validar que una cadena pueda representar un número real
*	
*	Parámetros:
*	- "string" : la cadena a analizar
*	
*	Valor de retorno:
*	Booleano : validez de la cadena como número real
'''
def isFloat(string):
	validChars = ".-0123456789" # caracteres válidos en un número real
	slashFound = False	# variable para registrar si se halló algún guión en la cadena
	dotFound = False	# variable para registrar si se halló algún punto en la cadena
	
	if len(string) > 0: # si el tamaño de la cadena es mayor a 0...
		if '-' in string and string[0] != '-':	# si la cadena contiene un guión, pero dicho guión no se ubica como el primer caracter...
			return False	# la cadena no es un número real válido
		else:	# sino...
			for c in string:	# iterando en cada caracter de la cadena
				if c not in validChars: # si el caracter iterado no se encuentra en los caracteres validos...
					return False	# la cadena no es un número real válido
				
				if c == '-':	# si el caracter iterado es un guión...
					if not slashFound:	# si aún no se ha hallado algún guión...
						slashFound = True	# registrar que ya hay un guión en la cadena
					else:	# sino...
						return False	# la cadena no es un número real válido
				if c == '.':	# si el caracter iterado es un punto...
					if not dotFound:	# si aún no hay registro de algún punto...
						dotFound = True # registrar que ya hay un punto en la cadena
					else:	# sino...
						return False	# la cadena no es un número real valido
	else:	# sino...
		return False	# la cadena no es un número real válido
	return True # si a pesar de las trabas llega a este punto, es un número real válido

'''
*	Descripción:
*	Función para validar que una cadena pueda representar un número entero
*	
*	Parámetros:
*	- "string" : la cadena a analizar
*	- "forcePositive" : especifica si la cadena analizada debe ser, a parte de entero, un número positivo
*	
*	Valor de retorno:
*	Booleano : validez de la cadena como número entero (y positivo si requerido)
'''
def isInt(string, forcePositive):
	validChars = "-0123456789"	# caracteres válidos en un número entero
	slashFound = False	# variable para registrar si se halló algún guión en la cadena
	if len(string) > 0: # si el tamaño de la cadena es mayor a 0...
		for c in string:	# iterando en cada caracter de la cadena
			if c not in validChars: # si el caracter iterado no se encuentra en los caracteres validos...
				return False	# la cadena no es un número real válido
			
			if c == '-':	# si el caracter iterado es un guión...
				if not forcePositive:	# si el entero no debe ser un positivo forzosamente...
					if not slashFound and len(string) >= 2: # si aún no se ha hallado un guión y el tamaño de la cadena es mayor o igual a 2...
						slashFound = True	# registrar que ya hay un guión en la cadena
					else:	# sino...
						return False	# la cadena no es un número entero válido
				else:	# sino...
					return False	# la cadena no es un número entero positivo válido
	else:	# sino...
		return False	# la cadena no es un número entero válido
	return True # si a pesar de las trabas llega a este punto, es un número entero válido


def evaluateFunction(coefficients, x):
	total = 0
	
	for i in range(0, len(coefficients)):
		coefficient = coefficients[i]
		total = total + coefficient * math.pow(x, i)
	return total

def calculateApproximateError(newValue, previousValue):
	if previousValue != 0:
		return abs((newValue - previousValue) / previousValue) * 100
	else:
		return 100


'''
*	Descripción:
*	Función principal. Pide el ingreso de los datos y manda llamar a todas las demás.
*	
*	Parámetros:
*	No tiene.
*	
*	Valor de retorno:
*	No tiene.
'''
def main():
	infoInput = None	# variable temporal que almacena la información ingresada por el usuario
	
	keepAskingDegree = True	# variable temporal usada para saber si la información ingresada fue correcta
	degree = 0	# almacena el grado del polinomio. Es reemplazado por la info. ingresada
	
	while keepAskingDegree:	# ciclo controlador del ingreso del grado
		infoInput = input("Ingrese el grado del polinomio (numero entero mayor a 0): ")
		
		if isInt(infoInput, True):	# si la información ingresada es un entero positivo...
			degree = int(infoInput)	# asignar la información ingresada al grado
			
			if degree > 0:	# si el grado es válido (mayor a 0)...
				keepAskingDegree = False	# salir del ciclo
			else:	# sino...
				print("- El grado debe ser mayor a 0.")
		else:	# sino...
			print("- La informacion introducida no es un numero entero mayor a 0.")
			
	coefficients = list()
	
	for i in range(0, degree+1):
		keepAskingCoefficient = True
		coefficient = 0
		
		while keepAskingCoefficient:
			infoInput = input(f"Ingrese el coeficiente de x^{i}: ")
			
			if isFloat(infoInput):
				coefficient = float(infoInput)
				keepAskingCoefficient = False
			else:
				print("- La informacion introducida no es un coeficiente valido.")
		coefficients.append(coefficient)
	
	
	keepAskingDesiredError = True
	desiredError = 0
	while keepAskingDesiredError:
		infoInput = input("Ingrese el error deseado (%): ")
		
		if isFloat(infoInput):
			val = float(infoInput)
			if val >= 0 and val < 100:
				desiredError = val
				keepAskingDesiredError = False
			else:
				print("- El error deseado debe ser mayor o igual a 0 y menor que 100.")
		else:
			print("- La informacion introducida no es un error esperado valido.")
	
	interval = list()
	
	keepAskingInterval = True
	while keepAskingInterval:
		for i in range(0, 2):
			keepAskingIntervals = True
			
			while keepAskingIntervals:
				infoInput = input(f"Ingrese el {'inicio' if i == 0 else 'fin'} del intervalo: ")
				
				if isFloat(infoInput):
					val = float(infoInput)
					if val not in interval:
						interval.append(val)
						keepAskingIntervals = False
					else:
						print("- Los elementos del intervalo son iguales. Intente de nuevo.")
				else:
					print("- La informacion introducida no es un intervalo valido.")
		interval.sort()
		
		if evaluateFunction(coefficients, interval[0]) * evaluateFunction(coefficients, interval[1]) < 0:
			keepAskingInterval = False
		else:
			print("- El producto del intervalo no es menor a 0. Ajuste el intervalo para que si lo sea.")
			interval.clear()
	
	keepIterating = True
	Xr = 0
	root = 0
	lastValue = None
	while keepIterating:
		Xr = (interval[0] + interval[1]) / 2
		
		if lastValue is None:
			lastValue = Xr
			approximateError = " - "
		else:
			approximateError = calculateApproximateError(Xr, lastValue)

			if approximateError < desiredError:
				break
		
		print(f"X1 = {interval[0]} Xu = {interval[1]} Xr = {Xr} Ea = {approximateError}%")
		
		lastValue = Xr
		if evaluateFunction(coefficients, interval[0]) * evaluateFunction(coefficients, Xr) < 0:
			interval[1] = Xr
			continue
		elif evaluateFunction(coefficients, interval[0]) * evaluateFunction(coefficients, Xr) > 0:
			interval[0] = Xr
			continue
		else:
			root = Xr
			keepIterating = False
			print(f"Raiz: {root}")
	
main()