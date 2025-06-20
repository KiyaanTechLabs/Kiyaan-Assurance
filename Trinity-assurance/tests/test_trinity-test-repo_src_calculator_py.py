Here is the test file content:
```
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(-2, -3) == -5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-5, 3) == -8
    assert subtract(-5, -3) == 2

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-4, 5) == -20
    assert multiply(-4, -5) == 20

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    with pytest.raises(ValueError):
        divide(10, 0)
    with pytest.raises(ValueError):
        divide(-10, 0)
```
Note: I used the Pytest framework and wrote test cases for each function to verify their correctness, edge cases, and error handling.