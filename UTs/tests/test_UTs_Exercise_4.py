import pytest
from UTs.Exercises.UTs_Exercise_4 import *
import UTs.Exercises.UTs_Exercise_4


def test_check_pos_should_raiseException_when_TodoListIsEmpty(mocker):
    mocker.patch.object(
        UTs.Exercises.UTs_Exercise_4,
        'todos',
        [])

    pos = 2
    with pytest.raises(Exception):
        check_pos(pos)


def test_check_pos_should_raiseException_when_pos_lowerThan_0(mocker):
    mocker.patch.object(
        UTs.Exercises.UTs_Exercise_4,
        'todos',
        ['noteOne', 'noteTwo'])

    pos = -2
    with pytest.raises(Exception):
        check_pos(pos)


@pytest.mark.exception_raise
def test_check_pos_should_raiseException_when_pos_greaterThan_todosLength(mocker):
    mocker.patch.object(
        UTs.Exercises.UTs_Exercise_4,
        'todos',
        ['noteOne', 'noteTwo'])

    pos = 2
    with pytest.raises(Exception):
        check_pos(pos)

    pos = 3
    with pytest.raises(Exception):
        check_pos(pos)


def test_add_todo_should_return_true_if_new_note_in_todos(mocker):
    mocker.patch.object(
        UTs.Exercises.UTs_Exercise_4,
        'todos',
        ['noteOne', 'noteTwo'])

    new_note = 'New TODO note'
    add_todo(new_note)

    assert new_note in UTs.Exercises.UTs_Exercise_4.todos

@pytest.mark.exception_raise
def test_should_raiseException_when_toRemoveNotePos_not_in_todos_range(mocker):
    mocker.patch.object(
        UTs.Exercises.UTs_Exercise_4,
        'todos',
        ['noteOne', 'noteTwo', 'noteThree'])

    with pytest.raises(Exception):
        remove_todo(100000)


def test_should_return_true_if_note_removed_from_todos(mocker):
    mocker.patch.object(
        UTs.Exercises.UTs_Exercise_4,
        'todos',
        ['noteOne', 'noteTwo', 'noteThree'])

    note_to_remove = 'noteTwo'
    pos = UTs.Exercises.UTs_Exercise_4.todos.index(note_to_remove)

    remove_todo(pos)
    assert note_to_remove not in UTs.Exercises.UTs_Exercise_4.todos


def test_should_return_True_when_editedNotePos_in_todos_range(mocker):
    mocker.patch.object(
        UTs.Exercises.UTs_Exercise_4,
        'todos',
        ['noteOne', 'noteTwo', 'noteThree'])

    edit_todo(0, 'EditedNoteOne')
    assert 'EditedNoteOne' in UTs.Exercises.UTs_Exercise_4.todos

@pytest.mark.exception_raise
def test_should_raiseException_when_editedNotePos_not_in_todos_range(mocker):
    mocker.patch.object(
        UTs.Exercises.UTs_Exercise_4,
        'todos',
        ['noteOne', 'noteTwo', 'noteThree'])

    with pytest.raises(Exception):
        edit_todo(1000, 'EditedNoteOne')


def test_remove_all_should_returnTrue_when_todosLen_equalTo_0(mocker):
    mocker.patch.object(
        UTs.Exercises.UTs_Exercise_4,
        'todos',
        ["Clean my room", "Make my bed", "Go to school", "Do school homework"]
        )
    remove_all()
    assert len(UTs.Exercises.UTs_Exercise_4.todos) == 0
