class ListMath:
    def __init__(self, lst_math = []):
        self.lst_math = [i for i in lst_math if type(i) in (int, float)]

    def __add__(self, other):
        new_list = [i + other for i in self.lst_math]
        return ListMath(new_list)

    def __radd__(self, other):
        new_list = [other + i for i in self.lst_math]
        return ListMath(new_list)

    def __iadd__(self, other):
        for position, value in enumerate(self.lst_math):
            self.lst_math[position] += other
        return self

    def __sub__(self, other):
        new_list = [i - other for i in self.lst_math]
        return ListMath(new_list)

    def __rsub__(self, other):
        new_list = [other - i for i in self.lst_math]
        return ListMath(new_list)

    def __isub__(self, other):
        for position, value in enumerate(self.lst_math):
            self.lst_math[position] -= other
        return self

    def __mul__(self, other):
        new_list = [i * other for i in self.lst_math]
        return ListMath(new_list)

    def __rmul__(self, other):
        new_list = [other * i for i in self.lst_math]
        return ListMath(new_list)

    def __imul__(self, other):
        for position, value in enumerate(self.lst_math):
            self.lst_math[position] *= other
        return self

    def __truediv__(self, other):
        new_list = [i / other for i in self.lst_math]
        return ListMath(new_list)

    def __rtruediv__(self, other):
        new_list = [other / i for i in self.lst_math]
        return ListMath(new_list)

    def __itruediv__(self, other):
        for position, value in enumerate(self.lst_math):
            self.lst_math[position] /= other
        return self