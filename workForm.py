__author__ = 'Arkady.Babaev'

import PyForm
import wx
import os
import sqlite3 as lite

class dbcontrol:
    def __init__(self):
        self.__con = lite.connect("version.db")
        cur = self.__con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS VERSIONLINES ("
                   "VL_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                   "VL_VER STRING NOT NULL, "
                   "VL_DATE DATETIME DEFAULT(STRFTIME('%Y-%m-%d', 'NOW')), "
                   "VL_TYPE STRING NOT NULL, "
                   "VL_TEXT STRING);")

    def Commit(self):
        self.__con.commit()

    def AddLine(self, params):
        cur = self.__con.cursor()
        cur.execute("INSERT INTO VERSIONLINES (VL_VER, VL_TYPE, VL_TEXT) VALUES (?,?,?);", params)

    def GetLines(self):
        lines = []
        cur = self.__con.cursor()
        cur_ver = ""
        for row in cur.execute("SELECT * FROM VERSIONLINES ORDER BY VL_VER DESC;"): #ASC DESC
            if cur_ver != row[1]:
                lines.append("\n")
                lines.append("Version: " + unicode(row[1]) + " (" + unicode(row[2]) + "):\n")
            cur_ver = unicode(row[1])
            lines.append("    " + unicode(row[3]) + ": " + unicode(row[4]) + "\n")
        return lines

class Main (PyForm.MainFrame):
    def __init__(self, version_name):
        self.version_name = version_name
        PyForm.MainFrame.__init__(self, None)
        self.m_grid5.SetColLabelValue(0, "Type")
        self.m_grid5.SetColLabelValue(1, "Text")

    def OnTextEnterFunc( self, event ):
        self.AddingNewLine(event)


    def AcceptChanges( self, event ):
        db = dbcontrol()

        for row in range(0, self.m_grid5.GetNumberRows()):
            db.AddLine([unicode(self.version_name), unicode(self.m_grid5.GetCellValue(row, 0)),  unicode(self.m_grid5.GetCellValue(row, 1))])

        db.Commit()
        self.Close()

    def AbandonChanges( self, event ):
        self.Close()


    def AddingNewLine( self, event ):
        value = self.m_textCtrl3.GetValue()
        vtype = self.m_choice2.GetString(self.m_choice2.GetSelection())
        self.m_grid5.AppendRows(1)
        nRows = self.m_grid5.GetNumberRows()
        self.m_grid5.SetCellValue(nRows-1,0, vtype)
        self.m_grid5.SetCellValue(nRows-1,1, value)
        self.m_textCtrl3.SetValue('')
        self.m_grid5.ForceRefresh()

