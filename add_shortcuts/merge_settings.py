import os
import shutil
import json
import pprint
from datetime import datetime

### Constants ###
# File path of the PowerToys keyboard manager settings
CONFIG_FILE = f'C:/Users/{os.getlogin()}/AppData/Local/Microsoft/PowerToys/Keyboard Manager/default.json'
KEYCODE_DATA = 'win-keycode-data.json'
#################

def backup_file():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = f'{CONFIG_FILE}_{timestamp}'
    shutil.copy(CONFIG_FILE, backup_file)

def merge_settings():
    global_array = []
    # Construct list of shortcuts to be added
    shortcuts = []
    for char in data:
        shortcuts.append(f'17;{data[char]["keycode"]}')

    # Remove shortcuts combos that already exist
    for current in settings["remapShortcuts"]["global"]:
        if current["originalKeys"] in shortcuts:
            shortcuts.pop(shortcuts.index(current["originalKeys"]))

    # Build and add array of new remap shortcuts to current shortcuts
    for char in data:
        if f'17;{data[char]["keycode"]}' in shortcuts:
            remap = {"operationType": 0, "secondKeyOfChord": 0}
            dvorak_letter = data[char]["dvorak"]
            remap["newRemapKeys"] = f'17;{data[char]["keycode"]}'
            remap["originalKeys"] = f'17;{data[dvorak_letter]["keycode"]}'
            settings["remapShortcuts"]["global"].append(remap)
        else:
            print("Shortcut for Ctrl + " + char + " already exists. Skipping.")
    with open(CONFIG_FILE, 'w') as settings_file:
        json.dump(settings, settings_file, indent=4)

if __name__ == '__main__':
    try:
        with open(CONFIG_FILE) as settings_file:
            settings = json.load(settings_file)
            print(settings)
    except Exception as e:
        print(f'Failed to open config file at {CONFIG_FILE}: {e}')
        exit()

    # Load in keycode data
    try:
        with open(KEYCODE_DATA) as data:
            data = json.load(data)
    except Exception as e:
        print(f'Failed to load keycode data file from {KEYCODE_DATA}: {e}')
        exit()
    backup_file()
    merge_settings()