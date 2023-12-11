import os
import PySimpleGUI as sg

def create_folders(values):
    path = values['-FOLDER_PATH-']
    num_folders = values['-NUM_FOLDERS-']
    try:
        num_folders = int(num_folders)
        for i in range(1, num_folders + 1):
            folder_name = f"{i:02d}" if i < 10 else str(i)
            folder_path = os.path.join(path, folder_name)
            os.makedirs(folder_path)
        sg.popup(f"{num_folders} folders created successfully!", title='Success', keep_on_top=True)
    except ValueError:
        sg.popup_error("Please enter a valid number", title='Error', keep_on_top=True)

# GUI layout with improved design
sg.theme('LightGrey1')

layout = [
    [sg.Text('Folder Path:', font=('Arial', 12)), sg.InputText(key='-FOLDER_PATH-', size=(30, 1)), sg.FolderBrowse()],
    [sg.Text('Number of Folders:', font=('Arial', 12)), sg.InputText(key='-NUM_FOLDERS-', size=(10, 1))],
    [sg.Button('Create Folders', size=(15, 1), button_color=('white', '#147147'), border_width=2, key='-CREATE-')],
    [sg.Button('Exit', size=(10, 1), button_color=('white', '#FF5733'), border_width=2)]
]

window = sg.Window('Folder Creator', layout, element_justification='c', margins=(20, 20))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == '-CREATE-':
        create_folders(values)

window.close()
