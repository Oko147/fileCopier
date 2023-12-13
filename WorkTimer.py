import PySimpleGUI as sg
import datetime
import openpyxl


def update_time():
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    window['-DATE-'].update(current_date)

    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    window['-TIME-'].update(current_time)


layout = [
    [sg.Text(size=(100, 50), font=('Helvetica', 20), key='-DATE-')],
    [sg.Text(size=(100, 50), font=('Helvetica', 20), key='-TIME-')],
    [sg.Text(size=(200, 100), font=('Helvetica', 30), justification='center', key='-STOPWATCH-')],
    [sg.InputText(size=(40, 1), key='-TASK-')],
    [sg.Button('START', size=(100, 100), button_color=('#fff', '#147147'), key='-START-', disabled=True),
     sg.Button('STOP', size=(100, 100), button_color=('#fff', '#E60012'), key='-STOP-', disabled=True)]
]

window = sg.Window('Task Timer', layout, finalize=True)

start_time = None
stop_time = None
timer_running = False

while True:
    event, values = window.read(timeout=1000)

    if event == sg.WIN_CLOSED:
        break

    if event == '-TASK-':
        if values['-TASK-']:
            window['-START-'].update(disabled=False)

    if event == '-START-' and not timer_running:
        start_time = datetime.datetime.now().strftime("%H:%M")
        window['-START-'].update(disabled=True)
        window['-STOP-'].update(disabled=False)
        timer_running = True

    if event == '-STOP-' and timer_running:
        stop_time = datetime.datetime.now().strftime("%H:%M")
        timer_running = False
        window['-STOP-'].update(disabled=True)
        window['-START-'].update(disabled=True)

        # Save data to Excel
        filename = "ST - godziny.xlsx"
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook["Test"]

        data = [
            datetime.datetime.now().strftime("%d.%m.%Y"),
            values['-TASK-'],
            start_time,
            stop_time
        ]

        # Finding the first available cell without text
        row = 1
        while sheet[f'A{row}'].value is not None:
            row += 1

        # Writing data to cells
        for col, value in enumerate(data, start=1):
            sheet.cell(row, col).value = value

        workbook.save(filename)
        workbook.close()

        window['-TASK-'].update('')

    update_time()

window.close()