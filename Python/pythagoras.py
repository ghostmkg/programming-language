"""
This is a pure Python implementation of the Pythagoras Triplets
"""

from math import sqrt
class Pythagoras:
    def pythagoras_triplet(side1 : int, side2:  int) -> int:
        hypotenuse = int(sqrt(side1**2 + side2**2))
        return hypotenuse


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    side1 = int(input("Enter the side one of the right triangle"))
    side2 = int(input("Enter the side two of the right triangle"))

    print("Formula of hypotenuse  => sqare root of side1^2 + side2^2")
    print(Pythagoras.pythagoras_triplet(side1, side2))
