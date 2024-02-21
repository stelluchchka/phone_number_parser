import requests
import re
import time

def extract_phone_numbers(urls):
    numbers_res = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            html_text = response.text
            phone_numbers = re.findall(r'(?<!\d)(?:\+7|8|7)[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}(?!\d)', html_text)
            phone_numbers_formated = []
            for number in phone_numbers:
                number = re.sub(r'\D', '', number)
                if number.startswith('+'):
                    number = '8' + number[2:]
                    phone_numbers_formated.append(number)
                else:
                    number = '8' + number[1:]
                    phone_numbers_formated.append(number)
            phone_numbers_formated_orig = set(phone_numbers_formated)
            numbers_res.append(phone_numbers_formated_orig)
    return numbers_res

def tests():
    urls = ["https://repetitors.info", "https://hands.ru/company/about"]
    print(extract_phone_numbers(urls))

if __name__ == "__main__":
    start_time = time.time()
    tests()
    end_time = time.time()
    print('Elapsed time: ', end_time - start_time)
