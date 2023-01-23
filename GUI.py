from functions import get_todos, write_todos
from PySimpleGUI import Window, Text, InputText, Button, WINDOW_CLOSED

label = Text('Type in a TODO:  ')

inputBox = InputText(tooltip='Enter TODO ', key='todo')

addButton = Button('Add')

# In layout, every list is a row, so if we want to put different columns in a row, we put them in a list
window = Window(
    'My TODO App',
    layout=[[label], [inputBox, addButton]],
    font=('Helvetica', 20)
)

while True:

    # Opens the window, and waits till button clicked
    event, values = window.read()

    match event:
        case 'Add':
            todos = get_todos()
            newTodo = values['todo'] + '\n'
            todos.append(newTodo)
            write_todos(todos)
        case WINDOW_CLOSED:
            break

window.close()
