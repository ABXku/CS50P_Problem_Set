from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    jar = Jar(13)
    assert jar.capacity == 13
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(12)

def test_withdraw():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
