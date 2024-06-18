import os
import shutil

# Define the desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define the categories and their corresponding file extensions
categories = {
    "Documents": [".pdf", ".docx", ".txt", ".doc", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Others": []
}

# Function to create category folders if they don't exist
def create_folders():
    for category in categories.keys():
        folder_path = os.path.join(desktop_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Function to move files to appropriate folders
def move_files():
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        
        # Skip directories
        if os.path.isdir(item_path):
            continue

        # Determine the file's category
        file_moved = False
        for category, extensions in categories.items():
            if any(item.lower().endswith(ext) for ext in extensions):
                shutil.move(item_path, os.path.join(desktop_path, category, item))
                file_moved = True
                break

        # Move files that don't match any category to 'Others'
        if not file_moved:
            shutil.move(item_path, os.path.join(desktop_path, "Others", item))

if __name__ == "__main__":
    create_folders()
    move_files()
