from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_window import Ui_MainWindow
from dialog import Ui_Dialog
from stylesheets import main_style_sheet
from stylesheets import dialog_style_sheet

# we will create our own class for dialog
class Dialog(QDialog):
     def __init__(self, *args, **kwargs):
        super(QDialog, self).__init__(*args, **kwargs)

        # create an instance of UI Dialog
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # adding here the style sheet for the dialog box
        self.setStyleSheet(dialog_style_sheet)
    

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)

        # the following step is very import. this will create the UI. This method is implemented in the main_Window.py file
        self.setupUi(self)

        # Attaching the button of new task to that dialog box
        self.pushButton.clicked.connect(self.add_stuff)

        # we will create here two lists: one for finished tasks (done) and one for remaining tasks (undone)
        self.done = []
        self.undone = []

        # Now we will add the functionality of the Done button of the UI: its name is pushButton_3 in the main_window
        self.pushButton_3.clicked.connect(self.do_task)

        # Now we will add the functionality of the Undone button of the UI: its name is pushButton_2 in the main_window
        self.pushButton_2.clicked.connect(self.undo_task)

        # adding here the style sheet
        self.setStyleSheet(main_style_sheet)

    def add_stuff(self):
        dlg = Dialog()

        # here, we will add the functionality of the OK button which name is button box in dialog
        dlg.ui.buttonBox.accepted.connect(
            # we will connect it to the add_task function which will check in which list to add this input: in finished list or in remaining tasks list
            lambda: self.add_task(dlg.ui.new_task_input.text())
            )
        dlg.exec()

    #  function that will add task to the suitable list
    def add_task(self, user_input):
        # if the bool(user_input) will return True if the length of the user_input string is greater than zero. this is how bool works for strings
        if bool(user_input):
            self.remaining_list.addItem(user_input)

    # function that will take the selected item of the remaining list and will add to the Finished task list: currentRow = SELECTED ITEM WITH MOUSE
    def do_task(self):
        task = self.remaining_list.takeItem(self.remaining_list.currentRow())
        if bool(task):
            self.finished_list.addItem(task.text())

        
    # function that will take the selected item of the finished list and will add to the remaining task list: currentRow = SELECTED ITEM WITH MOUSE
    def undo_task(self):
        task = self.finished_list.takeItem(self.finished_list.currentRow())
        if bool(task):
            self.remaining_list.addItem(task.text())




# Performing execution
app = QApplication([])
window = MyWindow()
window.show()
app.exec() 