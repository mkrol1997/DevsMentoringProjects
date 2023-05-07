from __future__ import annotations
from datetime import datetime


class Notebook:
    def __init__(self):
        self.notes = []

    def add_new_note(self, name: str, content: str) -> None:
        created_note = Note(name, content)
        self.notes.append(created_note)

    def add_note(self, note: Note) -> None:
        self.notes.append(note)

    def count_notes(self) -> None:
        print(f'\nYou have {len(self.notes)} notes in your Notebook.')

    def print_all_notes(self) -> None:
        if len(self.notes) == 0:
            print("You don't have any notes. Notebook is empty!")
        else:
            print("\nHere are Your Notes: ")
            for index, note in enumerate(self.notes, 1):
                print(f"\t{index}. {note}")


class Note:
    def __init__(self, name, content) -> None:
        self.name = name
        self.content = content
        self.date = datetime.now().strftime("%H:%M")

    def __str__(self) -> str:
        return f'{self.name}: "{self.content}"'


def main():
    notebook = Notebook()
    notebook.print_all_notes()

    notebook.add_new_note('Joey', 'Wake up at 6 AM')

    new_note = Note('Chandler', 'Drink more water')
    notebook.add_note(new_note)

    notebook.print_all_notes()
    notebook.count_notes()


if __name__ == "__main__":
    main()
