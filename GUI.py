from functions import get_todos, write_todos
from PySimpleGUI import Window, Text, InputText, Button

label = Text('Type in a TODO:  ')

inputBox = InputText(tooltip='Enter TODO ')

addButton = Button('Add')

# In layout, every list is a row, so if we want to put different columns in a row, we put them in a list
window = Window('My TODO App', layout=[[label], [inputBox, addButton]])

# Opens the window, and waits till button clicked
window.read()


window.close()
