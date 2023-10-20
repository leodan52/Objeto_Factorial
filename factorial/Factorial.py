# descripción
from math import factorial
import pandas as pd

def main():

	f1 = Factorial(10)
	f2 = Factorial(8)
	f3 = Factorial(5)

	print(f'{f1} = {f1.integer}')
	print(f'{f2} = {f2.integer}')
	print(f'{f3} = {f3.integer}')

	print('\nSumas\n')

	print('Con un entero o flotante:')
	print(f'\t{f1} + 10 = {f1 + 10}')
	print(f'\t14 + {f2} = {14 + f2}')

	print(f'\t{f2} + 0.25 = {f1 + 0.25}')
	print(f'\t7.31 + {f3} = {7.31 + f3}')
	print('Entre factoriales:')
	print(f'\t{f1} + {f2} = {f1 + f2}')
	print(f'\t{f2} + {f3} = {f3 + f2}')

	print('\nRestas\n')

	print('Con un entero o flotante:')
	print(f'\t{f1} - 10 = {f1 - 10}')
	print(f'\t14 - {f2} = {14 - f2}')

	print(f'\t{f2} - 0.25 = {f1 - 0.25}')
	print(f'\t-7.31 + {f3} = {- 7.31 + f3}')
	print('Entre factoriales:')
	print(f'\t-{f1} + {f2} = {- f1 + f2}')
	print(f'\t{f2} - {f3} = {f3 - f2}')



class BaseFactorial:

	def __init__(self, n_inicial, n_final):

		self.__n = n_final
		self.__inicial = n_inicial

	def __int__(self):
		return self.integer

	def __neg__(self):
		return -self.integer

	def __add__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede sumar con {type(other)}\'')
		elif isinstance(other, BaseFactorial):
			return self.integer + other.integer

		return self.integer + other

	def __radd__(self, other):
		return self + other

	def __sub__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede sumar con {type(other)}\'')

		return self.integer + (-other)

	def __rsub__(self, other):
		return -(self - other)

	def __rtruediv__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede dividir con {type(other)}\'')

		return other / self.integer

	def __eq__(self, other):
		if isinstance(other, (int, float)):
			return self.integer == other
		elif isinstance(other, BaseFactorial):
			return (self.n == other.n) and (self.inicial == other.inicial)
		else:
			return False

	def __lt__(self, other):
		if isinstance(other, (int, float)):
			return self.integer < other
		elif isinstance(other, BaseFactorial):
			if self.inicial == other.inicial:
				return self.n < other.n
			elif self.n == other.n:
				return other.inicial < self.inicial
			return self.integer < other.integer
		else:
			raise TypeError(f'No se puede comparar Factorial con {type(other)}')

	def __le__(self, other):
		return (self <  other) or (self == other)

	def __gt__(self, other):
		if isinstance(other, (int, float)):
			return self.integer > other
		elif isinstance(other, BaseFactorial):
			if self.inicial == other.inicial:
				return self.n > other.n
			elif self.n == other.n:
				return other.inicial > self.inicial
			return self.integer > other.integer
		else:
			raise TypeError(f'No se puede comparar Factorial con {type(other)}')

	def __ge__(self, other):
		return (self >  other) or (self == other)

	@property
	def n(self):
		return self.__n

	@property
	def integer(self):
		return self.__calcular()

	@property
	def inicial(self):
		return self.__inicial

	def __calcular(self):
		salida = 1
		if self.__n > 0:
			for i in range(self.__inicial, self.__n + 1):
				salida *= i
		elif self.__n == 0:
			pass

		return salida

class Factorial(BaseFactorial):
	''' Representación de la operación factorial: n!, tal que
	n! = n * (n - 1) * (n - 2) ... 3 * 2 * 1 '''

	def __init__(self, n):
		super().__init__(1, n)

	def __str__(self):
		return f'{self.n}!'

	def __repr__(self):
		return f'< Objeto Factorial, n!, n = {self.n} >'

	def __truediv__(self, other):

		if isinstance(other, BaseFactorial):
			if self.n > other.n and isinstance(other, Factorial):
				return DivFactorial(other.n + 1, self.n)
			else:
				return self.integer / other.integer

		if not isinstance(other, (int, float)):
			raise TypeError(f'Tipo \'Factorial\' no se puede dividir con {type(other)}\'')
		elif other == self.n:
			return Factorial(self.n - 1)
		elif other == self.inicial and other > 1:
			return DivFactorial(self.inicial + 1, self.n)

		return self.integer / other

	def __mul__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede multiplicar con {type(other)}\'')
		elif isinstance(other, BaseFactorial):
			return self.integer / other.integer

		if other == self.n + 1:
			return Factorial(self.n + 1)

		return self.integer * other

	def __rmul__(self, other):
		return self * other

class DivFactorial(BaseFactorial):

	def __str__(self):
		return f'{self.n}!/{self.m}!'

	def __repr__(self):
		return f'< Objeto DivFactorial, n!/m!, n = {self.n} y m = {self.m} >'

	def __truediv__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede multiplicar con {type(other)}\'')
		elif isinstance(other, BaseFactorial):
			return self.integer / other.integer

		if other == self.n:
			return DivFactorial(self.inicial, self.n - 1)
		elif other == self.inicial and other > 1:
			return DivFactorial(self.inicial + 1, self.n)

		return self.integer / other

	def __mul__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede multiplicar con {type(other)}\'')
		elif isinstance(other, BaseFactorial):
			return self.integer * other.integer

		if other == self.n + 1:
			return DivFactorial(self.m, other)
		elif other == self.m - 1:
			return DivFactorial(other, self.n)

		return self.integer * other

	def __rmul__(self, other):
		return self * other

	@property
	def m(self):
		return self.inicial - 1

if __name__ == '__main__':
	main()
