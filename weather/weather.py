import pyowm

print("Введите \"stop\" для выхода!")
while True:
    try:
        city = input("Какой город вас интересует?: ")
        if city == 'stop':
            break
        else:
            owm = pyowm.OWM('a99967bc9ee70d5b4bd387902982f400', language="RU")
            observation = owm.weather_at_place(city)
            w = observation.get_weather()

            temperature = w.get_temperature('celsius')['temp']

            print("В городе " + city + " сейчас температура: " + str(temperature) + " по Цельсию.")
            print('Погода в указаном городе: ' + w.get_detailed_status())
    except:
        print("Что-то пошло не так")
