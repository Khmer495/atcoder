import main
import pytest
from unittest.mock import patch, mock_open

examples = [
    ['7\nnikoandsolstice', 'nikoand...'],
    ['40\nferelibenterhominesidquodvoluntcredunt', 'ferelibenterhominesidquodvoluntcredunt'],
]


@pytest.mark.parametrize('inputs,  expected', examples)
def test(inputs, expected):
    with patch('main.open', mock_open(read_data=inputs)):
        assert main.main() == expected
