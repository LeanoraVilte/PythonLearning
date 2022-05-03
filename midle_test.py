def middle(x):
    if len(x)%2 == 0:
        a = len(x)
        e = int(a/2 - 1)
        d = x[e] + x[e + 1]
        return d/2
    else:
        e = int(len(x)/2)
        return x[e]

def test_middle():
    assert middle([0, 0, 0, 0]) == 0

def test_middle_1():
    assert middle([1, 2, 3]) == 2

def test_middle_2():
    assert middle([1, 2, 3, 4]) == 2.5

def test_middle_3():
    assert middle([1, 2]) == 1.5

def test_middle_4():
    assert middle([1]) == 1