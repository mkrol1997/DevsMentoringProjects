from datetime import datetime


class Notebook:
    def __init__(self):
        self.notes = []

    def add_new_note(self, name, content):
        created_note = Note(name, content)
        self.notes.append(created_note)

    def add_note(self, note):
        self.notes.append(note)

    def count_notes(self):
        print(f'\nYou have {len(self.notes)} notes in your Notebook.')

    def print_all_notes(self):
        if len(self.notes) == 0:
            print("You don't have any notes. Notebook is empty!")
        else:
            print("\nHere are Your Notes: ")
            for index, note in enumerate(self.notes, 1):
                print(f"\t{index}. {note}")


class Note:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.date = datetime.now().strftime("%H:%M")

    def __repr__(self):
        return f'{self.name}: "{self.content}"'


def main():
    notebook = Notebook()
    notebook.print_all_notes()

    notebook.add_new_note('Bartek', 'Wake up at 6 AM')
    notebook.add_new_note('Kacper', 'Eat proper breakfast')
    notebook.add_new_note('Damian', 'Learn new language')

    new_note = Note('Kazimierz', 'Drink more water')
    notebook.add_note(new_note)

    notebook.add_new_note('Daniel', 'Study systematically')
    notebook.add_new_note('Władek', 'Learn to play chess')

    notebook.print_all_notes()
    notebook.count_notes()


if __name__ == "__main__":
    main()
