from src.math_operations import add, sub, mul, div

def test_add():
  assert add(3, 5) == 8
  assert add(-1, 1) == 0

def test_sub():
  assert sub(2, 3) == -1
  assert sub(5, 3) == 2
  assert sub(1, 1) == 0
  assert sub(1, -1) == 2
  assert sub(-2, 2) == -4

def test_mul():
  assert mul(2, 3) == 6
  assert mul(5, 3) == 15
  assert mul(1, 1) == 1
  assert mul(1, -1) == -1
  assert mul(-2, 0) == 0

def test_div():
  assert div(2, 3) == 0.6666666666666666
  assert div(5, 3) == 1.6666666666666667
  assert div(1, 1) == 1
  assert div(1, -1) == -1
  assert div(-2, 2) == -1
