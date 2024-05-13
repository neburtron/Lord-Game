import tkinter as tk					 
from tkinter import ttk 
import commands
import json
import os
import shutil

# Not Final
# I'm going to play around with the settings + update llm_interface.py
# When that's done I'll change the read me and you'll be able to change settings with this thing.
# gets settings from Settings/OpenAI.json + Settings/HuggingFace.json, edit those docs to change what settings are given.
# API selected by last open tab, kept in Settings/last_tab_index.txt

SETTINGS_FOLDER = "Settings"

OpenAI_Settings = None
HuggingFace_Settings = None
tabControl = None

OpenAI_Settings = commands.load(os.path.join(SETTINGS_FOLDER, "OpenAI.json"))
HuggingFace_Settings = commands.load(os.path.join(SETTINGS_FOLDER, "HuggingFace.json"))



def save_tab_index(tab_index):
    with open(os.path.join(SETTINGS_FOLDER, "last_tab_index.txt"), "w") as file:
        file.write(str(tab_index))

def load_last_tab_index():
    try:
        with open(os.path.join(SETTINGS_FOLDER, "last_tab_index.txt"), "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def save_settings(model_settings, settings_file):
    try:
        with open(settings_file, "w") as file:
            json.dump(model_settings, file, indent=4)
    except:
        print("failed when trying to save")
    else:
        print("Settings saved:", model_settings)

def create_settings_widgets(frame, model_settings, settings_file):
    row = 1
    entry_vars = {}
    for setting, value in model_settings.items():
        ttk.Label(frame, text=setting).grid(column=0, row=row, padx=5, pady=5)
        entry_var = tk.StringVar(value=value)
        entry_vars[setting] = entry_var
        ttk.Entry(frame, textvariable=entry_var).grid(column=1, row=row, padx=5, pady=5)
        row += 1

    save_button = ttk.Button(frame, text="Save", command=lambda: save_settings({setting: entry_var.get() for setting, entry_var in entry_vars.items()}, settings_file))
    save_button.grid(column=0, row=row, columnspan=2, pady=10)


def on_tab_changed(event):

    global tabControl
    selected_tab_index = tabControl.index("current")
    save_tab_index(selected_tab_index)


def run_llm_settings():
    # Function to duplicate JSON template if not found
    def duplicate_json_template(src, dest):
        shutil.copyfile(src, dest)

    try:
        with open(os.path.join(SETTINGS_FOLDER, "HuggingFace.json"), "r") as file:
            pass
    except FileNotFoundError:
        # Duplicate HuggingFaceTemplate.json
        duplicate_json_template(os.path.join(SETTINGS_FOLDER, "HuggingFaceTemplate.json"), os.path.join(SETTINGS_FOLDER, "HuggingFace.json"))

    try:
        with open(os.path.join(SETTINGS_FOLDER, "OpenAI.json"), "r") as file:
            pass
    except FileNotFoundError:
        # Duplicate OpenAITemplate.json
        duplicate_json_template(os.path.join(SETTINGS_FOLDER, "OpenAITemplate.json"), os.path.join(SETTINGS_FOLDER, "OpenAI.json"))
    
    try:
        with open(os.path.join(SETTINGS_FOLDER, "last_tab_index.txt"), "r") as file:
            pass
    except FileNotFoundError:
        with open("last_tab_index.txt", "w") as file:
            file.write("0")

    global OpenAI_Settings
    global HuggingFace_Settings
    global tabControl
    
    root = tk.Tk()
    root.title("Tab Widget")
    root.minsize(height=500, width=500)
    root.geometry("500x500")

    label = ttk.Label(root, text="Edit LLM Settings \n\n\n Select tab of API you want to use. \n For OpenAI, base URL should be left blank if you are using their official servers. \n")
    label.pack(pady=10)

    tabControl = ttk.Notebook(root)
    tabControl.bind("<<NotebookTabChanged>>", on_tab_changed)

    OpenAI = ttk.Frame(tabControl)
    HuggingFace = ttk.Frame(tabControl)

    tabControl.add(OpenAI, text='OpenAI')
    tabControl.add(HuggingFace, text='HuggingFace')
    tabControl.pack(expand=1, fill="both")

    last_tab_index = load_last_tab_index()
    tabControl.select(last_tab_index)

    # Load settings after creating files
    OpenAI_Settings = commands.load(os.path.join(SETTINGS_FOLDER, "OpenAI.json"))
    HuggingFace_Settings = commands.load(os.path.join(SETTINGS_FOLDER, "HuggingFace.json"))

    ttk.Label(OpenAI, text="OpenAI").grid(column=0, row=0, padx=30, pady=30)
    create_settings_widgets(OpenAI, OpenAI_Settings, os.path.join(SETTINGS_FOLDER, "OpenAI.json"))

    ttk.Label(HuggingFace, text="HuggingFace").grid(column=0, row=0, padx=30, pady=30)
    create_settings_widgets(HuggingFace, HuggingFace_Settings, os.path.join(SETTINGS_FOLDER, "HuggingFace.json"))

    root.mainloop()

if __name__ == "__main__":
    run_llm_settings()