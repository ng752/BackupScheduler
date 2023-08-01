import shutil
import os
import time

def backup_files(source_path='test', destination_path='test_backup', interval=3600):
    while True:
        try:
            # Check if the source directory exists
            if not os.path.exists(source_path):
                print("Error: The specified source directory does not exist.")
                return

            # Copy files to destination directory
            shutil.copytree(source_path, destination_path)

            print(f"Backup successful: {source_path} -> {destination_path}")
        except Exception as e:
            print(f"Error during backup: {e}")

        time.sleep(interval)

if __name__ == "__main__":
    print("Welcome to the Simple Backup Tool!")

    # Input source path
    source_directory = input("Enter the path of the source directory to backup: ").strip()

    # Input destination path (external storage device)
    destination_directory = input("Enter the path of the destination directory (external storage device): ").strip()

    # Input backup interval in seconds
    backup_interval_seconds = int(input("Enter the backup interval in seconds (e.g., 3600 for 1 hour): "))

    # Schedule the backup
    backup_files(source_directory, destination_directory, backup_interval_seconds)
