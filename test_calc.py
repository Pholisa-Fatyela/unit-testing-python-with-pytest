import calc

def test_inc_3_by_1():
    assert calc.inc(3,1) == 4

def test_decr_3_by_1():
    assert calc.decr(3,1) == 2

def test_multiply_by_7():
    assert calc.mult(7, 6) == 42

def test_divide_by_12_by_3():
    assert calc.divide(12, 3) == 4

def test_inc_string_9_plus_3():
    assert calc.execute(9, 3, "+") == 12



