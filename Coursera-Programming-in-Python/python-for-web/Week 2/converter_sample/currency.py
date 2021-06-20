from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=' + date
    response = requests.get(url)  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'lxml')
    if cur_from == 'RUR':
        to_nominal = int(soup.find('charcode', text=cur_to).find_next_sibling('nominal').string)
        to_value = Decimal(soup.find('charcode', text=cur_to).find_next_sibling('value').string.replace(',','.'))
    elif cur_to == 'RUR':
        from_nominal = int(soup.find('charcode', text=cur_from).find_next_sibling('nominal').string)
        from_value = Decimal(soup.find('charcode', text=cur_from).find_next_sibling('value').string.replace(',','.'))
    else:
        from_nominal = int(soup.find('charcode', text=cur_from).find_next_sibling('nominal').string)
        from_value = Decimal(soup.find('charcode', text=cur_from).find_next_sibling('value').string.replace(',','.'))
        to_nominal = int(soup.find('charcode', text=cur_to).find_next_sibling('nominal').string)
        to_value = Decimal(soup.find('charcode', text=cur_to).find_next_sibling('value').string.replace(',','.'))
        
    result = (amount * from_value / from_nominal) / (to_value / to_nominal)
    result= result.quantize(Decimal('.0001'))
    #result = Decimal('3754.8057')
    return result  # не забыть про округление до 4х знаков после запятой

