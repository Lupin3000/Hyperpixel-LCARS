from typing import Literal

import requests


class OpenWeather:
    """
    module class for Openweathermap.org API
    """

    def __init__(self,
                 apikey: str,
                 zipcode: int,
                 countrycode: str = None,
                 measurement: Literal['standard', 'metric', 'imperial'] = 'standard') -> None:
        """
        initialize class
        :param apikey: OpenWeather API key
        :param zipcode: zipcode as int
        :param countrycode: 2-letter country code (ISO3166)
        :param measurement: set metric ('standard', 'metric' or 'imperial')
        """
        self.apikey = str(apikey)
        self.zipcode = int(zipcode)
        self.countrycode = str(countrycode)
        self.measurement = str(measurement)

    @staticmethod
    def __get_measurement_units(measurement: str) -> tuple:
        """
        convert measurement into units
        :param measurement: measurement standard, metric or imperial
        :return: tuple of units and speed
        """
        if measurement == 'imperial':
            unit = u"\N{DEGREE SIGN}" + 'F'
            speed = 'm/h'
        elif measurement == 'metric':
            unit = u"\N{DEGREE SIGN}" + 'C'
            speed = 'm/s'
        else:
            unit = 'K'
            speed = 'm/s'

        return str(unit), str(speed)

    def get_values(self) -> dict:
        """
        send request to openweathermap.org
        :return: dictionary of weather metrics
        """
        weather = {
            'temperature': '',
            'pressure': '',
            'humidity': '',
            'wind': ''
        }

        zip_code = f'{self.zipcode},{self.countrycode}'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = dict(zip=zip_code, units=self.measurement, appid=self.apikey)
        response = requests.get(url, params)

        if response.status_code == 200 and 'application/json' in response.headers.get('Content-Type'):
            json_response = response.json()
            units = OpenWeather.__get_measurement_units(self.measurement)

            res_temperature = f"{json_response['main']['temp']} {units[0]}"
            res_pressure = f"{json_response['main']['pressure']} hPa"
            res_humidity = f"{json_response['main']['humidity']} %"
            res_wind = f"{json_response['wind']['speed']} {units[1]}"

            weather.update(temperature=res_temperature, pressure=res_pressure, humidity=res_humidity, wind=res_wind)

        return weather
