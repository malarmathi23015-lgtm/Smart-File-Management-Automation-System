from modules.organizer import organize_files
from modules.renamer import rename_files
from modules.duplicate_remover import remove_duplicates
from modules.backup_manager import backup_files
from modules.cleaner import remove_empty_folders
from modules.report_generator import generate_report

def main():

    while True:

        print("\n===== SMART FILE MANAGER =====")
        print("1. Organize Files")
        print("2. Rename Files")
        print("3. Remove Duplicate Files")
        print("4. Backup Files")
        print("5. Remove Empty Folders")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter folder path: ")
            organize_files(path)

        elif choice == "2":
            path = input("Enter folder path: ")
            prefix = input("Enter file prefix: ")
            rename_files(path, prefix)

        elif choice == "3":
            path = input("Enter folder path: ")
            remove_duplicates(path)

        elif choice == "4":
            path = input("Enter source folder path: ")
            backup_files(path)

        elif choice == "5":
            path = input("Enter folder path: ")
            remove_empty_folders(path)

        elif choice == "6":
            generate_report()

        elif choice == "7":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()