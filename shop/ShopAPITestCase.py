from rest_framework.test import APITestCase


class ShopAPITestCase():
    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")                   # Cette méthode est un helper permettant de formater une date en chaine de caractères sous le même format que celui de l’api
