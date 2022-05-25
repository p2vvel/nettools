"""
ZADANIE 1

Napisz w funkcji check_ip() wyrazenie regularne, 
ktore bedzie sprawdzalo poprawnosc adresu IP, zakladamy, 
ze nie mozna wpisac zer wiodacych (tzn. np 013 zamiast 13)

Mozesz sprawdzic poprawnosc rozwiazania poprzez wpisanie w terminal:
pytest <sciezka_do_tego_pliku .py (z rozszerzeniem)>
"""
import re


def check_ip(ip_address: str) -> bool:
    # regex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    regex = r"" # tutaj wpisz wyrazenie regularne
    return re.match(regex, ip_address)


def test1():
    address = "000.0000.00.00"
    assert check_ip(address) is None

def test2():
    address = "192.168.1.1"
    assert check_ip(address) is not None

def test3():
    address = "912.456.123.123"
    assert check_ip(address) is None

def test4():
    address = "192.168.1.3"
    assert check_ip(address) is not None

def test5():
    address = "129.15.12.0"
    assert check_ip(address) is not None
    
