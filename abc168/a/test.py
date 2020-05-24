import main
import pytest
from unittest.mock import patch, mock_open

examples = [
    ['16', 'pon'],
    ['2', 'hon'],
    ['183', 'bon'],
]


@pytest.mark.parametrize('inputs,  expected', examples)
def test(inputs, expected):
    with patch('main.open', mock_open(read_data=inputs)):
        assert main.main() == expected
