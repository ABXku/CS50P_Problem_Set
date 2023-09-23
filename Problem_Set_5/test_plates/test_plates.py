from plates import is_valid


def test_length():
    assert is_valid("ABC123") == True
    assert is_valid("ABC12345") == False
    assert is_valid("A") == False


def test_first_two_characters():
    assert is_valid("CS50") == True
    assert is_valid("C123") == False
    assert is_valid("123") == False


def test_first_number():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_number_in_mid():
    assert is_valid("CS50CS") == False


def test_punc_period_space():
    assert is_valid("CS,50") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False
