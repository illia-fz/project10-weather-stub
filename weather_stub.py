WEATHER = {
    'Kharkiv': 'Sunny, 25°C',
    'Kyiv': 'Partly cloudy, 22°C',
    'London': 'Rainy, 15°C',
}
if __name__ == '__main__':
    city = input('Enter a city name: ').strip()
    print(WEATHER.get(city, 'Weather data not available.'))
