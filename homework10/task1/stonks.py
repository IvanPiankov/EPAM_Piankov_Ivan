import asyncio
import datetime
import json
from typing import Any, List, Tuple

import aiohttp
import pandas as pd
from bs4 import BeautifulSoup
from numpy import NaN

URL = "https://markets.businessinsider.com/index/components/s&p_500"
URL_bank = "https://www.cbr.ru/scripts/XML_daily.asp?"


async def get_request_aiohttp(url: str) -> str:
    """
    Function take url and generate url-session
    :param url: url of page
    :return: text
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def current_course_of_dollar(url_bank: str) -> float:
    """
    Check the current course of dollar
    :param url_bank: url of central bank
    :return: current course
    """
    soup = BeautifulSoup(await get_request_aiohttp(url_bank), "html.parser")
    dollar_course = float(soup.find(text="Доллар США").next.text.replace(",", "."))
    return dollar_course


def create_json_file(name: str, date: dict):
    """
    function create json file
    :param name: name of json file
    :param date: information which will be write in file
    :return: json file
    """
    with open(f"{name}.json", "w") as file_json:
        raw_json = date.to_json(orient="table", index=False)
        json_date = json.loads(raw_json)["data"]
        file_json.write(json.dumps(json_date, indent=4))


def year_parse_company(company: str):
    """
    Parse year growth of company
    :param company: name of company
    :return: float
    """
    company_row = company.find_all("td")
    _, yaer_growth_company = company_row[-1].text.split()
    return float(yaer_growth_company[:-1:])


def url_company(company_row_for_url: str):
    """
    Parse url of company
    :param company_row_for_url: row text
    :return: url
    """
    company_row = company_row_for_url.find_all("td")
    href = company_row[0].find("a").get("href")
    url = f"https://markets.businessinsider.com{href}"
    return url


def page_of_company(company_page: str):
    """
    Read company page
    :param company_page: row text of company page
    :return: soup
    """
    soup = BeautifulSoup(company_page, "html.parser")
    return soup


def parser_for_name_and_ticker(soup: BeautifulSoup) -> Tuple[str, str]:
    """
    Parse company page and find name and company ticker
    :param soup: soup
    :return: tuple with element
    """
    name_of_company = soup.find("span", class_="price-section__label").text.strip()
    ticker_of_company = (
        soup.find("span", class_="price-section__category")
        .find("span")
        .text.lstrip(", ")
    )
    return name_of_company, ticker_of_company


def parser_for_current_price(soup: BeautifulSoup, current_course: float) -> float:
    """
    Parse current price of company
    :param soup: soup
    :param current_course: current course of dollar
    :return: price
    """
    current_price = float(
        soup.find("span", class_="price-section__current-value").text.replace(",", "")
    )
    current_price_in_rub = round(current_price * current_course, 2)
    return current_price_in_rub


def parser_for_profit(soup: BeautifulSoup) -> Any:
    """
    Parse the profit of company
    :param soup: soup
    :return: profit
    """
    try:
        low_52_week = (
            soup.find(text="52 Week Low", class_="snapshot__header")
            .previous_sibling.strip()
            .replace(",", "")
        )
    except AttributeError:
        low_52_week = NaN
    try:
        high_52_week = (
            soup.find(text="52 Week High", class_="snapshot__header")
            .previous_sibling.strip()
            .replace(",", "")
        )
    except AttributeError:
        high_52_week = NaN
    profit = NaN
    if low_52_week and high_52_week:
        profit = round(
            ((float(high_52_week) - float(low_52_week)) / float(low_52_week) * 100), 2
        )
    return profit


def parser_for_price_to_earnings(soup: BeautifulSoup) -> Any:
    """
    P/E parser
    :param soup: soup
    :return: P/E value
    """
    try:
        price_to_earnings = float(
            soup.find(text="P/E Ratio", class_="snapshot__header")
            .previous_sibling.strip()
            .replace(",", "")
        )
    except AttributeError:
        price_to_earnings = NaN
    return price_to_earnings


async def create_list_with_companies(URL_standard: str) -> None:
    """
    List with all companies
    :param URL_standard: url of site
    :return: list with company
    """
    all_url_pages = [URL_standard + f"?p={i+1}" for i in range(10)]
    generator_of_pages = [
        BeautifulSoup(await get_request_aiohttp(url_page), "html.parser")
        for url_page in all_url_pages
    ]
    list_with_links = [page.find(class_="table__tbody") for page in generator_of_pages]
    raw_table_list_with_all_company = []
    for clear_page in list_with_links:
        rows = clear_page.find_all("tr")
        raw_table_list_with_all_company.extend(rows)
    list_with_url_all_company = [
        url_company(raw_company_info)
        for raw_company_info in raw_table_list_with_all_company
    ]
    list_with_company_html = []
    for page_url in list_with_url_all_company:
        task = asyncio.create_task(get_request_aiohttp(page_url))
        list_with_company_html.append(task)
    list_with_company = await asyncio.gather(*list_with_company_html)
    list_with_company_page = []
    for general_page, company_page in zip(
        raw_table_list_with_all_company, list_with_company
    ):
        new_company = (general_page, company_page)
        list_with_company_page.append(new_company)
    return list_with_company_page


async def company_parser(company, current_course: float, df: Any) -> List:
    """
    Parse all information on one company and return pd.Series
    :param company: name of company
    :param current_course: current course of dollar
    :param df: pd.DataFrame
    :return: pd.Series
    """
    yaer_growth_company = year_parse_company(company[0])
    soup = page_of_company(company[1])
    name, ticker = parser_for_name_and_ticker(soup)
    price = parser_for_current_price(soup, current_course)
    profit = parser_for_profit(soup)
    price_to_earnings = parser_for_price_to_earnings(soup)
    return pd.Series(
        [ticker, name, price, price_to_earnings, yaer_growth_company, profit],
        index=df.columns,
    )


async def main():
    """
    Start parsing process
    :return: None
    """
    start = datetime.datetime.now()
    df = pd.DataFrame(
        columns=[
            "code",
            "name",
            "price, rub",
            "P/E",
            "growth, %",
            "potential profit, %",
        ]
    )
    course_of_dollar = await current_course_of_dollar(URL_bank)
    company_page_list = await create_list_with_companies(URL)
    list_with_task_asinc = []
    for page_url in company_page_list:
        task = asyncio.create_task(company_parser(page_url, course_of_dollar, df))
        list_with_task_asinc.append(task)
    companies_data = await asyncio.gather(*list_with_task_asinc)
    for company in companies_data:
        df = df.append([company], ignore_index=True)
    create_json_file("top10_most_expensive", df.nlargest(10, ["price, rub"]))
    create_json_file("top10_lowest_pe_ratio", df.nsmallest(10, ["P/E"]))
    create_json_file("top10_max_growth", df.nlargest(10, ["growth, %"]))
    create_json_file("top10_potential_profit", df.nlargest(10, ["potential profit, %"]))
    end = datetime.datetime.now()
    print(f"Program execute time: {end - start}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
