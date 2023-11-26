import functions
import PySimpleGUI

label = PySimpleGUI.Text('Type in a to-do')
input_box = PySimpleGUI.InputText(tooltip='Enter a todo', key='todo')
add_button = PySimpleGUI.Button('Add')
window = PySimpleGUI.Window('My To-Do App',
                            layout=[[label], [input_box, add_button]],
                            font=('Helvetica', 20))

while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case PySimpleGUI.WIN_CLOSED:
            break


window.close()
