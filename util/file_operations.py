import os
import shutil
from PySide6.QtWidgets import QFileDialog, QMessageBox


class FileOperations:
    def __init__(self):
        self.backup_directory = ""

    def backup(self):
        source_path = os.path.expanduser("~\\AppData\\Roaming\\EldenRing")
        destination_path = QFileDialog.getExistingDirectory(None, "Select Backup Directory")
        if destination_path:
            self.backup_directory = destination_path
            try:
                for item in os.listdir(source_path):
                    src_item = os.path.join(source_path, item)
                    dst_item = os.path.join(destination_path, item)
                    if os.path.isdir(src_item):
                        shutil.copytree(src_item, dst_item, dirs_exist_ok=True)
                    else:
                        shutil.copy2(src_item, dst_item)
                QMessageBox.information(None, "Success", "Backup completed successfully!")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))

    def restore(self):
        if not self.backup_directory:
            QMessageBox.warning(None, "Warning", "No backup directory selected.")
            return
        source_path = self.backup_directory
        destination_path = os.path.expanduser("~\\AppData\\Roaming\\EldenRing")
        try:
            for item in os.listdir(source_path):
                src_item = os.path.join(source_path, item)
                dst_item = os.path.join(destination_path, item)
                if os.path.isdir(src_item):
                    shutil.copytree(src_item, dst_item, dirs_exist_ok=True)
                else:
                    shutil.copy2(src_item, dst_item)
            QMessageBox.information(None, "Success", "Restore completed successfully!")
        except Exception as e:
            QMessageBox.critical(None, "Error", str(e))
