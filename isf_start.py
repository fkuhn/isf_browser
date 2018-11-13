import easygui
from isf_browser.sqlite_web import *

# very lazy file dialogue
path = easygui.fileopenbox()

print(path)
main_file(path)
