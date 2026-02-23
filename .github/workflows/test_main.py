from main import add

def test_add_success():
    assert add(2, 3) == 5

def test_add_fail():
    assert add(1, 1) != 3