import os

import pytest
from bs4 import BeautifulSoup

import homework10.task1.stonks as hw

PATH = os.path.dirname(__file__) + os.path.sep


def test_growth():
    with open(PATH + "apple_main.txt", "r") as file:
        text = file.read()
    soup = BeautifulSoup(text, "html.parser")
    company = soup.find("tr")
    growth = hw.year_parse_company(company)
    assert growth == 51.02


def test_price():
    with open(PATH + "apple_page.txt", "r") as file:
        text = file.read()
    soup = BeautifulSoup(text, "html.parser")
    latest_prices = hw.parser_for_current_price(soup, 1)
    assert latest_prices == 150.68


def test_ticker_name():
    with open(PATH + "apple_page.txt", "r") as file:
        text = file.read()
    soup = BeautifulSoup(text, "html.parser")
    ticker_name = hw.parser_for_name_and_ticker(soup)
    assert ticker_name == ("Apple Inc.", "AAPL")


def test_parser_for_profit():
    with open(PATH + "apple_page.txt", "r") as file:
        text = file.read()
    soup = BeautifulSoup(text, "html.parser")
    profit = hw.parser_for_profit(soup)
    assert profit == 46.59


def test_for_p_e():
    with open(PATH + "apple_page.txt", "r") as file:
        text = file.read()
    soup = BeautifulSoup(text, "html.parser")
    p_e = hw.parser_for_price_to_earnings(soup)
    assert p_e == 35.60
