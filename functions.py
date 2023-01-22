FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Gets the content from the file """
    with open(filepath, 'r') as file_get:
        todos_from_file = file_get.readlines()

    return todos_from_file


def write_todos(new_todos, filepath=FILEPATH):
    """ Writes the context to the file """
    with open(filepath, 'w') as file_write:
        file_write.writelines(new_todos)


"""
When directly executing function.py, the variable __name__ would have value __main__ 
When executing CLI.py and comes here by the import statement, the variable __name__ would have value being 
the file's name, in this case: function
"""

if __name__ == '__main__':
    print('Directly executing function.py')

gasBoundary = 100
solidBoundary = 0


def get_water_state(temperature):
    if temperature >= gasBoundary:
        return 'Gas'
    elif temperature >= solidBoundary:
        return 'Liquid'
    else:
        return 'Solid'

