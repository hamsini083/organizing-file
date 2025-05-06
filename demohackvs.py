import os
import shutil
# 🔧 Set your real folder path here
folder_path = "C:/Users/hamsini/Desktop/OrganizerProject"  # <-- CHANGE this to your path!
# 🗂 Define folder names and extensions
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Others': []  # This will catch files with unknown types
}
# 🏗 Create folders if they don't exist
for folder in file_types.keys():
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)
# 🔄 Move files to their respective folders
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    # Skip folders to avoid moving already organized folders
    if os.path.isdir(file_path):
        continue
    # Get file extension
    _, ext = os.path.splitext(file)
    ext = ext.lower()  # Normalize extension
    # Check and move the file
    moved = False
    for folder, extensions in file_types.items():
        if ext in extensions:
            shutil.move(file_path, os.path.join(folder_path, folder, file))
            moved = True
            break
    # If extension not matched, move to 'Others'
    if not moved:
        shutil.move(file_path, os.path.join(folder_path, 'Others', file))
print("✅ Files organized successfully!")

