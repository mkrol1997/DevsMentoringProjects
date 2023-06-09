"""
W bazach danych, pod pojęciem ACID określa się cztery cechy definiujące operacje transakcji.
W odnieśeniu do tych zasad, odpowiednio zdefiniowany Context Manager posiada właściwości
transakcji. W sytuacji nawiązania połączenia z bazą danych za pomocą context managera
przy użyciu słowa “with”,  wszystkie  zapytania zawarte w kontekście, będą traktowane
jako zbiór zapytań wykonywanych w ramach transakcji. Oznacza to, że w zmiany w bazie danych zostaną
wprowadzone tylko i wyłącznie w momencie, w którym żadne z zapytań wykonywanych w ramach połączenia
nie spowodowuje wystąpienia błędu - następuje commit założonych zmian. W przeciwnym wypadku, następuje
rollback, czyli zmiany wprowadzone przez zapytania wykonane w ramach połączenia z bazą danych
do momentu wystąpienia błedu zostają cofnięte. Aby Context Manager używany do
pracy z bazami danych posiadał w/w właściwości, należy zdefiniować dwie metody dla
klasy bazy danych np. z użyciem biblioteki sqlite3: __enter__ oraz __exit__ w poniższy sposób:
"""
import sqlite3

class Database:
    def __init__(self, path: str) -> None:
        self.con = sqlite3.connect(path)

    def __enter__(self):
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()

        self.con.close()
