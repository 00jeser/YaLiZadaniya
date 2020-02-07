import sys
from io import BytesIO

import requests
from PIL import Image


def find(args):
    toponym_to_find = " ".join(sys.argv[1:])

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    size1 = toponym['boundedBy']['Envelope']['lowerCorner'].split()
    size2 = toponym['boundedBy']['Envelope']['upperCorner'].split()

    size = (str(float(size2[0]) - float(size1[0])), str(float(size2[1]) - float(size1[1])))


    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([*size]),
        "l": "map"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    return requests.get(map_api_server, params=map_params)
