import os

def create_folders():
    # Ask for base folder details
    base_name = input("Enter the base name for the folders: ")
    location = input("Enter the location to create folders: ")
    num_base_folders = int(input("Enter the number of base folders to create: "))

    # Ask for subfolder names
    subfolder1_name = input("Enter the name for the first subfolder: ")
    subfolder2_name = input("Enter the name for the second subfolder: ")

    # Create base folders and subfolders
    for i in range(1, num_base_folders + 1):
        base_folder_name = f"{base_name}_{i}"
        base_folder_path = os.path.join(location, base_folder_name)
        
        try:
            # Create base folder
            os.makedirs(base_folder_path)
            print(f"Created base folder: {base_folder_path}")

            # Create first subfolder
            subfolder1_path = os.path.join(base_folder_path, subfolder1_name)
            os.makedirs(subfolder1_path)
            print(f"Created subfolder: {subfolder1_path}")

            # Create second subfolder
            subfolder2_path = os.path.join(base_folder_path, subfolder2_name)
            os.makedirs(subfolder2_path)
            print(f"Created subfolder: {subfolder2_path}")

        except FileExistsError:
            print(f"Folder already exists: {base_folder_path}")
        except Exception as e:
            print(f"Error creating folders in {base_folder_path}: {e}")

    print("Folder creation complete.")

if __name__ == "__main__":
    create_folders()