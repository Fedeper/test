import unittest
import test
from sut import *

class TestSut(unittest.TestCase):

    def test_area(self):
        calc_area=area(5, 4)
        self.assertTrue(calc_area == 20)

    def test_saludar(self):
        saludo = saludar('Fede')
        self.assertTrue(saludo == "Hola Fede")

    def test_sumar(self):
        suma = sumar(8, 5)
        self.assertTrue(suma == 13)

if __name__ == '__main__':
    unittest.main()
