from morse import decode
import pytest


@pytest.mark.parametrize(
    "string_to_decode,result",
    [
        ('.... . .-.. .-.. --- -....- .-- --- .-. .-.. -.. ..--..',
         'HELLO-WORLD?'),
        ('.- .- .- -....- -.. ... -.--. ..--- ----- ..--- ..--- '
         '-.--.- - . ... - ... -....- .... --- -- . .-- --- .-. -.-',
         'AAA-DS(2022)TESTS-HOMEWORK'),
        ('.. ... ... ..- . -....- ----- ..--- -....- -.. . -.-. --- '
         '-.. . -....- ..-. ..- -. -.-. - .. --- -. -....- - . ... -',
         'ISSUE-02-DECODE-FUNCTION-TEST'),
        ('-.--. -.--.- -.--.- -..-. .-. -..-. -. -..-. ..--.. -..-. '
         '.---- ....- .---- ..--- -....- ..... ...-- ....- '
         '-....- -.... ---.. --...',
         '())/R/N/?/1412-534-687'),
        ('-..- ' * 10, 'XXXXXXXXXX')
    ]
)
def test_decode_parametric(string_to_decode, result):
    """Testing decode function with several cases."""
    assert decode(string_to_decode) == result


if __name__ == "__main__":
    """"""
    pass
