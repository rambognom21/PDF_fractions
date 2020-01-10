"""
This file contains definition of a fraction class.

You should put complete class here. It must be named `Fraction` and must have the following properties:

- four basic mathematical operators defined;
- elegant conversion to string in the form '3/2';
- simplification and clean-up on construction: both attribute divided by the greatest common divisor
  sign in the nominator, denominator not zero (ValueError should be raised in such case), both attributes
  must be integers (ValueError if not),
- method `decimal` returning float value of the fraction.
"""
from math import gcd


class Fraction:
    """
    Fraction class.
    """

    def __init__(self, nom, denom):
        self.nom = nom // gcd(nom,denom)
        self.denom = denom // gcd(nom,denom)
        self.valError()
        self.sanit()

    def __str__(self):
        return f"{self.nom}/{self.denom}"

    def __repr__(self):
        return f"Fraction({self.nom}, {self.denom})"

    def __eq__(self, other):
        return self.nom == other.nom and self.denom == other.denom

    def __add__(self, other):
        return (self.nom * other.denom + other.nom * self.denom)/(other.denom * self.denom)

    def __sub__(self, other):
        return (self.nom * other.denom - other.nom * self.denom)/(other.denom * self.denom)

    def __mul__(self, other):#multiplication
        return (self.nom * other.nom)/(self.denom * other.denom)

    def __truediv__(self, other):#a/b; calkowite: a//b
        return (self.nom * other.denom)/(self.denom * other.nom)

    def decimal(self):
        return self.nom/self.denom

    def valError(self):
        if self.denom == 0 or type(self.nom)!=int or type(self.nom)!=int:
            raise ValueError

    def sanit(self):
        if self.denom < 0:
            self.denom*=-1
            self.nom*=-1


#ma sie ulamek skracac greatest common divisor