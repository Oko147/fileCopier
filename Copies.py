import PySimpleGUI as sg
import shutil
import os
import socket



def copy_files(src_file, dest_folder, num_copies, revision):
    base_name, extension = os.path.splitext(src_file)
    file_name = os.path.basename(src_file)
    file_parts = file_name.split('-')

    for i in range(1, num_copies + 1):
        new_file_name = f"{file_parts[0]}-{i:02}-{revision}{extension}"
        shutil.copy(src_file, os.path.join(dest_folder, new_file_name))


def main():
    sg.theme('DarkAmber')

    layout = [
        [sg.Text('Select a file to copy:'), sg.InputText(key='file_path'), sg.FileBrowse(button_color=('#000', '#d3d3d3'))],
        [sg.Text('Destination folder:'), sg.InputText(key='dest_folder'), sg.FolderBrowse(button_color=('#000', '#d3d3d3'))],
        [sg.Text('Number of copies to create:'), sg.InputText(key='num_copies', size=(3, 1))],
        [sg.Text('Revision number (e.g., B04):'), sg.InputText(key='revision', size=(5, 1))],
        [sg.Button('Copy Files', button_color=('#fff', '#147147')), sg.Button('Exit', button_color=('#fff', '#FF6347'))]
    ]

    window = sg.Window('File Copier', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Copy Files':
            src_file = values['file_path']
            dest_folder = values['dest_folder']
            num_copies = int(values['num_copies'])
            revision = values['revision']

            if os.path.isfile(src_file) and os.path.isdir(dest_folder):
                copy_files(src_file, dest_folder, num_copies, revision)
                sg.popup(f'{num_copies} copies created successfully in {dest_folder}!', title='Success')
            else:
                sg.popup('Please select a valid file and destination folder!', title='Error')

    window.close()


if __name__ == '__main__':
    main()
