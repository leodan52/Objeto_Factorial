import pytest
from factorial.Factorial import Factorial, DivFactorial

# @pytest.fixture
# def factorial_10():
# 	return Factorial(10)


# @pytest.fixture
# def factorial_8():
# 	return Factorial(8)

# @pytest.fixture
# def factorial_5():
# 	return Factorial(5)


class TestClassUnaryMethods:
	@pytest.mark.parametrize(
		"number_input, expected_value",
		[
			(0, 1),
			(1, 1),
			(2, 2),
			(3, 6),
			(4, 24),
			(5, 120),
			(8, 40_320),
			(10, 3_628_800)
		]
	)
	def test_Factorial(self, number_input, expected_value):
		f = Factorial(number_input)
		assert str(f) == f'{number_input}!'
		assert f.n == number_input
		assert f.value == expected_value


	@pytest.mark.parametrize(
		"n_input, m_input, expected_value",
		[
			(10, 8, 90),
			(5, 4, 5),
			(8, 6, 56),
			(20, 18, 380),
			(15, 9, 3_603_600),
			(52, 47, 311_875_200),
			(9, 10, 1/10),
			(18, 20, 1/380),
			(6, 8, 1/56),
			(8, 10, 1/90)
		]
	)
	def test_DivFactorial(self, n_input, m_input, expected_value):
		divf = DivFactorial(n_input, m_input)
		assert str(divf) == f'{n_input}!/{m_input}!'
		assert divf.n == n_input
		assert divf.m == m_input
		assert divf.value == expected_value
		assert divf.invert().value == (1 / expected_value)


class TestClassBinaryMethods:

	@pytest.mark.parametrize(
		"inputs, expected",
		[
			([Factorial(2), 4], 6),
			([Factorial(4), 6], 30),
			([Factorial(5), 80], 200),
			([10, Factorial(6)], 730),
			([9, Factorial(1)], 10),
			([Factorial(2), 0.5], 2.5),
			([Factorial(3), 0.25], 6.25),
			([3.14, Factorial(5)], 123.14),
			([Factorial(3), Factorial(4)], 30),
			([Factorial(3), Factorial(4), Factorial(5)], 150)
		]
	)
	def test_Factorial_sum(self, inputs, expected):
		assert sum(inputs) == expected

	@pytest.mark.parametrize(
		"a_input, b_input, expected",
		[
			(Factorial(2), 4, -2),
			(Factorial(4), 6, 18),
			(Factorial(5), 80, 40),
			(10, Factorial(6), -710),
			(9, Factorial(1), 8),
			(Factorial(2), 0.5, 1.5),
			(Factorial(3), 0.25, 5.75),
			(3.14, Factorial(5), -116.86),
			(Factorial(3), Factorial(4), -18)
		]
	)
	def test_Factorial_sub(self, a_input, b_input, expected):
		assert a_input - b_input == expected
