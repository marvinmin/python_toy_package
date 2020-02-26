import numpy as np
def sqsum(a):
    """
    Calculate the squared sum of a list

    Parameters
    ----------
    a: list
        the list of numbers to be calculated
    
    Return
    ------
    float
        the squared sum
    
    Examples
    --------
    >>> a = [1, 2, 3]
    >>> sqsum(a)
    14
    """
    a = np.array(a)
    return np.sum(a**2)
