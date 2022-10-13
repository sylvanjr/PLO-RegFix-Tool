import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QLabel, QCheckBox, QPushButton, QFileDialog, QListWidget, QTextEdit
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from bs4 import BeautifulSoup
import os
import datetime


class mainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # Load UI file
        uic.loadUi("mainWindow.ui", self)

        # Declare buttons
        self.button = self.findChild(QPushButton, "pbSelect")
        self.button2 = self.findChild(QPushButton, "pbRun")
        self.label = self.findChild(QLabel, "labelDisplay")
        self.list = self.findChild(QListWidget, "listWidget")
        self.checkbox = self.findChild(QCheckBox, "cbET")
        self.checkbox2 = self.findChild(QCheckBox, "cbPC")
        self.checkbox3 = self.findChild(QCheckBox, "cbSC")
        self.checkbox4 = self.findChild(QCheckBox, "cbWS")
        self.checkbox5 = self.findChild(QCheckBox, "cbTable")
        self.button3 = self.findChild(QPushButton, "pbSingle")
        self.button4 = self.findChild(QPushButton, "pbRemove")

        # Button click function
        self.pbSelect.clicked.connect(self.getFilename)
        self.pbRun.clicked.connect(self.cleanUp)
        self.pbSingle.clicked.connect(self.singleBtn)
        self.pbRemove.clicked.connect(self.removeSel)
        self.show()

    def removeSel(self):
        listItems = self.listWidget.selectedItems()
        if not listItems:
            return
        for item in listItems:
            self.listWidget.takeItem(self.listWidget.row(item))

    def cleanUp(self):

        for row in range(self.list.count()):
            file = self.list.item(row).text()

            with open(file) as f:
                contents = f.read()
                soup = BeautifulSoup(contents, 'xml')
                if self.cbET.isChecked():
                    for empTags in soup.find_all():
                        if (len(empTags.get_text(strip=True)) == 0):  # and (empTags.name not in whiteList):
                            empTags.extract()

                if self.cbPC.isChecked():
                    for pTags in soup.find_all('p'):
                        pTags.attrs.clear()
                        pTags.attrs["class"] = 'indent'

                if self.cbSC.isChecked():
                    for secTags in soup.find_all('section_content'):
                        if " (" in secTags['section']:
                            current = str(secTags['section'])
                            newVal = current.replace(" (", "(")
                            secTags['section'] = newVal

                if self.cbWS.isChecked():
                    for pTags in soup.find_all('p'):
                        currText = pTags.get_text()
                        newText = currText.split()
                        newText = ' '.join(newText)
                        a = currText.replace(currText, newText)
                        pTags.string = a

                if self.cbTable.isChecked():
                    for trTag in soup.find_all('tr'):
                        trTag.name = "p"

                    x = soup.prettify()
                    soup = BeautifulSoup(x, 'xml')

                    for pTags in soup.find_all('p'):
                        pTags.attrs["class"] = 'indent'

                    for tableTag in soup.find_all('table'):
                        tableTag.unwrap()

                    x = soup.prettify()
                    soup = BeautifulSoup(x, 'xml')

                    for tdTag in soup.find_all('td'):
                        tdTag.unwrap()

                    x = soup.prettify()
                    soup = BeautifulSoup(x, 'xml')

                    for empTags in soup.find_all():
                        if (len(empTags.get_text(strip=True)) == 0):  # and (empTags.name not in whiteList):
                            empTags.extract()

            x = soup.prettify()

            outDir = os.path.dirname(__file__)
            now = datetime.datetime.now()
            date = now.strftime('%m%d%y')
            newPath = os.path.join(r".\Output", date)

            checkFolder = os.path.isdir(newPath)
            if not checkFolder:
                os.mkdir(newPath)

            xmlFile = os.path.basename(file)
            file = os.path.join(newPath, xmlFile)
            with open(file, "w+") as f:
                f.write(str(x))

        msg = QMessageBox()

        msg.setIcon(QMessageBox.Information)

        msg.setWindowTitle(f"Success!")

        msg.setText("\nCleanup Done.\n")

        msg.exec()

    def printBtn(self):
        self.labelDisplay.setText("Clicked")

    def singleBtn(self):
        QMainWindow.hide(self)

        uic.loadUi("singleWindow.ui", self)


        self.button = self.findChild(QPushButton, "pbRun")
        #self.label = self.findChild(QLabel, "labelDisplay")
        self.text = self.findChild(QTextEdit, "textEdit")
        self.checkbox = self.findChild(QCheckBox, "cbET")
        self.checkbox2 = self.findChild(QCheckBox, "cbPC")
        self.checkbox3 = self.findChild(QCheckBox, "cbSC")
        self.checkbox4 = self.findChild(QCheckBox, "cbWS")
        self.checkbox5 = self.findChild(QCheckBox, "cbTable")
        self.button2 = self.findChild(QPushButton, "pbMultiple")

        self.pbMultiple.clicked.connect(self.multipleBtn)
        self.pbRun.clicked.connect(self.cleanText)

        self.show()

    def multipleBtn(self):
        QMainWindow.hide(self)
        uic.loadUi("mainWindow.ui", self)

        # Declare buttons
        self.button = self.findChild(QPushButton, "pbSelect")
        self.button2 = self.findChild(QPushButton, "pbRun")
        self.label = self.findChild(QLabel, "labelDisplay")
        self.list = self.findChild(QListWidget, "listWidget")
        self.checkbox = self.findChild(QCheckBox, "cbET")
        self.checkbox2 = self.findChild(QCheckBox, "cbPC")
        self.checkbox3 = self.findChild(QCheckBox, "cbSC")
        self.checkbox4 = self.findChild(QCheckBox, "cbWS")
        self.checkbox5 = self.findChild(QCheckBox, "cbTable")
        self.button3 = self.findChild(QPushButton, "pbSingle")
        self.button4 = self.findChild(QPushButton, "pbRemove")

        # Button click function
        self.pbSelect.clicked.connect(self.getFilename)
        self.pbRun.clicked.connect(self.cleanUp)
        self.pbSingle.clicked.connect(self.singleBtn)
        self.pbRemove.clicked.connect(self.removeSel)

        self.show()

    # Need correction
    def cleanText(self):
        xmlString = self.textEdit.toPlainText()
        print(xmlString)

        soup = BeautifulSoup(xmlString, 'html.parser')

        if self.cbET.isChecked():
            #print("checked")
            for empTags in soup.find_all():
                if (len(empTags.get_text(strip=True)) == 0):  # and (empTags.name not in whiteList):
                    empTags.extract()

        if self.cbPC.isChecked():
            for pTags in soup.find_all('p'):
                pTags.attrs.clear()
                pTags.attrs["class"] = 'indent'

        if self.cbSC.isChecked():
            for secTags in soup.find_all('section_content'):
                if " (" in secTags['section']:
                    current = str(secTags['section'])
                    newVal = current.replace(" (", "(")
                    secTags['section'] = newVal

        if self.cbWS.isChecked():
            for pTags in soup.find_all('p'):
                currText = pTags.get_text()
                newText = currText.split()
                newText = ' '.join(newText)
                a = currText.replace(currText, newText)
                pTags.string = a

        if self.cbTable.isChecked():
            for trTag in soup.find_all('tr'):
                trTag.name = "p"

            x = soup.prettify()
            soup = BeautifulSoup(x, 'xml')

            for pTags in soup.find_all('p'):
                pTags.attrs["class"] = 'indent'

            for tableTag in soup.find_all('table'):
                tableTag.unwrap()

            x = soup.prettify()
            soup = BeautifulSoup(x, 'xml')

            for tdTag in soup.find_all('td'):
                tdTag.unwrap()

            x = soup.prettify()
            soup = BeautifulSoup(x, 'xml')

            for empTags in soup.find_all():
                if (len(empTags.get_text(strip=True)) == 0):  # and (empTags.name not in whiteList):
                    empTags.extract()

        x = soup.prettify()

        self.textEdit.setPlainText(x)
        msg = QMessageBox()

        msg.setIcon(QMessageBox.Information)

        msg.setWindowTitle(f"Success!")

        msg.setText("\nCleanup Done.\n")

        msg.exec()

    def getFilename(self):
        fname = QFileDialog.getOpenFileNames(None, "Select XML File", "", "*.xml")
        print(fname)
        if fname[0]:
            for files in fname[0]:
                #fileName = files.split("/")[-1]
                self.listWidget.addItem(files)
                #self.listWidget.addItem(fileName)

        #fileName = fname[0].split("\\")[-1]
        #print(fileName)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = mainWindow()
    sys.exit(app.exec_())
