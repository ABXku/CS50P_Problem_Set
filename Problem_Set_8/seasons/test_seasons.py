from seasons import convert
from datetime import date
from dateutil.relativedelta import relativedelta

def test_convert():
    assert convert(date.today() - relativedelta(years=1)) == "Five hundred twenty-five thousand, six hundred"
    assert convert(date.today() - relativedelta(years=2)) == "One million, fifty-one thousand, two hundred"
