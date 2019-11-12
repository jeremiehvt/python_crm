import requests

class Meteo(object):
    APPID = '43d45b6981ca6beef6f552c4ba738074'

    def __init__(self, city="rennes", country_code="fr"):
        self.payload = {'q': {city, country_code}, 'APPID': '43d45b6981ca6beef6f552c4ba738074'}

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, value):
        self.__payload = value

    def get_meteo(self):
        result = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'q': 'Rennes', 'APPID': '43d45b6981ca6beef6f552c4ba738074'})
        return result.json