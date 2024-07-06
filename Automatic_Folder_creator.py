import os

def create_folders():
    # Ask for folder details
    base_name = input("Enter the base name for the folders: ")
    location = input("Enter the location to create folders: ")
    num_folders = int(input("Enter the number of folders to create: "))

    # Create folders
    for i in range(1, num_folders + 1):
        folder_name = f"{base_name}_{i}"
        folder_path = os.path.join(location, folder_name)
        
        try:
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        except FileExistsError:
            print(f"Folder already exists: {folder_path}")
        except Exception as e:
            print(f"Error creating folder {folder_path}: {e}")

    print("Folder creation complete.")

if __name__ == "__main__":
    create_folders()