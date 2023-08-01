import shutil
import os
import time

def backup_files(source_path='test', destination_path='test_backup', interval=3600):
    while True:
        try:
            # Check if the source directory exists
            if not os.path.exists(source_path):
                print("Fehler: Das eingegebene Quellverzeichnis konnte nicht gefunden werden.")
                return

            # Copy files to destination directory
            shutil.copytree(source_path, destination_path)

            print(f"Sicherung erfolgreich: {source_path} -> {destination_path} ")
        except Exception as e:
            print(f"Fehler beim Backup: {e}")

        time.sleep(interval)

if __name__ == "__main__":
    print("Willkommen beim einfachen Backup-Tool!")

    # Input source path
    source_directory = input("Gib den Pfad des Quellverzeichnisses ein, das gesichert werden soll: ").strip()

    # Input destination path (external storage device)
    destination_directory = input("Gib den Pfad des Zielverzeichnisses (externes Speichergerät) ein: ").strip()

    # Input backup interval in seconds
    backup_interval_seconds = int(input("Gib das Sicherungsintervall in Sekunden ein (z. B. 3600 für 1 Stunde): "))

    # Schedule the backup
    backup_files(source_directory, destination_directory, backup_interval_seconds)
