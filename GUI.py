from functions import get_todos, write_todos
from PySimpleGUI import Window, Text, InputText, Button, Listbox, popup, WINDOW_CLOSED, TIMEOUT_EVENT
from time import strftime
from os import path


if not path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        # pass does nothing, just for syntax's sake
        pass


clock = Text('', key='clockText')
label = Text('Type in a TODO:  ')

inputBox = InputText(key='todo', tooltip='Enter TODO ')

addButton = Button(
    image_source='files/add.png',
    button_color='LightBlue',
    tooltip='Add TODO',
    key='Add'
)

todosList = Listbox(
    key='todoList',
    values=get_todos(),
    enable_events=True,
    size=(45, 10)
)

editButton = Button('Edit')

completeButton = Button(
    image_source='files/complete.png',
    key='Complete'
)

exitButton = Button('Exit')

layout = [
    [clock],
    [label],
    [inputBox, addButton],
    [todosList, editButton, completeButton],
    [exitButton]
]


# In layout, every list is a row, so if we want to put different columns in a row, we put them in a list
window = Window(
    'My TODO App',
    layout=layout,
    font=('Helvetica', 20)
)

while True:

    # Opens the window, and waits till button clicked, or timeout is reached
    event, values = window.read(timeout=500)

    window['clockText'].update(value=strftime('%b %d, %Y %H:%M:%S'))

    match event:
        case 'Add':
            todos = get_todos()

            newTodo = values['todo'] + '\n'
            todos.append(newTodo)

            write_todos(todos)
            window['todoList'].update(values=todos)
            window['todo'].update(value='')

        case 'Edit':
            try:
                selectedTodo = values['todoList'][0]

                newTodo = values['todo']
                todos = get_todos()
                todos[todos.index(selectedTodo)] = newTodo

                write_todos(todos)
                window['todoList'].update(values=todos)
            except IndexError:
                popup('Please select an item first.', font=('Helvetica', 20))

        case 'Complete':
            try:
                selectedTodo = values['todoList'][0]

                todos = get_todos()

                todos.remove(selectedTodo)

                write_todos(todos)
                window['todoList'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                popup('Please select an item first.', font=('Helvetica', 20))

        case 'todoList':
            window['todo'].update(value=values['todoList'][0])

        # Match looks like switch, but it isn't. These are hacks, called guards, to make it work
        case event if event == TIMEOUT_EVENT:
            continue

        case 'Exit':
            break

        case event if event == WINDOW_CLOSED:
            break

window.close()
