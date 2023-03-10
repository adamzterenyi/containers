def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''

    i = a
    if b is None and c is None:
        i = 0
        while i < a:
            yield i
            i += 1
    elif c is None:
        while i < b:
            yield i
            i += 1
    elif c > 0:
        while i < b:
            yield i
            i += c
    else:
        while i > b:
            yield i
            i += c
