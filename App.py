# Import Libs
import sys, pyttsx3, PyPDF2
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from src.Main_UI import PA_Root
##################################################



class ROOT(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        ## Setting Up Our Ui:
        self.ui = PA_Root()
        self.ui.setupUi(self)
        
        ## Home Buttons
        ##----------- Home Page Index No: 0 ---------------##
        self.ui.stt.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.qtb.clicked.connect(self.quit_func)
        ## Action Page
        ##----------- Action Page Index No: 0 ---------------##
        self.ui.back_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.browse_btn.clicked.connect(self.openfilePDF)
        self.ui.stt_conv.clicked.connect(self.startConvertAction)
    
    def quit_func(self):
        self.close()
    
    def openfilePDF(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        dialog = QFileDialog()
        dialog.setWindowTitle("Open PDF File")
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter("PDF files (*.pdf);;Text Files (*.txt);;Word Files(*.docx)")
        dialog.setViewMode(QFileDialog.Detail)
        dialog.setOption(QFileDialog.Option.ShowDirsOnly, False)
        
        if dialog.exec():
            selected_files = dialog.selectedFiles()
            if selected_files:
                # Set the text of QLineEdit to the selected file's path
                self.ui.browse_txt.setText(selected_files[0])
                
    
    def startConvertAction(self):
        try:
            pdffileName = self.ui.browse_txt.text()
            pdfreader = PyPDF2.PdfReader(open(pdffileName, 'rb'))
            speaker = pyttsx3.init()
            
            
            for page_num in range(len(pdfreader.pages)):
                text = pdfreader.pages[page_num].extract_text()
                clean_text = text.strip().replace('\n', ' ')
                self.ui.status.setText("Status: Operation Is Over -- Status -> Done!")
                QMessageBox.information(QMessageBox(),"Extracted Text",f"{clean_text}")
            speaker.save_to_file(clean_text, 'AudioFile.mp3')
            speaker.runAndWait()
            speaker.stop()
            
            
        except FileNotFoundError:
            QMessageBox.critical(QMessageBox(),"ERROR","NO PDF FILE FOUND!! First Select One")

######################
# Runs The Whole App #
######################
if __name__ == "__main__":
    app = QApplication([])
    root = ROOT()
    root.show()
    sys.exit(app.exec())