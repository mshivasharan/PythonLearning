import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip = 'Enter todo', key ='todo')
add_button = sg.Button('Add')

window = sg.Window('My To-Do App', 
                   layout=[[label], [input_box, add_button]], 
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == 'Add':
        todos = functions.get_todos()
        new_todos = values['todo'] + '\n'
        todos.append(new_todos)

        functions.write_todos(todos)
    else:
        break

window.close()