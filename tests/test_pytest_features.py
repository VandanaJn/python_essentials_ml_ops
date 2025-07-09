import pytest
def test_builin_fixture(tmpdir):
        # assert tmpdir==''#trying to see the tmpdir value
        pass

def test_exception():
    with pytest.raises(ZeroDivisionError) as e:
          10/0
    assert str(e.value)=="division by zero"
