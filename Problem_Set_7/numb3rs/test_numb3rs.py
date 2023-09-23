from numb3rs import validate


def test_validate_true():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("123.255.0.123") == True


def test_validate_false():
    assert validate("cat") == False
    assert validate("512.512.512.512") == False
    assert validate("256.255.255.255") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.256.1.1") == False
