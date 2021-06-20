from bs4 import BeautifulSoup
import unittest

def parse(path_to_file):    
    # Поместите ваш код здесь.
    # ВАЖНО!!!
    # При открытии файла, добавьте в функцию open необязательный параметр
    # encoding='utf-8', его отсутствие в коде будет вызвать падение вашего
    # решения на грейдере с ошибкой UnicodeDecodeError
    file = open(path_to_file, 'r', encoding="UTF-8")
    html = file.read()
    soup = BeautifulSoup(html, 'lxml')
    soup = soup.find(id="bodyContent")
    
    imgs = 0 #Количество картинок (img) с шириной (width) не меньше 200. 
    images = soup.find_all('img', width = True)
    for image in images:
        if int(image['width']) >= 200:
            imgs += 1

    headers = 0 #Количество заголовков (h1, h2, h3, h4, h5, h6), первая буква текста внутри которых соответствует заглавной букве E, T или C
    for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        if heading.text[0] in ["E", "T", "C"]:
            headers += 1

    linkslen = 0 #Длину максимальной последовательности ссылок, между которыми нет других тегов, открывающихся или закрывающихся
    links = soup.find_all('a')
    for link in links:
        l_siblings = link.find_next_siblings()
        len_arr = 1
        for sib in l_siblings:
                if sib.name == 'a':
                    len_arr+=1
                else:
                    break
        if len_arr > linkslen:
            linkslen = len_arr

    lists = 0 #Количество списков (ul, ol), не вложенных в другие списки.
    tags = soup.find_all(['ul', 'ol'])
    for tag in tags:
        if not tag.find_parents(['ul', 'ol']):
            lists += 1

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7])
            )

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()