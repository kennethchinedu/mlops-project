import pytest 


# n = input("What is the number? ")

def double(n):
    
    return n * 2

def test_double_with_normal_number():
    assert double(2) == 4


def test_double_with_string():
    assert double("hello") == "hellohello"