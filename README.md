# Map Dvorak Ctrl + shortcuts to QWERTY keycodes
A lot of the QWERTY `ctrl` `+` keyboard shortcuts are conveniently placed for easy use and become difficult to use in the Dvorak layout.

For example,  `ctrl + c` and `ctrl + v` requires both hands on the keyboard, or your left hand to be displaced to used the right `ctrl` key (in addition to building new muscle memory).

Assuming your keyboard is still labeled for QWERTY (and of course using the Dvorak layout), these mappings will map every physically labeled QWERTY key to their actual QWERTY keycode when pressed alongside `ctrl`.

Eg. Physically pressing the `ctrl` and `c` key on your keyboard will input `ctrl` and `j` to windows (via the dvorak layout).  `ctrl + j` will then be interpretted as `ctrl + c`.

## Requirements
Windows PowerToys (https://learn.microsoft.com/en-us/windows/powertoys/).

It's a pretty neat suite of features/hacks, one of them being a keyboard shortcut remapper.  I wasn't able to find a native way to do this in Windows (11) so a 3rd party application was needed.

## Installation
### Fresh installation
If you are new to Windows PowerToys and are installing it fresh (or you don't have any custom shortcuts already configured), then replace the  `C:/Users/USER_NAME/AppData/Local/Microsoft/PowerToys/Keyboard Manager/default.json'` file with the `default.json` file found here.

(Depending on how you installed PowerToys, the PowerToys application data may not be in the `AppData/Local/` directory).

### If you are already a PowerToys user
And you have keyboard shortcuts already set up, run the python script found in the `add_shortcuts/` directory to merge in the new shortcuts with your existing shortcuts.  

Preexisting shortcuts will not be touched and if there is a conflict it will be noted in the output.  Previous configuration file will also be backed up before modification.

(Depending on how you installed PowerToys, the PowerToys application data may not be in the `AppData/Local/` directory, please edit the script as necessary).
