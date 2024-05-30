""" Function to read the todo list from txt file """


def read_from_file(filepath='todos.txt'):
    with open(filepath, 'r') as filename:
        todos_from_function = filename.readlines()
        return todos_from_function


""" function to write todo list in the txt file """


def write_to_file(todos_list_from_file, filepath='todos.txt'):
    with open(filepath, 'w') as filename:
        filename.writelines(todos_list_from_file)