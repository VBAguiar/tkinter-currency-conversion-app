import sys, os; myPath = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, myPath + '/../')

from src.main import EconomiaApi
import pytest

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def test_EconomiaApi_return_float():
	e = EconomiaApi('USD', 'BRL')
	
	assert isfloat(e.get()) == True

@pytest.mark.xfail()
def test_EconomiaApi_receive_equal_values():
	e = EconomiaApi('BRL', 'BRL')
	
	assert isfloat(e.get()) == True
