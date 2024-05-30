import read_and_write_function
import time


time_now = time.strftime("%b %d %Y, %H:%M:%S")
print(f"Time at this instant is {time_now}")

while True:
    user_data = input("Enter add, edit, delete, show or exit:")
    user_data = user_data.strip()


    if user_data.startswith('add'):
        todo = user_data[4:]

        todos = read_and_write_function.read_from_file()

        todos.append(todo + '\n')

        read_and_write_function.write_to_file(todos)



    elif user_data.startswith('edit'):
        try:
            todos = read_and_write_function.read_from_file()

            replaced_number = int(user_data[5:])
            replaced_item = input("Enter new item:") + "\n"
            todos[replaced_number-1] = replaced_item

            read_and_write_function.write_to_file(todos)

        except ValueError:
            print("you have value in wrong format")
            continue


    elif user_data.startswith('show'):
        todos = read_and_write_function.read_from_file()

        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            print(f"{index+1} - {item}")



    elif user_data.startswith('delete'):

        try:
            todos = read_and_write_function.read_from_file()
    
            to_delete_item = int(user_data[7:])
            todos.pop(to_delete_item-1)

            read_and_write_function.write_to_file(todos)

        except IndexError:
            for index, item in enumerate(todos):
                max_number_to_delete = index + 1
            print(f"Enter the value equal or less than {max_number_to_delete}")


    elif user_data.startswith('exit'):
        break


    else:
        print("You have entered a wrong command please enter the correct command")

print("Bye")
