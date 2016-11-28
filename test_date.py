"""Simple test cases"""
import date_simple as ds
import datetime as dt
import pytest

def test_get_date_value():
    today = dt.datetime.today()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    assert ds.get_date() == today
    assert ds.get_date('2016-05-05') == dt.datetime(2016, 5, 5, 0, 0)
    assert ds.get_date('5/5/2016') == dt.datetime(2016, 5, 5, 0, 0)
    assert ds.get_date('7/5/2016') == dt.datetime(2016, 7, 5, 0, 0)


def test_get_date_value_failure():
    assert  ds.get_date('5/7/2016') != dt.datetime(2016, 7, 5, 0, 0)
    assert ds.get_date('11/5/2016') != dt.datetime(2016, 7, 5, 0, 0)  

def test_type_error():
    with pytest.raises(Exception):
        ds.get_date('11/5/16')

def test_add_day( ):
    today = dt.datetime.today()
    today=today.replace(hour=0, minute=0,second=0,microsecond=0)
    assert ds.add_day(today , 1) == dt.datetime(2016, 11, 28, 0, 0)
    assert ds.add_day(dt.datetime(2016, 5, 5, 0, 0), 3) == dt.datetime(2016, 5, 8, 0, 0)
    assert ds.add_day(dt.datetime(2016, 5, 4, 0, 0), -2) == dt.datetime(2016, 5, 2, 0, 0)

def test_add_week( ):
    assert ds.add_week(dt.datetime(2016, 5, 5, 0, 0), 1) == dt.datetime(2016, 5, 12, 0, 0)
    assert ds.add_week(dt.datetime(2016, 5, 5, 0, 0), 2) == dt.datetime(2016, 5, 19, 0, 0)

def test_format_date():
    assert ds.format_date(dt.datetime(2016, 5, 5, 0, 0), '%m/%d/%Y') == '05/05/2016'
    assert ds.format_date(dt.datetime(2016, 5, 6, 0, 0),'%m/%d/%Y') == '05/06/2016'
    assert ds.format_date(dt.datetime(2016, 7, 5, 0, 0), '%d-%b-%y') == '05-Jul-16'

def test_month_only():
    assert ds.month_only(dt.datetime(2016, 5, 5, 0, 0)) == '05'


