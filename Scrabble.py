import PySimpleGUI as sg

# Function to update the pool of letters
def update_pool(word, pool, letters_on_board):
    temp_pool = pool.copy()
    for letter in word.upper():
        if letter in temp_pool and letter not in letters_on_board:
            temp_pool.remove(letter)
        else:
            sg.popup(f'Warning: Letter {letter} not available in the pool!')
            return pool  # Revert pool if a letter isn't available
    return temp_pool

# Define the layout for the window
layout = [
    [sg.Text('Enter word to put on board:')],
    [sg.InputText(key='word_input'), sg.InputText(key='board_letters')],
    [sg.Text('Words on board:')],
    [sg.Listbox(values=[], size=(30, 6), key='word_list')],
    [sg.Text('Remaining letters in pool:', size=(30, 1))],
    [sg.Text('', size=(30, 6), key='remaining_letters')],
    [sg.Button('Add Word'), sg.Button('Exit')]
]

# Create the window
window = sg.Window('Scrabble Letter Pool Tracker', layout)

# Initialize the corrected letter pool (include Polish letters)
letter_pool = list("*" * 2 + "A" * 9 + "Ą" * 1 + "B" * 2 + "C" * 3 + "Ć" * 1 + "D" * 3 + "E" * 7 +
                   "Ę" * 1 + "F" * 1 + "G" * 2 + "H" * 2 + "I" * 8 + "J" * 2 + "K" * 3 + "L" * 6 +
                   "Ł" * 2 + "M" * 3 + "N" * 5 + "Ń" * 1 + "O" * 6 + "Ó" * 1 + "P" * 3 + "R" * 4 +
                   "S" * 3 + "Ś" * 1 + "T" * 3 + "U" * 2 + "W" * 4 + "Y" * 4 + "Z" * 5 + "Ź" * 1 +
                   "Ż" * 1)

word_list = []  # Store entered words

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Add Word':
        word = values['word_input']
        board_letters = values['board_letters']

        if word:
            updated_pool = update_pool(word, letter_pool, list(board_letters.upper()))
            if updated_pool != letter_pool:
                letter_pool = updated_pool
                window['remaining_letters'].update('|'.join(letter_pool))
                continue  # Skip adding word if letters are not available

            word_list.append(word)
            window['word_list'].update(values=word_list)
            # Update remaining letters
            letter_pool = update_pool(word, letter_pool, list(board_letters.upper()))
            window['remaining_letters'].update(', '.join(letter_pool))
            window['word_input'].update('')  # Clear the word input field
        else:
            sg.popup('Type the word!')

window.close()
