import easygui
from isf_browser.sqlite_web import *

# very lazy file dialogue
path = easygui.fileopenbox(default='*.db')

if path:

    main_file(path)
