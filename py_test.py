import os
import pytest


def kris(x):
    if x > 0:
        return ('Yes')
    elif x == 0:
        return ('Zero')
    else:
        return ('No')


def test_pos():
    assert kris(4) == 'Yes'

def test_zero():
    assert kris(0) == 'Zero'

def test_neg():
    assert kris(-1) == 'No'


def newWorld(x):
    if x**2 > 0:
        return ('True')
    else:
        return('False')

def test_nw():
    assert newWorld(7) == 'True'

def test_nw_1():
    assert newWorld(0) == 'False'

def test_nw_2():
    assert newWorld(-4) == 'True'


def parse_txt(x):
    return len(x)

def r_txt(x):
    return x[1]

def test_rtxt():
    assert r_txt('Taffy') == 'a'

def test_rtxt_1():
    assert r_txt('AA') == 'A'

def dev_zero(x):
    return x/0

def test_devzero():
    assert dev_zero(5) == 0

def test_txt():
    assert parse_txt('Test') == 4

def mean(x):
    return sum(x)/len(x)

def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5

def test_mean_1():
    assert mean([0, 0, 0, 0]) == 0

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