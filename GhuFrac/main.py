"""
 GhuFrac v1.0
-------------------------------------------------
 Biblioteca para manipular frações!

"""


class Fraction:
    def __init__(self, nume, deno=None):
        if deno is not None:
            if type(deno) is not int and type(deno) is not float:
                raise TypeError('Insira somente valores do tipo Int ou Float')
            if type(nume) is not int and type(nume) is not float:
                raise TypeError('Insira somente valores do tipo Int ou Float')

            if deno != 0:
                if type(nume) is int:
                    self.numerador = nume
                    self.denominador = deno
                    self.simplify()
                else:
                    self.numerador, self.denominador = self.float_to_frac(nume)
                    self.denominador *= deno
                    self.simplify()
            else:
                raise ZeroDivisionError('Você está tentando dividir por 0')
        else:
            self.numerador, self.denominador = self.float_to_frac(nume)
            self.simplify()

        if self.denominador < 0:
            self.denominador = -1 * self.denominador
            self.numerador = -1 * self.numerador

    def __repr__(self):
        return f'Fraction({self.numerador},{self.denominador})'

    def __str__(self):
        if float(self.denominador) != 1.0:
            return f'{self.numerador}/{self.denominador}'
        else:
            return f'{self.numerador}'

    def __int__(self):
        return int(self.numerador / self.denominador)

    def __float__(self):
        return self.numerador / self.denominador

    def __add__(self, outra):
        if '__main__.Fraction' in str(type(outra)):
            if outra.denominador != self.denominador:
                den = self.denominador * outra.denominador
                num = self.denominador * outra.numerador + self.numerador * outra.denominador
            else:
                den = self.denominador
                num = self.numerador + outra.numerador

        elif type(outra) is int or type(outra) is float:
            numerador, denominador = self.float_to_frac(outra)
            if self.denominador != denominador:
                den = self.denominador * denominador
                num = self.denominador * numerador + self.numerador * denominador
            else:
                den = self.denominador
                num = self.numerador + numerador

        return Fraction(num, den)

    def __radd__(self, outra):
        if outra == 0:
            return Fraction(self.numerador, self.denominador)
        else:
            return self.__add__(outra)

    def __sub__(self, outra):
        if '__main__.Fraction' in str(type(outra)):
            den = self.denominador * outra.denominador
            num = - self.denominador * outra.numerador + self.numerador * outra.denominador

        elif type(outra) is int or type(outra) is float:
            numerador, denominador = self.float_to_frac(outra)
            den = self.denominador * denominador
            num = - self.denominador * numerador + self.numerador * denominador

        return Fraction(num, den)

    def __rsub__(self, outra):
        if outra == 0:
            return Fraction(-self.numerador, self.denominador)
        else:
            return self.__sub__(outra)

    def __mul__(self, outra):
        if '__main__.Fraction' in str(type(outra)):
            den = self.denominador * outra.denominador
            num = self.numerador * outra.numerador
        elif type(outra) is int or type(outra) is float:
            den = self.denominador * 1
            num = self.numerador * outra

        return Fraction(num, den)

    def __rmul__(self, outra):
        if outra == 0:
            return Fraction(0, self.denominador)
        else:
            return self.__mul__(outra)

    def __truediv__(self, outra):
        if '__main__.Fraction' in str(type(outra)):
            den = self.denominador * outra.numerador
            num = self.numerador * outra.denominador
        elif type(outra) is int or type(outra) is float:
            den = self.denominador * outra
            num = self.numerador * 1

        return Fraction(num, den)

    def __rtruediv__(self, outra):
        if outra == 0:
            return Fraction(0, self.denominador)
        else:
            return Fraction(self.denominador * outra, self.numerador)

    def __floordiv__(self, outra):
        if '__main__.Fraction' in str(type(outra)):
            return (self.numerador * outra.denominador) // (self.denominador * outra.numerador)
        elif type(outra) is int or type(outra) is float:
            return self.numerador // (self.denominador * outra)

    def __rfloordiv__(self, outra):
        return (outra * self.denominador) // self.numerador

    def __pow__(self, outra):
        return self.__float__() ** outra.__float__()

    def __rpow__(self, outra):
        return outra.__float__() ** self.__float__()

    def __pos__(self):
        return Fraction(self.numerador, self.denominador)

    def __neg__(self):
        return Fraction(-self.numerador, self.denominador)

    def __abs__(self):
        return Fraction(abs(self.numerador), self.denominador)

    def __trunc__(self):
        if self.numerador < 0:
            return abs(self.numerador) // self.denominador
        else:
            return self.numerador // self.denominador

    def __floor__(self):
        return self.numerador // self.denominador

    def __ceil__(self):
        return -(-self.numerador // self.denominador)

    def __round__(self, ndigits=None):
        if ndigits is None:
            floor, remainder = divmod(self.numerador, self.denominador)
            if remainder * 2 < self.denominador:
                return floor
            elif remainder * 2 > self.denominador:
                return floor + 1
            elif floor % 2 == 0:
                return floor
            else:
                return floor + 1

        shift = 10 ** abs(ndigits)
        if ndigits > 0:
            return Fraction(round(self * shift), shift)
        else:
            return Fraction(round(self / shift) * shift)

    def __eq__(self, outra):
        return self.__float__() == outra.__float__()

    def __lt__(self, outra):
        return self.__float__() < outra.__float__()

    def __gt__(self, outra):
        return self.__float__() > outra.__float__()

    def __le__(self, outra):
        return self.__float__() <= outra.__float__()

    def __ge__(self, outra):
        return self.__float__() >= outra.__float__()

    def __bool__(self, outra):
        return bool(self.numerador)

    def simplify(self):
        a = self.numerador
        b = self.denominador
        r = 1

        while r != 0:
            r = a % b
            a, b = b, r

        self.numerador = int(self.numerador / a)
        self.denominador = int(self.denominador / a)

    @staticmethod
    def float_to_frac(num):
        num_str = str(num)

        if '.' in num_str:
            num_split = num_str.split('.')
            if len(num_split) == 2:
                tam_dec = len(num_split[1])
                dec = int('1' + tam_dec * '0')
                numerador = int(str(num_split[0]) + str(num_split[1]))
                return numerador, dec
            else:
                raise SyntaxError('Por favor, digite o número corretamente')
        else:
            return num, 1
