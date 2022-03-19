import pytest
from app.Calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correct(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_correctly(self):
        assert self.calc.division(self, 12, 4) == 3

    def test_substraction_correctly(self):
        assert self.calc.substraction(self, 6, 1) == 5

    def test_adding_correctly(self):
        assert self.calc.adding(self, 1, 7) == 8
