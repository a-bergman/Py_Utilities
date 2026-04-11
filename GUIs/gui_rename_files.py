import sys
from PyQt6.QtWidgets import  QApplication, QWidget, QPushButton, QLabel,QVBoxLayout, QHBoxLayout, QLineEdit, QFileDialog, QMessageBox, QFormLayout, QGroupBox, QComboBox

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

        # GUI Layout

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

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(group)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.run_btn)

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

        main_layout.addLayout(theme_layout)
        main_layout.addWidget(group)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.run_btn)

        self.setLayout(main_layout)

        # Set default theme
        self.change_theme("VSC_Dark")

        # Styling
        self.setStyleSheet("""
            QWidget {font-size: 14px;}
            QLineEdit {padding: 6px; border: 1px solid #ccc; border-radius: 6px;}
            QPushButton {padding: 6px 12px; border-radius: 6px; background-color: #4a90e2; color: white;}
            QPushButton:hover {background-color: #357abd;}
            QGroupBox {font-weight: bold; border: 1px solid #ddd; border-radius: 8px; margin-top: 10px; padding: 10px;}
            QGroupBox::title {subcontrol-origin: margin; left: 10px;padding: 0 5px;}
        """)

    def get_themes(self):
        return {
            "Light": """
                QWidget { background-color: #f5f5f5; color: #000; }
                QLineEdit {padding: 6px; border: 1px solid #ccc; border-radius: 6px; background: white;}
                QPushButton {padding: 6px 12px; border-radius: 6px; background-color: #4a90e2; color: white;}
                QPushButton:hover {background-color: #357abd;}
            """,
            "Dark": """
                QWidget { background-color: #2b2b2b; color: #f0f0f0; }
                QLineEdit {padding: 6px; border: 1px solid #555; border-radius: 6px; background: #3c3c3c; color: white;}
                QPushButton {padding: 6px 12px; border-radius: 6px; background-color: #6a9fb5; color: white;}
                QPushButton:hover {background-color: #5a8fa5;}
            """,
            "VSC_Dark" : """
                QWidget {background-color: #1e1e1e; color: #d4d4d4; font-family: Segoe UI, Arial; font-size: 13px;}
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

        if not file.endswith(".csv"):
            print("Invalid file! Please select a .csv")
            return
        print("Processing:", file)


# Run app
app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())