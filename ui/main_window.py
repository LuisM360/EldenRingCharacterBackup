from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox
from util.file_operations import FileOperations


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_ops = FileOperations()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Elden Ring Backup and Restore")
        self.setGeometry(100, 100, 400, 200)
        layout = QVBoxLayout()

        # Backup button
        btn_backup = QPushButton("Backup Files", self)
        btn_backup.clicked.connect(self.file_ops.backup)
        layout.addWidget(btn_backup)

        # Restore button
        btn_restore = QPushButton("Restore Files", self)
        btn_restore.clicked.connect(self.file_ops.restore)
        layout.addWidget(btn_restore)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)