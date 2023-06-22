import streamlit as slt
import Functions

todos = Functions.get_todos()

def add_todo ():
    todo = slt.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions.write_todos(todos)


slt.title("My ToDo App")
slt.subheader("This is my ToDo App")
slt.write("This app is written in Python")

for index, todo in enumerate(todos):
    checkbox = slt.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del slt.session_state[todo]
        slt.experimental_rerun()



slt.text_input(label='', placeholder="Add a New Todo... ",
               on_change=add_todo, key="new_todo")