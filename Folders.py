import os
import tkinter as tk
from tkinter import filedialog

def browse_path():
    folder_selected = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_selected)

def create_folders():
    path = path_entry.get()
    num_folders = int(num_entry.get())

    if os.path.exists(path):
        for i in range(1, num_folders + 1):
            folder_name = f"{i:02d}" if i < 10 else str(i)
            folder_path = os.path.join(path, folder_name)
            os.makedirs(folder_path)
        print(f"{num_folders} folders created at {path}")
    else:
        print("Invalid path. Please enter a valid path.")

root = tk.Tk()
root.title('Folder Creator')

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

path_label = tk.Label(frame, text='Selected path for folders:')
path_label.grid(row=0, column=0, sticky='w')

path_entry = tk.Entry(frame, width=50)
path_entry.grid(row=0, column=1, padx=5)

browse_button = tk.Button(frame, text='Browse', command=browse_path)
browse_button.grid(row=0, column=2, padx=5)

num_label = tk.Label(frame, text='Enter number of folders:')
num_label.grid(row=1, column=0, sticky='w')

num_entry = tk.Entry(frame, width=10)
num_entry.grid(row=1, column=1, padx=5)

create_button = tk.Button(frame, text='Create Folders', command=create_folders)
create_button.grid(row=2, columnspan=3, pady=10)

root.mainloop()
