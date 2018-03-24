from fb import fizzbuzz
import pytest

#testujeme, ze je argument str
def test_fizzbuzz_returns_str():
    assert isinstance(fizzbuzz(1), str)

#parametrizujeme pro vice moznosti argumentu (1 a 2)
@pytest.mark.parametrize('num', [1, 2, 4, 7, 8, 11, 13, 14])
#testujeme, ze pokud argument neni delitelny 3 nebo 5, funkce vrati stejne cislo zpet
def test_fizzbuzz_regular_returns_self(num):
    assert fizzbuzz(num) == str(num)

@pytest.mark.parametrize('num', [3, 6, 9, 12])
#testujeme, ze pokud je argument delitelny 3, funce vrati fizz
def test_fizzbuzz_3div_returns_fizz(num):
    assert fizzbuzz(num) == "fizz"

@pytest.mark.parametrize('num', [5, 10, 8885])
#testujeme, ze pokud je argument delitelny 5, funkce vrati buzz
def test_fizzbuzz_5div_returns_buzz(num):
    assert fizzbuzz(num) == "buzz"

@pytest.mark.parametrize('num', [15, 30, 15000015])
#testujeme, ze pokud je argument delitelny 3 i 5 najednou, funkce vrati fizzbuzz
def test_fizzbuzz_3div_5div_returns_fizzbuzz(num):
    assert fizzbuzz(num) == "fizzbuzz"
