"""Changing bases."""

digits = {}

for i in range(0, 10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'


def change_to_base(n: int, b: int) -> str:
    """
    Return `n` in base `b`.

    The base `b` must be in the range 2 to 16.

    >>> change_to_base(1, 2)
    '1'
    >>> change_to_base(31, 2)
    '11111'
    >>> change_to_base(31, 8)
    '37'
    >>> change_to_base(31, 16)
    '1F'
    """
    assert 2 <= b <= 16
    x = ""
    i = n
    if i == 0:
        return "0"
    elif i < 0:
        i = (-1)*i

    while i:
    
        x += (str(digits[i % b]))
        i //= b
    if n < 0:
        x += "-"
    x = x[::-1]
    return x   # FIXME: return n in the right base
