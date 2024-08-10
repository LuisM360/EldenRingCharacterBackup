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
            self.backup_directory = self.create_backup_folder(destination_path)
            try:
                for item in os.listdir(source_path):
                    src_item = os.path.join(source_path, item)
                    dst_item = os.path.join(self.backup_directory, item)
                    if os.path.isdir(src_item):
                        shutil.copytree(src_item, dst_item, dirs_exist_ok=True)
                    else:
                        shutil.copy2(src_item, dst_item)
                QMessageBox.information(None, "Success", "Backup completed successfully!")
            except Exception as e:
                QMessageBox.critical(None, "Error", str(e))

    def create_backup_folder(self, destination_path):
        existing_backups = [d for d in os.listdir(destination_path) if d.startswith('Backup') and d[6:].isdigit()]
        backup_numbers = [int(d[6:]) for d in existing_backups]
        next_backup_number = max(backup_numbers, default=0) + 1
        new_backup_folder = os.path.join(destination_path, f'Backup{next_backup_number}')
        os.makedirs(new_backup_folder)
        return new_backup_folder

    def restore(self, backup_directory):
        source_path = backup_directory
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
