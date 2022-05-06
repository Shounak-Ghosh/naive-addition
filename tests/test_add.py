from src.add import add
import numpy as np
def test_add():
    assert add(1) == 101
    assert add(np.zeros(1)) == 100
    assert add(np.zeros(1), np.array([1])) == 1
    assert add("fourth", "Brain") == "fourthBrain"

