import os

def rename_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    count = 1
    for file in files:
        if file.endswith(".jpg"):
            new_name = f"image_{count}.jpg"
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
            count += 1
    print("✅ Renamed all JPG files successfully!")

if __name__ == "__main__":
    folder = input("Enter folder path containing JPG files: ")
    rename_files_in_folder(folder)
