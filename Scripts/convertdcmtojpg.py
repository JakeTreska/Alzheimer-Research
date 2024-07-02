import os
import pydicom
import numpy as np
from PIL import Image

def convert_dcm_to_jpg(dcm_file_path, jpg_file_path):
    # Read DICOM file
    dicom_image = pydicom.dcmread(dcm_file_path)
    
    # Get pixel data as numpy array
    pixel_array = dicom_image.pixel_array
    
    # Normalize the pixel array to the range 0-255
    pixel_array = pixel_array - np.min(pixel_array)
    pixel_array = (pixel_array / np.max(pixel_array) * 255).astype(np.uint8)
    
    # Convert to PIL image
    image = Image.fromarray(pixel_array)
    
    # Convert to RGB (optional, if you want to save as color image)
    # image = image.convert('RGB')
    
    # Save as JPG
    image.save(jpg_file_path)

def traverse_and_convert(root_folder):
    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith('.dcm'):
                dcm_file_path = os.path.join(root, file)
                jpg_file_path = os.path.splitext(dcm_file_path)[0] + '.jpg'
                convert_dcm_to_jpg(dcm_file_path, jpg_file_path)
                print(f'Converted: {dcm_file_path} to {jpg_file_path}')

if __name__ == "__main__":
    root_folder = 'newAxial'
    traverse_and_convert(root_folder)
