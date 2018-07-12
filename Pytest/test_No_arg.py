import pytest
def function():
    raise SystemExit(1)

def test_my():
    with pytest.raises(SystemExit):
        function()
