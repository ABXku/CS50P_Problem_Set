from working import convert_am, convert_pm, convert
import pytest

def test_convert_am():
    assert convert_am("9", None) == "09:00"
    assert convert_am("9", "00") == "09:00"
    assert convert_am("9", "30") == "09:30"
    assert convert_am("10", "59") == "10:59"
    assert convert_am("12", None) == "00:00"
    assert convert_am("12", "00") == "00:00"

def test_convert_pm():
    assert convert_pm("12", "00") == "12:00"
    assert convert_pm("12", None) == "12:00"
    assert convert_pm("1", "59") == "13:59"
    assert convert_pm("1", "00") == "13:00"

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
