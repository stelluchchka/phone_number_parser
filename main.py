import requests
import re
import time

def extract_phone_numbers(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_text = response.text
        phone_numbers = re.findall(r'(?<!\d)(?:\+7|8)[-\s]?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}(?!\d)', html_text)
        phone_numbers_formated = []
        for number in phone_numbers:
            number = re.sub(r'\D', '', number)
            if number.startswith('+') or number.startswith('7'):
                number = '8' + number[1:]
            phone_numbers_formated.append(number)
        phone_numbers_formated_orig = set(phone_numbers_formated)
        return phone_numbers_formated_orig
    else:
        return None 

def tests():
    print(extract_phone_numbers("https://repetitors.info"))
    print(extract_phone_numbers("https://hands.ru/company/about/"))
    print(extract_phone_numbers("https://timeweb.cloud/tutorials/python/ochistka-veb-stranic-v-python-s-beautiful-soup"))

if __name__ == "__main__":
    start_time = time.time()
    tests()
    end_time = time.time()
    print('Elapsed time: ', end_time - start_time)