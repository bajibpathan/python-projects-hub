import sys
import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit,
    QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog,
    QComboBox, QToolBar, QStatusBar, QMessageBox
)
from PyQt6.QtGui import QAction, QIcon


COURSES = ["Biology", "Math", "Astronomy", "Physics"]


# ---------------- DATABASE LAYER ----------------
class DatabaseConnection:
    """
    Handles all database interactions.
    """

    def __init__(self, database_file="database.db"):
        self.database_file = database_file

    def connect(self):
        return sqlite3.connect(self.database_file)

    def fetch_students(self):
        with self.connect() as conn:
            return conn.execute("SELECT * FROM students").fetchall()

    def insert_student(self, name, course, mobile):
        with self.connect() as conn:
            conn.execute(
                "INSERT INTO students(name, course, mobile) VALUES(?,?,?)",
                (name, course, mobile)
            )

    def update_student(self, student_id, name, course, mobile):
        with self.connect() as conn:
            conn.execute(
                "UPDATE students SET name=?, course=?, mobile=? WHERE id=?",
                (name, course, mobile, student_id)
            )

    def delete_student(self, student_id):
        with self.connect() as conn:
            conn.execute("DELETE FROM students WHERE id=?", (student_id,))


# ---------------- MAIN WINDOW ----------------
class MainWindow(QMainWindow):
    """
    Main GUI window.
    """

    def __init__(self):
        super().__init__()
        self.db = DatabaseConnection()

        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.setCentralWidget(self.table)

        self.create_menu()
        self.create_toolbar()

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.table.cellClicked.connect(self.show_action_buttons)

    def create_menu(self):
        file_menu = self.menuBar().addMenu("&File")
        edit_menu = self.menuBar().addMenu("&Edit")
        help_menu = self.menuBar().addMenu("&Help")

        self.add_action = QAction("Add Student", self)
        self.add_action.triggered.connect(self.insert)
        file_menu.addAction(self.add_action)

        self.search_action = QAction("Search", self)
        self.search_action.triggered.connect(self.search)
        edit_menu.addAction(self.search_action)

        about_action = QAction("About", self)
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.addAction(self.add_action)
        toolbar.addAction(self.search_action)

    def load_data(self):
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(self.db.fetch_students()):
            self.table.insertRow(row_number)
            for col, data in enumerate(row_data):
                self.table.setItem(row_number, col, QTableWidgetItem(str(data)))

    def show_action_buttons(self):
        if not hasattr(self, "edit_button"):
            self.edit_button = QPushButton("Edit")
            self.delete_button = QPushButton("Delete")

            self.edit_button.clicked.connect(self.edit)
            self.delete_button.clicked.connect(self.delete)

            self.status_bar.addWidget(self.edit_button)
            self.status_bar.addWidget(self.delete_button)

    def insert(self):
        InsertDialog(self).exec()

    def search(self):
        SearchDialog(self).exec()

    def edit(self):
        EditDialog(self).exec()

    def delete(self):
        DeleteDialog(self).exec()

    def about(self):
        QMessageBox.information(self, "About", "Student Management System using PyQt6 & SQLite.")


# ---------------- DIALOGS ----------------
class InsertDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.setWindowTitle("Register Student")
        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")

        self.course_name = QComboBox()
        self.course_name.addItems(COURSES)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")

        button = QPushButton("Register")
        button.clicked.connect(self.add_student)

        for w in (self.student_name, self.course_name, self.mobile, button):
            layout.addWidget(w)

        self.setLayout(layout)

    def add_student(self):
        name = self.student_name.text()
        mobile = self.mobile.text()
        course = self.course_name.currentText()

        if not name or not mobile:
            QMessageBox.warning(self, "Error", "All fields are required.")
            return

        self.parent.db.insert_student(name, course, mobile)
        self.parent.load_data()
        self.close()


class EditDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        index = parent.table.currentRow()
        if index < 0:
            QMessageBox.warning(parent, "Error", "Select a row first.")
            self.close()
            return

        self.student_id = parent.table.item(index, 0).text()

        layout = QVBoxLayout()

        self.student_name = QLineEdit(parent.table.item(index, 1).text())
        self.course_name = QComboBox()
        self.course_name.addItems(COURSES)
        self.course_name.setCurrentText(parent.table.item(index, 2).text())
        self.mobile = QLineEdit(parent.table.item(index, 3).text())

        button = QPushButton("Update")
        button.clicked.connect(self.update_student)

        for w in (self.student_name, self.course_name, self.mobile, button):
            layout.addWidget(w)

        self.setLayout(layout)

    def update_student(self):
        self.parent.db.update_student(
            self.student_id,
            self.student_name.text(),
            self.course_name.currentText(),
            self.mobile.text()
        )
        self.parent.load_data()
        self.close()


class DeleteDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        layout = QGridLayout()
        label = QLabel("Are you sure?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        yes.clicked.connect(self.delete_student)
        no.clicked.connect(self.close)

        layout.addWidget(label, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)

        self.setLayout(layout)

    def delete_student(self):
        index = self.parent.table.currentRow()
        if index < 0:
            return

        student_id = self.parent.table.item(index, 0).text()
        self.parent.db.delete_student(student_id)
        self.parent.load_data()
        self.close()


class SearchDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        layout = QVBoxLayout()
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")

        button = QPushButton("Search")
        button.clicked.connect(self.search)

        layout.addWidget(self.student_name)
        layout.addWidget(button)
        self.setLayout(layout)

    def search(self):
        name = self.student_name.text()
        items = self.parent.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            self.parent.table.selectRow(item.row())


# ---------------- RUN APP ----------------
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
