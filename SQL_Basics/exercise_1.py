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


    def create_table(self) -> None:
        query = "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, " \
                "name TEXT NOT NULL, surname TEXT NOT NULL, date_joined DATE NOT NULL);"
        self.con.execute(query)

    def add_to_customers(self, name: str, surname: str, date_joined: str) -> None:
        query = "INSERT INTO Customers(name, surname, date_joined) VALUES(?, ?, ?)"
        self.con.execute(query, (name, surname, date_joined))

    def preview_table(self, table_name: str) -> None:
        query = f"SELECT * FROM {table_name}"
        results = self.con.execute(query).fetchall()
        print(results)

    def update_customer_name(self, customer_id: int, name: str) -> None:
        query = f"UPDATE Customers SET name = ? WHERE id = ?"
        self.con.execute(query, (name, customer_id))

    def update_customer_surname(self, customer_id: int, surname: str) -> None:
        query = f"UPDATE Customers SET surname = ? WHERE id = ?"
        self.con.execute(query, (surname, customer_id))

    def update_customer_date_joined(self, customer_id: int, date_joined: str) -> None:
        query = "UPDATE Customers SET date_joined = ? WHERE id = ?"
        self.con.execute(query, (date_joined, customer_id))

    def remove_customer(self, customer_id):
        query = "DELETE FROM Customers WHERE id = ?"
        self.con.execute(query, (customer_id,))
