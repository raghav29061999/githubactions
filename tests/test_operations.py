from src.math_operations import add, subtract, divide


def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_sub():
    assert subtract(4,2)==2
    assert subtract(5,1)==4

def test_divide():
    assert divide(9,1)==9
    
