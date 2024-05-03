#!/usr/bin/python3
def this_raises():
    """This function always raises an exeception

    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: here is the error
    >>> this_raises()
    Traceback (innermost last):
    RuntimeError: here is the error
    """
    raise RuntimeError("here is the error")