from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hello, Liam") == 0


def test_start_with_h():
    assert value("hi!") == 20
    assert value("Hi!") == 20
    assert value("How are you doing?") == 20


def test_normal_case():
    assert value("what's up") == 100
    assert value("What's up") == 100


def test_blank_space():
    assert value("   hello   ") == 0
    assert value("  Hi!  ") == 20
    assert value("  What's up  ") == 100


def test_blank_input():
    assert value("") == 100
