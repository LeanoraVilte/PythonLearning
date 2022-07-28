A = type("A", (), {})
print(A)

class Foo:
    ...

a = Foo()
b = Foo()

print ( a == b)

print (*[i * 2 for i in range(4)])

a = ()

print(type(a))

a = complex(4,7) + 2

print(abs(a + 1j))

a = (1, 1.0)

print(isinstance(a, (int, float)))

_A__variable = 1
class A:
    def get_variable(self):
        return __variable

print(A().get_variable())