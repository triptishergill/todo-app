import functions
import PySimpleGUI

label = PySimpleGUI.Text('Type in a to-do')
input_box = PySimpleGUI.InputText(tooltip='Enter a todo', key='todo')
add_button = PySimpleGUI.Button('Add')
list_box = PySimpleGUI.Listbox(values=functions.get_todos(), key='todos',
                               enable_events=True, size=[45, 10])
edit_button = PySimpleGUI.Button('Edit')

window = PySimpleGUI.Window('My To-Do App',
                            layout=[[label], [input_box, add_button],[list_box, edit_button]],
                            font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todos = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todos
            values['todos'] = todo_to_edit
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
