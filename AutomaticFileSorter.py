# Imports
import tkinter as tk
from tkinter import filedialog
import os, shutil

# Author: Patrick Loeber
# Source: https://github.com/patrickloeber/python-fun/blob/master/file-organizing/file_organizing.py
# This portion of the code is adapted from Patrick Loeber and licensed under the MIT License

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

doc = (".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".txt", ".csv")

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_doc(file):
    return os.path.splitext(file)[1] in doc
# End of adapted code

def select_folder(inital_dir):
    """
    Select folder to be sorted and return the path
    :param inital_dir: The initial directory to start the file dialog
    :return: The path of the selected folder
    """
    try:
        # Create instance of tkinter and hide window
        root = tk.Tk()
        root.withdraw()

        # Ask user to select folder
        folder_selected = filedialog.askdirectory(initialdir=inital_dir)

        if folder_selected:
            print(f"Selected folder: {folder_selected}")
            return folder_selected
        else:
            print("No folder selected")
            return None
    except Exception as ex:
        print(f"An error occured: {ex}")
        return None

def main():
    try:
        # Select the folder to be sorted
        # Replace default path with the path of the folder you want, for example "C\Users\UserName\Downloads".
        path = select_folder(r"C:\Users\User\Downloads")
        print(f'Path: {path}')
        for (path, dirs, files) in os.walk(path):
            for file in files:
                # Extract the file extension 
                extension = os.path.splitext(file)[1]
                print(extension)

                if is_audio(file):
                    if not os.path.exists(path + '/audio'):
                        os.makedirs(path + '/audio')
                    shutil.move(path+ '/' + file, path + '/audio')

                if is_video(file):
                    if not os.path.exists(path + '/video'):
                        os.makedirs(path + '/video')
                    shutil.move(path + '/' + file, path + '/video')

                if is_image(file):  
                    if not os.path.exists(path + '/image'):
                        os.makedirs(path + '/image')
                    shutil.move(path + '/' + file, path + '/image')

                if is_doc(file):
                    if not os.path.exists(path + '/doc'):
                        os.makedirs(path + '/doc')
                    shutil.move(path + '/' + file, path + '/doc')
    except:
        print("An error occured")

if __name__ == "__main__":
    main()
