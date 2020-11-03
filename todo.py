import PySimpleGUI as sg
from file import file_write,file_read
fname = 'file'
tasks = file_read(fname)
layout=[
    [sg.Text("Enter New Task " ),sg.InputText("",key="todo_item"),(sg.Button("ADD",key="add_save"))],
    [sg.Slider(orientation='horizontal',key='priority')],
    [sg.Listbox(tasks,size=(40,10),key='items')],
    [sg.Button("Delete"),sg.Button("Edit"),sg.Button("Exit")]
]
window=sg.Window("week1",layout)

while True:
    event,values=window.Read()
    if event=="add_save":
        tasks.sort()
        values['todo_item']=values['todo_item']+" = Priority:"+str(int(values['priority']))
        tasks.append(values['todo_item'])
        window.FindElement('add_save').Update("ADD")
        window.FindElement('items').Update(tasks)
        window.FindElement('todo_item').Update('')
        file_write(fname, tasks)

    elif event == "Delete":
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        file_write(fname, tasks)

    elif event == "Edit":
        edit_val = values["items"][0]
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('todo_item').Update(value=edit_val)
        window.FindElement('add_save').Update("Save")
        file_write(fname, tasks)

    elif event=="Exit":
        break
window.Close()

