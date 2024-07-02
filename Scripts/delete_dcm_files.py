import os

def delete_dcm_files(directory):
    # Walk through all the directories and files in the given directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.dcm'):
                # Construct the full file path
                file_path = os.path.join(root, file)
                try:
                    # Delete the file
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

# Define the directory to start the search
base_directory = "newAxial"

# Call the function to delete all .dcm files
delete_dcm_files(base_directory)
