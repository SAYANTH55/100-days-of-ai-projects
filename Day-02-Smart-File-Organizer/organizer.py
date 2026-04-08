import os
import shutil

# Folder path
folder_path = "test_folder"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Others": []
}

# Create folders
for folder in file_types.keys():
    folder_dir = os.path.join(folder_path, folder)
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)

# Organize files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()

        moved = False

        for folder, extensions in file_types.items():
            if file_ext in extensions:
                dest = os.path.join(folder_path, folder, file)
                shutil.move(file_path, dest)
                print(f"Moved {file} to {folder}")
                moved = True
                break

        if not moved:
            dest = os.path.join(folder_path, "Others", file)
            shutil.move(file_path, dest)
            print(f"Moved {file} to Others")