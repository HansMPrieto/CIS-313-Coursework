import math
class mathOps:

    def __init__(self, u, v):
        self.u = u
        self.v = v
    
    def __repr__(self):
        return "LeastCommonMultiple({}, {})".format(self.u, self.v)
    
    def __str__(self):
        return "GreatestCommonDivisor({}, {}).".format(self.u, self.v)

    def valid(self):
        return isinstance(self.u, int) and isinstance(self.v, int)
    
    def gcd(self):
        # Find the greatest common divisor of a and b
        # Hint: Use Euclid's Algorithm
        # https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure
        tempU = self.u
        tempV = self.v
        try:
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise OverflowError
            elif isinstance(tempU, str) or isinstance(tempV, str):
                raise TypeError

        except OverflowError:
            print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
            raise OverflowError

        except TypeError:
            print("one or both the values of", tempU, " and ", tempV, "are strings")
            raise TypeError

        if isinstance(tempU, float) or isinstance(tempV, float):
            tempU = math.ceil(tempU)
            tempV = math.ceil(tempV)

        while tempV:
            tempU, tempV = abs(tempV), abs(tempU % tempV)
        return abs(tempU)


        
    def lcm(self):
        # Find the least common multiple of a and b
        # Hint: Use the gcd of a and b
        try:
            tempU = self.u
            tempV = self.v
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise OverflowError
            elif tempU == 0 or tempV == 0:
                raise ValueError
            elif isinstance(tempU, str) or isinstance(tempV, str):
                raise TypeError
      
        except OverflowError:
            print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
            raise OverflowError

        except ValueError:
            print("one or both of the values of", tempU, " and ", tempV, "are equal to 0")
            raise ValueError

        except TypeError:
            print("one or both the values of", tempU, " and ", tempV, "are strings")
            raise TypeError

        if isinstance(tempU, float) or isinstance(tempV, float):
            tempU = math.ceil(tempU)
            tempV = math.ceil(tempV)

        values = mathOps(tempU, tempV)
        values_gcd = values.gcd()

        least_common_multiple = (tempU * tempV) // values_gcd
        return least_common_multiple
