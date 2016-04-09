def add(a, b):
    return a + b
 
def test_add_1():
    assert add(3, 4) == 7
 
def test_add_2():
    assert add(0, 5) == 5
 
def test_add_3():
    assert add(-1, 3) == 2