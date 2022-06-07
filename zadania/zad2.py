"""
Napisz widok, ktory na podstawie parametrow zwracanych w linku (GET),
bedzie  zwracal string w postaci np. "Kaczuszka ZuziaKaczuszka ZuziaKaczuszka Zuzia".
Występujące imię i liczba powtórzeń powinny zależeć od parametrów z linku

Mozesz sprawdzic poprawnosc rozwiazania poprzez wpisanie w terminal:
pytest <sciezka_do_tego_pliku .py (z rozszerzeniem)>
"""
from fastapi.testclient import TestClient
from fastapi import FastAPI

app = FastAPI()

# sciezka pod ktora powinien byc dostepny widok (nie zmieniaj jej)
@app.get("/hello/")
async def root():  # wpisz parametry, ich nazwy mozesz rozpoznac na podstawie testu znajdujacego sie ponizej 
    return "No zmien cos tutaj"


client = TestClient(app)

def test_zad2():
    name = "twoje_imie"
    for count in range(0, 4):
        response = client.get(f"/hello/?name={name}&count={count}")
        assert response.status_code == 200
        print(response.text)
        assert response.text.strip('"') == (f"Kaczuszka {name}" * count)