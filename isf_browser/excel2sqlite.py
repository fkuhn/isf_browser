#!/usr/bin/python

# snippets for excel to sqlite import

import sqlite3
import sys
import easygui
import pandas as pd

try:
    filename = easygui.fileopenbox(default='*.xlsx')
except:
    sys.stderr.write("\nKeine Datei gefunden.\nBitte Excel-Dateinamen angeben!\n\n")
    sys.exit()
    
#Name of Excel xlsx file. SQLite database will have the same name and extension .db
con=sqlite3.connect(filename+".db")
wb=pd.read_excel(filename, sheetname=None, header=1)

for sheet in wb: 
    wb[sheet].to_sql(sheet, con, index=False)

con.commit()
con.close()
