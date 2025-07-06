import os
import shutil as sh
import pathlib as p
from datetime import datetime
folder_path = p.Path(input("Enter absolute path of folder: ")) 

if not folder_path.exists() or not folder_path.is_dir():
    print("Invalid folder path.")
    exit()

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Docs":   [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music":  [".mp3", ".wav", ".aac"],
}

def organize(folder: p.Path):
    files = [f for f in folder.iterdir() if f.is_file()]
    if not files:
        print("No files.")
        return

    for file in files:
        ext = file.suffix.lower()
        moved = False

        for category, extensions in file_types.items():
            if ext in extensions:
                dest_folder = folder / category
                dest_folder.mkdir(exist_ok=True)
                sh.move(str(file), dest_folder / file.name)
                print(f"Moved: {file.name} -> {category}/")
                moved = True
                break

        if not moved:
            other_folder = folder / "Others"
            other_folder.mkdir(exist_ok=True)
            sh.move(str(file), other_folder / file.name)
            print(f"Moved: {file.name} -> Others/")

def log_timestamp():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nFile organization completed at {now}")

if __name__ == "__main__":
    print("Organizing files in:", folder_path)
    organize(folder_path)
    log_timestamp()
