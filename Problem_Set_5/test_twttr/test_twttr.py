from twttr import shorten


def test_lower_case():
    assert shorten("twitter") == "twttr"
    assert shorten("what's your name?") == "wht's yr nm?"


def test_upper_case():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("WHAT'S YOUR NAME?") == "WHT'S YR NM?"


def test_number():
    assert shorten("50") == "50"


def test_blank_input():
    assert shorten("") == ""
