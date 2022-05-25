"""
ZADANIE 1

Napisz w funkcji check_ip() wyrazenie regularne, 
ktore bedzie sprawdzalo poprawnosc adresu IP, zakladamy, 
ze nie mozna wpisac zer wiodacych (tzn. np 013 zamiast 13)

Mozesz sprawdzic poprawnosc rozwiazania poprzez wpisanie w terminal:
python -m unittest zadania.test_zad1
"""
from unittest import TestCase
import re


def check_ip(ip_address: str) -> bool:
    # regex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    regex = r"" # tutaj wpisz wyrazenie regularne
    return re.match(regex, ip_address)


class TestZadanie1(TestCase):
    def test1(self):
        address = "000.0000.00.00"
        self.assertFalse(check_ip(address))
    
    def test2(self):
        address = "192.168.1.1"
        self.assertTrue(check_ip(address))

    def test3(self):
        address = "912.456.123.123"
        self.assertFalse(check_ip(address))

    def test4(self):
        address = "192.168.1.3"
        self.assertTrue(check_ip(address))

    def test5(self):
        address = "129.15.12.0"
        self.assertTrue(check_ip(address))
        
