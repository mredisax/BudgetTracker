# BudgetApp

BudgetApp to aplikacja do zarządzania budżetem, która umożliwia śledzenie transakcji i kategorii związanych z budżetem domowym, firmowym itp.

## Funkcje

- Dodawanie i edycja transakcji związanych z budżetem
- Tworzenie i zarządzanie kategoriami transakcji
- Generowanie statystyk dotyczących budżetu
- Podział budżetu na różne typy (np. domowy, firmowy)

## Wymagania

Aby uruchomić aplikację BudgetApp, musisz mieć zainstalowane następujące oprogramowanie:

- Python 3.x
- Django 3.x

## Instalacja

1. Sklonuj repozytorium:

`git clone https://github.com/mredisax/budgetApp.git`

2. Przejdź do katalogu projektu:

`cd budgetApp`

3. Utwórz wirtualne środowisko
```
virtualenv env
source env/bin/activate
```

4. Zainstaluj zależności:

`pip install -r requirements.txt`

5. Uruchom migracje:

```
python manage.py migrate
python manage.py makemigrations
```

6. Uruchom serwer deweloperski:

`python manage.py runserver`

Aplikacja będzie dostępna pod adresem http://localhost:8000.

## Konfiguracja

1. Skonfiguruj ustawienia bazy danych w pliku `settings.py`.
2. Dostosuj pliki szablonów i statyczne do własnych potrzeb.


## Licencja

Ten projekt jest licencjonowany na podstawie licencji [MIT](https://opensource.org/licenses/MIT).
