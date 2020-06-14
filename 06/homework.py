import requests

from bs4 import BeautifulSoup

source = requests.get('https://ua.sinoptik.ua').text
# print(source)

soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

location = soup.find('h1', class_='isMain').text.lstrip()

# print(location)

for day in soup.find_all('div', class_='main '):

    day_name = day.find('p', class_='day-link').text
    # print(day_name)

    day_num = day.find('p', class_='date dateFree').text
    # print(day_num)

    month = day.find('p', class_='month').text
    # print(month)

    temperature_min = day.find('div', class_='temperature').find('div', class_='min').span.text
    # print(temperature_min)

    temperature_max = day.find('div', class_='temperature').find('div', class_='max').span.text
    # print(temperature_max)

    print(f'{day_name} {day_num} {month}: температура повітря коливатиметься в межах від {temperature_min} до {temperature_max}')