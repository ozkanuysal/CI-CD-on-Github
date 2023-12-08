from hello import more_hello, more_bye


def test_more_hello():
    assert "SA" == more_hello()


def test_2_more_hello():
    assert "ASé" == more_hello()


def test_Bye():
    assert "bye" == more_bye()
