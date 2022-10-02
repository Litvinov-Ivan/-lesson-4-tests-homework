from morse import encode


def test_encode_sos():
    """
    >>> encode('SOS')
    '... --- ...'
    """


def test_encode_aaa():
    """
    >>> encode('AAA-DS (2022) TESTS-HOMEWORK')
    '.- .- .- -....- -.. ...   -.--. ..--- -----
    ..--- ..--- -.--.-   - . ... - ... -....- .... --- -- . .-- --- .-. -.-'
    """


def test_encode_exception():
    """
    >>> encode('ТЕСТ КИРИЛЛИЦЫ')
    Traceback (most recent call last):
    ...
    KeyError: 'Т'
    """


def test_encode_hello_world():
    """
    >>> encode('HELLO WORLD')  # doctest: +ELLIPSIS
    '.... ...'
    """


if __name__ == "__main__":
    pass
