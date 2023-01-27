import pytest
import numpy as np

def test_array():
    a=np.zeros((5,5))
    print(a)

def test_array_sum():
    a=np.array([1,2,3])
    b=np.array([4,5,6])
    c=np.sum((a,b),axis=0)
    print('\n Sum of Array : ', c)
    