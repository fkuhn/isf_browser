#!/usr/bin/python

# snippets for excel to sqlite import

import sqlite3
import sys
import easygui
import pandas as pd


ftypes = ['db', 'sqlite']

okbut =easygui.msgbox('Excel zu SQLite Konverter.')
if okbut:

    try:

        filename = easygui.fileopenbox('Bitte Excel-Datei wählen', 'Excel Quelle', default='*.xlsx')

        savedb = easygui.filesavebox('Bitte Speicherort für SQlite Datei und ihren Namen wählen',
                                     'DB Speichern', default='*.db', filetypes="*.db")

    except:
        easygui.exceptionbox('\nKeine Datei gefunden.\nBitte Excel-Dateinamen angeben!\n\n')
        sys.stderr.write("\nKeine Datei gefunden.\nBitte Excel-Dateinamen angeben!\n\n")
        sys.exit()

    #Name of Excel xlsx file. SQLite database will have the same name and extension .db

    con=sqlite3.connect(savedb)
    wb=pd.read_excel(filename, header=1)

    for sheet in wb:
        wb[sheet].to_sql(sheet, con, index=False)

    con.commit()
    con.close()
