class Culc(object):
    """Add and Doubel
    """
    def add_and_doubel(self, x, y):
        """Add and Doubel
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result 
