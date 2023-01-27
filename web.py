from streamlit import title, subheader, write, checkbox, text_input, session_state, _rerun
from functions import get_todos, write_todos


todos = get_todos()


def add_todo():
    new_todo = session_state['addTodoInput'] + '\n'
    todos.append(new_todo)
    write_todos(todos)


title('My TODO App')
subheader('As a practice project')
write('This app is to increase your productivity.')


for index, singleTodo in enumerate(todos):
    checkboxInstance = checkbox(singleTodo, key=singleTodo)

    if checkboxInstance:
        todos.pop(index)
        write_todos(todos)
        del session_state[singleTodo]
        _rerun()

text_input(
    label='Enter a TODO :',
    placeholder='Add new TODO...',
    # Pressing enter triggers on_change
    on_change=add_todo,
    key='addTodoInput'
)

