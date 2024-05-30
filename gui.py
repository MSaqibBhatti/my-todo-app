import read_and_write_function
import PySimpleGUI as PSG


label = PSG.Text("Add a Todo")
input_box = PSG.InputText()
button = PSG.Button("Add")

window = PSG.Window('Todo List App', [[label], [input_box, button]])
window.read()
window.close()
