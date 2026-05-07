# Smart File Management & Automation System

## Objective
This project automates file management tasks such as:
- Organizing files
- Renaming files
- Removing duplicate files
- Creating backups
- Removing empty folders
- Generating reports

---

# Features
- File Organizer
- Bulk File Renamer
- Duplicate File Remover
- Backup System
- Empty Folder Cleaner
- Logging System
- Report Generator
- Exception Handling

---

# Technologies Used
- Python
- OS Module
- Shutil
- Logging
- Hashlib
- Datetime

---

# Folder Structure

smart-file-management-system/
│
├── main.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── helper.py
│   ├── organizer.py
│   ├── renamer.py
│   ├── duplicate_remover.py
│   ├── backup_manager.py
│   ├── cleaner.py
│   └── report_generator.py
│
├── logs/
│   └── operations.log
│
├── reports/
│   └── report.txt
│
├── backup/
│
├── test_files/
│
└── screenshots/

---

# Modules Description

## organizer.py
Organizes files into categories like:
- Images
- Documents
- Videos
- Music

## renamer.py
Renames files automatically using custom prefixes.

## duplicate_remover.py
Detects and removes duplicate files using file hashing.

## backup_manager.py
Creates timestamp-based backups of folders.

## cleaner.py
Removes empty folders from directories.

## report_generator.py
Generates reports from operation logs.

## helper.py
Contains helper functions and logging setup.

---

# How to Run the Project

## Step 1
Open terminal inside project folder.

## Step 2
Run:

```bash
python3 main.py
```

---

# Sample Output

===== SMART FILE MANAGER =====

1. Organize Files
2. Rename Files
3. Remove Duplicate Files
4. Backup Files
5. Remove Empty Folders
6. Generate Report
7. Exit

---

