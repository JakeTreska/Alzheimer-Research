import os

def generate_template_paths(template_folder):
    template_paths = []
    
    for root, _, files in os.walk(template_folder):
        for file in files:
            if file.endswith('.jpg'):
                file_path = os.path.join(root, file)
                template_paths.append(f'r"{file_path}"')
    
    template_paths_str = "template_paths = [" + ",\n                  ".join(template_paths) + "]"
    return template_paths_str

# Path to the template folder
template_folder = r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template"

# Generate the template paths
template_paths_str = generate_template_paths(template_folder)

# Print the result
print(template_paths_str)