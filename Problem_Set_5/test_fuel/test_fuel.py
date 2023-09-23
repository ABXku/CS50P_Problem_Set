from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("0/1") == 0


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("2/1")


def test_zero_div_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
