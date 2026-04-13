import sys
import os
import py_rename_files
from PyQt6.QtWidgets import  QApplication, QWidget, QPushButton, QLabel,QVBoxLayout, QHBoxLayout, QLineEdit, QFileDialog, QMessageBox, QFormLayout, QGroupBox, QComboBox, QPlainTextEdit

user = "andrew.bergman"

class EmittingStream:
    def __init__(self, callback):
        self.callback = callback

    def write(self, text):
        if text.strip():  # ignore empty lines
            self.callback(text)

    def flush(self):
        pass

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select File and Directory")
        self.setGeometry(200, 200, 1000, 400)

        ### Widgets ###

        # Directory selection
        self.dir_label = QLabel("Select Directory: ")
        self.dir_input = QLineEdit()
        self.dir_btn = QPushButton("Browse Directories")
        self.dir_btn.clicked.connect(self.select_directory)

        # File name mapping file
        self.file_label = QLabel("Select A File: ")
        self.file_input = QLineEdit()
        self.file_btn = QPushButton("Browse Files")
        self.file_btn.clicked.connect(self.select_file)

        # Button to run py_rename_files.py
        self.run_btn = QPushButton("Run")
        self.run_btn.clicked.connect(self.run_script)

        # GUI output
        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        self.output.setPlaceholderText("")
        self.output.setMinimumHeight(250)

        # Clear output button
        self.clear_btn = QPushButton("Clear Terminal")
        self.clear_btn.clicked.connect(self.output.clear)

        # Directory row
        dir_layout = QHBoxLayout()
        dir_layout.addWidget(self.dir_input)
        dir_layout.addWidget(self.dir_btn)

        # File row
        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_input)
        file_layout.addWidget(self.file_btn)

        # Form layout (clean alignment)
        form_layout = QFormLayout()
        form_layout.addRow("Directory:", dir_layout)
        form_layout.addRow("CSV File:", file_layout)

        # Group box for structure
        group = QGroupBox("Input")
        group.setLayout(form_layout)

        # Themes
        self.themes = self.get_themes()

        # Theme Selector
        self.theme_selector = QComboBox()
        self.theme_selector.addItems(self.themes.keys())
        self.theme_selector.currentTextChanged.connect(self.change_theme)

        theme_layout = QHBoxLayout()
        theme_layout.addWidget(QLabel("Theme:"))
        theme_layout.addWidget(self.theme_selector)
        theme_layout.addStretch()  # pushes it left nicely

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(theme_layout)
        main_layout.addWidget(group)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.run_btn)
        main_layout.addWidget(self.output)
        main_layout.addWidget(self.clear_btn)

        self.setLayout(main_layout)

        # Set default theme
        self.change_theme("VSC_Dark")

        # GUI Styling
        self.setStyleSheet("""
            QWidget {font-size: 14px;}
            QLineEdit {padding: 6px; border: 1px solid #ccc; border-radius: 6px;}
            QPushButton {padding: 6px 12px; border-radius: 6px; background-color: #4a90e2; color: white;}
            QPushButton:hover {background-color: #357abd;}
            QGroupBox {font-weight: bold; border: 1px solid #ddd; border-radius: 8px; margin-top: 10px; padding: 10px;}
            QGroupBox::title {subcontrol-origin: margin; left: 10px;padding: 0 5px;}
            QPlainTextEdit {background-color: #1e1e1e; color: #d4d4d4; border: 1px solid #3c3c3c; border-radius: 6px; padding: 8px;}
        """)

        self.output.setStyleSheet("""
            QWidget {font-size: 12px; font-family: "Arial";}
            QPlainTextEdit {background-color: #1e1e1e; color: #d4d4d4; border: 1px solid #3c3c3c; border-radius: 6px; padding: 8px;}
        """)

    def get_themes(self):
        return {
            "Light": """
                QWidget {font-size: 14px; background-color: #f5f5f5; color: #000; font-family: "Arial";}
                QLineEdit {padding: 6px; border: 1px solid #ccc; border-radius: 6px; background: white;}
                QPushButton {padding: 6px 12px; border-radius: 6px; background-color: #4a90e2; color: white;}
                QPushButton:hover {background-color: #357abd;}
              
            """,
            "Dark": """
                QWidget {font-size: 14px; background-color: #2b2b2b; color: #f0f0f0; font-family: "Arial";}
                QLineEdit {padding: 6px; border: 1px solid #555; border-radius: 6px; background: #3c3c3c; color: white;}
                QPushButton {padding: 6px 12px; border-radius: 6px; background-color: #6a9fb5; color: white;}
                QPushButton:hover {background-color: #5a8fa5;}
            """,
            "VSC_Dark" : """
                QWidget {background-color: #1e1e1e; color: #d4d4d4; font-family: "Arial"; font-size: 14px;}
                QLineEdit, QTextEdit {background-color: #252526; border: 1px solid #3c3c3c; border-radius: 6px; padding: 6px; color: #d4d4d4;}
                QLineEdit:focus, QTextEdit:focus {border: 1px solid #007acc;}
                QPushButton {background-color: #0e639c; border: none; border-radius: 6px; padding: 6px 12px; color: white;}
                QPushButton:hover {background-color: #1177bb;}
                QPushButton:pressed {background-color: #094771;}
                QLabel {color: #cccccc;}
                QComboBox {background-color: #252526; border: 1px solid #3c3c3c; border-radius: 6px; padding: 5px;}
                QComboBox:hover {border: 1px solid #007acc;}
                QComboBox QAbstractItemView {background-color: #1e1e1e; border: 1px solid #3c3c3c; selection-background-color: #094771; selection-color: white;}
                QGroupBox {border: 1px solid #3c3c3c; border-radius: 8px; margin-top: 10px; padding: 10px; font-weight: bold;}
                QGroupBox::title {subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #cccccc;}
                QScrollBar:vertical {background: #2a2a2a; width: 10px; margin: 0px;}
                QScrollBar::handle:vertical {background: #3c3c3c; border-radius: 5px;}
                QScrollBar::handle:vertical:hover {background: #505050;}
                QToolTip {background-color: #252526; color: #d4d4d4; border: 1px solid #3c3c3c;}
            """
        }

    # Functions

    # Functions
    def log(self, message):
        self.output.appendPlainText(f"{message}")

    def change_theme(self, theme_name):
        theme = self.themes.get(theme_name, "")
        self.setStyleSheet(theme)

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error!")
        msg.exec()

    def select_directory(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.dir_input.setText(folder)

    def select_file(self):
        start_dir = self.dir_input.text() or ""

        file, _ = QFileDialog.getOpenFileName(self, "Select CSV File", start_dir, "CSV Files (*.csv)")

        if file:
            if not file.endswith(".csv"):
                self.show_error("Please select a valid CSV file.")
                return
            self.file_input.setText(file)

    def run_script(self):

        file = self.file_input.text()
        file_dir = self.dir_input.text()

        self.output.clear()

        if not file.endswith(".csv"):
            self.output(f"Invalid file: {file}! Please select a .CSV")
            return
        
        original_stdout = sys.stdout

        try:
            self.log("Python Script: rename_files()")
            self.log(f"User     : {user}")
            self.log(f"Directory: {file_dir}")
            self.log(f"Name File: {file} \n")
            self.log("~~~~~Beginning Script~~~~~")
            sys.stdout = EmittingStream(self.log)
            py_rename_files.rename_files(file_path = file_dir, name_csv = file)
            self.log("~~~~~Script Complete~~~~~")
        except Exception as ex:
            self.show_error(f"Error encountered: {str(ex)}")
        finally:
            sys.stdout = original_stdout
       

# Run app
app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())