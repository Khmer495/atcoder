import main
import pytest
from unittest.mock import patch, mock_open

examples = [
    ['4 3\n1 2 3 4\n1 3\n2 3\n2 4', 2],
    ['6 5\n8 6 9 1 2 1\n1 3\n4 2\n4 3\n4 6\n4 6', 3],
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
