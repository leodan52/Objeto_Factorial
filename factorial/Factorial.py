# descripción
from math import factorial
import pandas as pd

class BaseFactorial:

	def __init__(self, n_final, n_inicial):

		self.__n = n_final
		self.__inicial = n_inicial
		self.__m = n_inicial - 1

	def __neg__(self):
		return -self.value

	def __add__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede sumar con {type(other)}\'')
		elif isinstance(other, BaseFactorial):
			return self.value + other.value

		return self.value + other

	def __radd__(self, other):
		return self + other

	def __sub__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede sumar con {type(other)}\'')

		return self.value + (-other)

	def __rsub__(self, other):
		return -(self - other)

	def __eq__(self, other):
		if isinstance(other, (int, float)):
			return self.value == other
		elif isinstance(other, BaseFactorial):
			return (self.n == other.n) and (self.inicial == other.inicial)
		else:
			return False

	def __lt__(self, other):
		if isinstance(other, (int, float)):
			return self.value < other
		elif isinstance(other, BaseFactorial):
			if self.inicial == other.inicial:
				return self.n < other.n
			elif self.n == other.n:
				return other.inicial < self.inicial
			return self.value < other.value
		else:
			raise TypeError(f'No se puede comparar Factorial con {type(other)}')

	def __le__(self, other):
		return (self <  other) or (self == other)

	def __gt__(self, other):
		if isinstance(other, (int, float)):
			return self.value > other
		elif isinstance(other, BaseFactorial):
			if self.inicial == other.inicial:
				return self.n > other.n
			elif self.n == other.n:
				return other.inicial > self.inicial
			return self.value > other.value
		else:
			raise TypeError(f'No se puede comparar Factorial con {type(other)}')

	def __ge__(self, other):
		return (self >  other) or (self == other)

	@property
	def n(self):
		return self.__n

	@property
	def m(self):
		return self.__m

	@property
	def value(self):
		return self.__calcule()

	@property
	def inicial(self):
		return self.__inicial

	def __calcule(self):
		salida = 1
		if self.__n <= 0 and self.m == 0:
			return salida

		if self.__inicial == self.__n:
			return self.__n

		final = max(self.__m, self.__n)
		inicial = min(self.__m, self.__n)

		for i in range(inicial + 1, final + 1):
			salida *= i

		if self.__m < self.__n:
			return salida
		else:
			return 1 / salida

	def factors(self):

		if self.__n <= 0 and self.m == 0:
			return {1}, set()

		if self.__inicial == self.__n:
			return {self.__n}, set()

		initial = min(self.__m, self.__n)
		final = max(self.__m, self.__n)

		# print()
		# print(f, initial, final)
		# for i in range(initial + 1, final + 1):
		# 	print(f'\t{i}')

		factors = {i for i in range(initial + 1, final + 1)} | {1}
		# print('\t', factors)

		if self.__inicial <= self.__n:
			num, den = factors, {1}
		else:
			num, den = {1}, factors

		# print('\t', num, den)

		return num, den

class DivFactorial(BaseFactorial):

	def __init__(self, n, m):
		super().__init__(n, m + 1)

	def __str__(self):
		return f'{self.n}!/{self.m}!'

	def __repr__(self):
		return f'< Objeto DivFactorial, n!/m!, n = {self.n} y m = {self.m} >'

	def __rtruediv__(self, other):
		return self.invert() * other

	def __mul__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede multiplicar con {type(other)}\'')
		elif isinstance(other, float):
			return NumericFactorial(self.value * other)
		elif isinstance(other, int):
			other_factorial = DivFactorial(other - 1, other)
		else:
			other_factorial = other

		if self.n == other_factorial.m:
			if self.m == 0:
				return Factorial(other_factorial.n)
			else:
				return DivFactorial(self.m, other_factorial.n)
		elif other_factorial.n == self.m:
			if other_factorial.m == 0:
				return Factorial(self.n)
			else:
				return DivFactorial(other_factorial.m, self.n)
		else:
			return NumericFactorial(DivFactorial.__mul(self, other_factorial))

	def __rmul__(self, other):
		return self * other

	def invert(self):
		return DivFactorial(self.m, self.n)

	def __truediv__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede multiplicar con {type(other)}\'')
		elif isinstance(other, int):
			return self * DivFactorial(other-1, other).invert()
		elif isinstance(other, BaseFactorial):
			return self * other.invert()

		if other == self.n:
			return DivFactorial(self.m, self.n - 1)
		elif other == self.inicial and other > 1:
			return DivFactorial(self.m + 1, self.n)
		elif isinstance(other, float):
			return NumericFactorial(self.value / other)

		return NumericFactorial(DivFactorial.__mul(self, other.invert()))

	def __rtruediv__(self, other):
		return self.invert() * other

	@staticmethod
	def __mul(f1, f2):
		f1_num, f1_den = f1.factors()
		f2_num, f2_den = f2.factors()

		num_factors = list(f1_num) + list(f2_num)
		den_factors = list(f1_den) + list(f2_den)
		num_factors.sort(), den_factors.sort()

		list_short = sorted([num_factors.copy(),
							den_factors.copy()], key=len)[0]

		for f in list_short:
			if f in num_factors and f in den_factors and f != 1:
				num_factors.remove(f)
				den_factors.remove(f)

		num = DivFactorial.__prod(num_factors)
		den = DivFactorial.__prod(den_factors)

		if den == 1:
			return num
		else:
			return num / den


	@staticmethod
	def __prod(iter_):
		salida = 1
		for i in iter_:
			salida *= i
		return salida



class Factorial(DivFactorial):
	''' Representación de la operación factorial: n!, tal que
	n! = n * (n - 1) * (n - 2) ... 3 * 2 * 1 '''

	def __init__(self, n):
		super().__init__(n, 0)

	def __str__(self):
		return f'{self.n}!'

	def __repr__(self):
		return f'< Objeto Factorial, n!, n = {self.n} >'

	@staticmethod
	def prod(a, b):
		''' Ejecuta la multiplicación de factoriales de la forma a! * b! '''

		a_factorial = Factorial(a)
		b_factorial = Factorial(b)

		return (a_factorial*b_factorial).value


	@staticmethod
	def div(a, b):
		''' Ejecuta la división de factoriales de la forma a!/b! '''

		a_factorial = Factorial(a)
		b_factorial = Factorial(b)

		return (a_factorial/b_factorial).value


class NumericFactorial(BaseFactorial):
	def __init__(self, result):
		super().__init__(result, result)

	def __repr__(self):
		if isinstance(self.value, int):
			repr = f'{self.value:,}'
		elif self.value >= 0.01:
			repr = f'{self.value:,.2f}'
		else:
			repr = f'{self.value:.2e}'

		return f'< Objeto NumericFactorial, value = {repr} >'

	def invert(self):
		return NumericFactorial(1 / self.value)

	def __truediv__(self, other):
		if not isinstance(other, (int, float, BaseFactorial)):
			raise TypeError(f'Tipo \'Factorial\' no se puede multiplicar con {type(other)}\'')
		elif isinstance(other, int):
			return self * DivFactorial(other-1, other).invert()
		elif isinstance(other, BaseFactorial):
			return self * other.invert()

	def __rtruediv__(self, other):
		return (self / other).invert()

if __name__ == '__main__':
	main()
