import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)

Print(' ')
while True:
    user_action = input('Type add, show, edit, delete or exit: ')
    user_action =user_action.strip()

    if user_action.startswith(('add')):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append((todo + '\n'))
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number  = number -1
            todos = functions.get_todos()

            new_todo = input('Enter net todo: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except IndexError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('delete'):
        try:
            number = int(user_action[6:])

            todos = functions.get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo {todo_to_remove} was removed from todos. '
            print(message)

        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith(('exit')):
        break
    else:
        print('command is not valid.')

print('Bye!') 





