import os
import re

def rename_jpg_files(directory):
    # Regular expression to match the specific section of the filename including everything before it
    pattern = re.compile(r'^.*?_\d{17}_')

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg'):
                # Check if the filename matches the pattern
                match = pattern.search(file)
                if match:
                    # Create the new filename by removing everything before and including the matched section
                    new_name = file[match.end():]
                    # Construct the full file paths
                    old_path = os.path.join(root, file)
                    new_path = os.path.join(root, new_name)
                    # Rename the file
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")

# Define the base directory to start the renaming
base_directory = "verynewAxial"

# Call the function to rename the jpg files
rename_jpg_files(base_directory)
