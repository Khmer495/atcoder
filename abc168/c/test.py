import main
import pytest
from unittest.mock import patch, mock_open

examples = [
    ['3 4 9 0', '5.00000000000000000000'],
    ['3 4 10 40', '4.56425719433005567605'],
]


@pytest.mark.parametrize('inputs,  expected', examples)
def test(inputs, expected):
    with patch('main.open', mock_open(read_data=inputs)):
        ans = main.main()
        expected = float(expected)
        abs_err = abs(ans - expected)
        rel_err = abs_err / expected
        if abs_err <= 10**-9 or rel_err <= 10**-9:
            assert True
        else:
            assert False
