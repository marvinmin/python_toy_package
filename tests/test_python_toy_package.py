from python_toy_package import python_toy_package
import numpy as np

def test_sqsum():
    a = np.array([1,2,3])
    assert python_toy_package.sqsum(a) == 14
