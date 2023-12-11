import PySimpleGUI as sg

def create_sticky_note():
    layout = [
        [sg.Multiline(default_text='', size=(30, 10), key='-NOTE-')],
        [sg.Button('Exit')]
    ]

    window = sg.Window('Sticky Note', layout, keep_on_top=True, no_titlebar=True, grab_anywhere=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()

if __name__ == '__main__':
    create_sticky_note()