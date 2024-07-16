import glob
import os
import tkinter as tk
from tkinter import filedialog


def delete_exe_msi(directory: str) -> None:
    patterns = ['*.exe', '*.msi']
    for pattern in patterns:
        full_path = os.path.join(directory, pattern)
        for file in glob.glob(full_path):
            try:
                os.remove(file)
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")


def select_folder_and_delete_files() -> None:
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        delete_exe_msi(folder_selected)
    else:
        print("No folder selected.")


if __name__ == '__main__':
    select_folder_and_delete_files()
