import os
import PySimpleGUI as sg


def batch_rename_files(folder_path, extension, new_number, num_files):
    file_list = os.listdir(folder_path)
    file_list.sort()  # Sorting the files to maintain order if needed

    count = 0
    for file_name in file_list:
        if file_name.endswith(f'.{extension}'):
            parts = file_name.split('-')
            if len(parts) == 2:
                old_xxxx_number = parts[0][-4:]  # Extracting the current 'xxxx' number
                old_count = parts[1].split('_')[0]  # Extracting the current count number

                new_name = f"{new_number:04d}-{old_count}_{count + 1:02d}.{extension}"
                old_file_path = os.path.join(folder_path, file_name)
                new_file_path = os.path.join(folder_path, new_name)
                os.rename(old_file_path, new_file_path)

                count += 1
                if count == num_files:
                    break


layout = [
    [sg.Text('Select Folder: '), sg.InputText(key='folder_path'), sg.FolderBrowse()],
    [sg.Text('File Extension: '), sg.InputText(key='extension')],
    [sg.Text("New 'xxxx' Number: "), sg.InputText(key='new_xxxx_number')],
    [sg.Text('Number of Files to Rename: '), sg.InputText(key='num_files')],
    [sg.Button('Rename Files')]
]

window = sg.Window('File Renamer').Layout(layout)

while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    elif event == 'Rename Files':
        folder_path = values['folder_path']
        extension = values['extension']
        new_xxxx_number = int(values['new_xxxx_number'])
        num_files_to_rename = int(values['num_files'])

        batch_rename_files(folder_path, extension, new_xxxx_number, num_files_to_rename)
        sg.popup('Files renamed successfully!')

window.Close()
