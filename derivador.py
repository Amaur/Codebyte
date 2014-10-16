#!/usr/bin/env python3

import abc
import functools
import numbers
import operator


class Expr(object, metaclass=abc.ABCMeta):
    @staticmethod
    def _conv_expr(v):
        if isinstance(v, numbers.Real) and not isinstance(v, Expr):
            v = Const(v)
        return v

    @abc.abstractmethod
    def diff(self, v):
        pass

    @abc.abstractmethod
    def eval(self, dic):
        pass

    def __add__(self, y):
        return Add(self, self._conv_expr(y))

    def __mul__(self, y):
        return Mult(self, self._conv_expr(y))

    def __radd__(self, y):
        return self._conv_expr(y) + self

    def __rmul__(self, y):
        return self._conv_expr(y) * self


class Var(Expr):
    __slots__ = ('_name',)

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def diff(self, v):
        return Const(1 if v == self else 0)
    
    def eval(self, dic):
        if self in dic:
            return dic[self]
        else:
            return self

    def __eq__(self, y):
        if isinstance(y, Var):
            y = y.name
        return self._name == y

    def __hash__(self):
        return hash(self._name)
    
    def __repr__(self):
        return str(self._name)

        
@functools.total_ordering
class Const(Expr, numbers.Real):
    __slots__ = ('_value',)

    def __init__(self, value):
        assert isinstance(value, numbers.Real)
        self._value = value

    @staticmethod
    def _conv(y):
        if isinstance(y, Const):
            y = y._value
        return y

    def _op(self, op, y):
        if not isinstance(y, numbers.Real):
            return getattr(super(), op)(y)
        return Const(getattr(self._conv(self), op)(self._conv(y)))

    def __abs__(self):
        return Const(abs(self._value))

    def __add__(self, y):
        return self._op('__add__', y)

    def __ceil__(self):
        return Const(math.ceil(self._value))

    def __eq__(self, y):
        return self._value == self._conv(y)

    def __float__(self):
        return Const(float(self._value))

    def __floor__(self):
        return Const(math.floor(self._value))

    def __floordiv__(self, y):
        return self._op('__floordiv__', y)

    def __hash__(self):
        return hash(self._value)
        
    def __le__(self, y):
        return self._conv(self) <= self._conv(y)

    def __lt__(self, y):
        return self._value < self._conv(y)

    def __mod__(self, y):
        return self._op('__mod__', y)
    
    def __mul__(self, y):
        return self._op('__mul__', y)

    def __neg__(self):
        return Const(-self._value)

    def __pos__(self):
        return Const(+self._value)

    def __pow__(self, y):
        return self._op('__pow__', y)

    def __repr__(self):
        return repr(self.value)

    def __radd__(self, y):
        return NotImplemented

    def __rfloordiv__(self, y):
        return NotImplemented

    def __rmod__(self, y):
        return NotImplemented

    def __rmul__(self, y):
        return NotImplemented

    def __round__(self):
        return Const(round(self._value))

    def __rpow__(self, y):
        return NotImplemented

    def __rtruediv__(self, y):
        return NotImplemented
    
    def __truediv__(self, y):
        return self._op('__truediv__', y)

    def __trunc__(self):
        return Const(math.trunc(self._value))
            
    def diff(self, v):
        return Const(0)

    @property
    def value(self):
        return self._value

    def eval(self, dic):
        return self


class BinOp(Expr):
    __slots__ = ('_left', '_right')

    def __new__(cls, left, right):
        self = super(BinOp, cls).__new__(cls)
        self._left = left
        self._right = right
        return self

    def __repr__(self):
        return '{class_name}({left!r}, {right!r})'.format(class_name=type(self).__name__,
                                                          left=self._left,
                                                          right=self._right)

    
class Add(BinOp):
    def diff(self, v):
        return self._left.diff(v) + self._right.diff(v)

    def __new__(cls, left, right):
        if left == 0:
            return right
        if right == 0:
            return left
        return super(Add, cls).__new__(cls, left, right)

    def eval(self, dic):
        return self._left.eval(dic) + self._right.eval(dic)


class Mult(BinOp):
    def diff(self, v):
        return self._left.diff(v) * self._right + self._left * self._right.diff(v)
    
    def __new__(cls, left, right):
        if left == 0 or right == 0:
            return Const(0)
        if left == 1:
            return right
        if right == 1:
            return left
        return super(Mult, cls).__new__(cls, left, right)

    def eval(self, dic):
        return self._left.eval(dic) * self._right.eval(dic)


if __name__ == '__main__':
    x = Var('x')
    dez_x = 10 * x
    y = dez_x * dez_x
    
    dy_dx = y.diff(x)
    print('y = {y}'.format(y=y))
    print('dy/dx = {dy_dx}'.format(dy_dx=dy_dx))
    print('dy/dx(3) = {dy_dx3}'.format(dy_dx3=dy_dx.eval({x: 3})))
