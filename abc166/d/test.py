import main
import pytest
from unittest.mock import patch, mock_open

examples = [
    ['33', '2 -1'],
    ['1', '0 -1'],
]


@pytest.mark.parametrize('inputs,  expected', examples)
def test(inputs, expected):
    with patch('main.open', mock_open(read_data=inputs)):
        assert main.main() == expected


# @pytest.mark.parametrize('inputs,  expected', examples)
# def test(inputs, expected):
#     with patch('main.open', mock_open(read_data=inputs)):
#         ans = main.main()
#         expected = float(expected)
#         abs_err = abs(ans - expected)
#         rel_err = abs_err / expected
#         if abs_err <= 10**-9 or rel_err <= 10**-9:
#             assert True
#         else:
#             assert False
