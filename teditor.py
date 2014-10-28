#!/usr/bin/python3

import  sys
from PyQt5.QtCore import*
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Main (QMainWindow):
    def __init__(self, parent= None):
        QMainWindow.__init__(self, parent)
        self.filename = ""

        self.initUI()

    def initUI(self):

        self.text = QTextEdit(self)
        self.text.setTabStopWidth(33)
        self.setWindowIcon(QIcon("icons/icon.png"))
        self.text.cursorPositionChanged.connect(self.cursorPosition)
        self.setCentralWidget(self.text)
        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()

        self.statusbar = self.statusBar()

        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("writer")
    def new(self):
        spawn = Main(self)
        spawn.show()
    def open(self):
        # get file file and show ".writer" file
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', " . ", "(*.writer)")

        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())
    def save(self):
        if not self.filename:
            self.filename=QFileDialog.getOpenFileName(self, "save File")

        if not self.filename.endswith(".writer"):
            self.filename += ".writer"

        with open(self.filename, "wt") as file:
            file.write(self.text.toHtml())

    def preview(self):
        #open dialog
        preview = QPrintPreviewDialog()

        #if print is request open print dialog
        preview.paintRequest.connect(lambda p: self.text.print_(p))
        preview.exec_()

    def print(self):
        # open printing dialog

        dialog = QPrintDialog()

        if (dialog.exec_() == QDialog.Accepted):
            self.text.document().print_(dialog.printer())

    def bulletList(self):

        cursor = self.text.textCursor()

        # Insert bulleted list
        cursor.insertList(QTextListFormat.ListDisc)

    def numberList(self):

        cursor = self.text.textCursor()

        # Insert list with numbers
        cursor.insertList(QTextListFormat.ListDecimal)

    def cursorPosition(self):

        cursor = self.text.textCursor()

        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))

    def initToolbar(self):

        self.newAction = QAction(QIcon("icons/new.png"),"New",self)
        self.newAction.setStatusTip("New document")
        self.newAction.setShortcut("Ctrl +N")
        self.newAction.triggered.connect(self.new)

        self.openAction = QAction(QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open document")
        self.openAction.setShortcut("Ctrl + O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QAction(QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip("Open document")
        self.saveAction.setShortcut("Ctrl + S")
        self.saveAction.triggered.connect(self.save)

        self.printAction = QAction(QIcon("icons/print.png"), "Print document", self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("ctrl + P")
        self.printAction.triggered.connect(self.print)

        self.previewAction = QAction(QIcon("icons/preview.png"), "Preview page", self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.printAction.setShortcut("ctrl + Shift+ P")
        self.previewAction.triggered.connect(self.preview)


        self.cutAction= QAction(QIcon("icons/cut.png"),"Cut to clipboad", self)
        self.cutAction.setStatusTip("Copy and delete text from clipboad")
        self.cutAction.setShortcut("ctrl + x")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QAction(QIcon("icons/copy.png"), "Copy to clipboad",self)
        self.copyAction.setStatusTip("Copy text to clipboad")
        self.copyAction.setShortcut("ctrl + C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QAction(QIcon("icons/paste.png"), "Paste from clipboad",self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QAction(QIcon("icons/undo.png"), "Undo last action",self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QAction(QIcon("icons/redo.png"), "Redo last undone thing",self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        bulletAction = QAction(QIcon("icons/bullet.png"),"Insert bullet List",self)
        bulletAction.setStatusTip("Insert bullet list")
        bulletAction.setShortcut("Ctrl+Shift+B")
        bulletAction.triggered.connect(self.bulletList)

        numberedAction = QAction(QIcon("icons/number.png"),"Insert numbered List",self)
        numberedAction.setStatusTip("Insert numbered list")
        numberedAction.setShortcut("Ctrl+Shift+L")
        numberedAction.triggered.connect(self.numberList)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addAction(self.previewAction)
        self.toolbar.addAction(self.previewAction)
        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)
        self.toolbar.addAction(bulletAction)
        self.toolbar.addAction(numberedAction)



        self.toolbar.addSeparator()

        self.addToolBarBreak()






    def initFormatbar(self):
        self.formatbar = self.addToolBar("Format")

    def initMenubar(self):

        menubar = self.menuBar()
        file = menubar.addMenu("File")
        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)



        edit = menubar.addMenu("Edit")
        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)

        view = menubar.addMenu("View")



def main():
    app = QApplication([])
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
