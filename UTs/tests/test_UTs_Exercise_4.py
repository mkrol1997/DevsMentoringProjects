import pytest
import UTs.Exercises.UTs_Exercise_4 as todo_app

def test_check_pos_should_raiseException_when_TodoListIsEmpty(mocker):
    mocker.patch('UTs.Exercises.UTs_Exercise_4.todos', [])
    pos = 2

    with pytest.raises(Exception):
        todo_app.check_pos(pos)


def test_check_pos_should_raiseException_when_pos_lowerThan_0(mocker):
    mocker.patch('UTs.Exercises.UTs_Exercise_4.todos', ['noteOne', 'noteTwo'])
    pos = -2

    with pytest.raises(Exception):
        todo_app.check_pos(pos)


@pytest.mark.exception_raise
@pytest.mark.parametrize('mocked_todos, pos', [(['noteOne', 'noteTwo'], 2), (['noteOne'], 7)])
def test_check_pos_should_raiseException_when_pos_greaterThan_todosLength(mocker, mocked_todos, pos):
    mocker.patch('UTs.Exercises.UTs_Exercise_4.todos', mocked_todos)

    with pytest.raises(Exception):
        todo_app.check_pos(pos)


def test_add_todo_should_return_true_if_new_note_in_todos(mocker):
    mocker.patch('UTs.Exercises.UTs_Exercise_4.todos', ['noteOne', 'noteTwo', 'noteThree'])

    new_note = 'New TODO note'
    todo_app.add_todo(new_note)

    assert new_note in todo_app.todos


@pytest.mark.exception_raise
def test_should_raiseException_when_toRemoveNotePos_not_in_todos_range(mocker):
    mocker.patch('UTs.Exercises.UTs_Exercise_4.todos', ['noteOne', 'noteTwo', 'noteThree'])

    with pytest.raises(Exception):
        todo_app.remove_todo(100000)


def test_should_return_true_if_note_removed_from_todos(mocker):
    mocker.patch('UTs.Exercises.UTs_Exercise_4.todos', ['noteOne', 'noteTwo', 'noteThree'])

    note_to_remove = 'noteTwo'
    pos = todo_app.todos.index(note_to_remove)
    todo_app.remove_todo(pos)

    assert note_to_remove not in todo_app.todos


def test_should_return_True_when_editedNotePos_in_todos_range(mocker):
    mocker.patch('UTs.Exercises.UTs_Exercise_4.todos', ['noteOne', 'noteTwo', 'noteThree'])

    todo_app.edit_todo(0, 'EditedNoteOne')

    assert 'EditedNoteOne' in todo_app.todos

@pytest.mark.exception_raise
def test_should_raiseException_when_editedNotePos_not_in_todos_range(mocker):
    mocker.patch('UTs.Exercises.UTs_Exercise_4.todos', ['noteOne', 'noteTwo', 'noteThree'])

    with pytest.raises(Exception):
        todo_app.edit_todo(1000, 'EditedNoteOne')


def test_remove_all_should_returnTrue_when_todosLen_equalTo_0(mocker):
    mocker.patch('UTs.Exercises.UTs_Exercise_4.todos',
                 ["Clean my room", "Make my bed", "Go to school"])

    todo_app.remove_all()

    actual = len(todo_app.todos)
    expected = 0

    assert actual == expected
