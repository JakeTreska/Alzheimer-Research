import os
import cv2
import numpy as np
import shutil
from skimage.metrics import structural_similarity as ssim

def read_image(file_path):
    return cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

def score_image(image, templates):
    best_score = 0
    for template in templates:
        # Perform template matching
        result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        
        # Crop the region that matched the template
        h, w = template.shape
        matched_region = image[max_loc[1]:max_loc[1]+h, max_loc[0]:max_loc[0]+w]
        
        # Compute SSIM between the template and the matched region
        similarity = ssim(template, matched_region)
        
        # Keep the highest similarity score
        best_score = max(best_score, similarity)
    
    return best_score

def process_folder(folder_path, template_paths):
    templates = [read_image(template_path) for template_path in template_paths]
    
    for root, _, files in os.walk(folder_path):
        no_butterfly_folder = os.path.join(root, "no_butterfly")
        os.makedirs(no_butterfly_folder, exist_ok=True)
        
        image_scores = []
        for file in files:
            if file.endswith('.jpg'):
                file_path = os.path.join(root, file)
                image = read_image(file_path)
                
                score = score_image(image, templates)
                image_scores.append((file_path, score))
        
        # Sort images based on the filename numbers (to ensure order)
        image_scores.sort(key=lambda x: int(os.path.basename(x[0]).split('_')[0]))
        
        # Find the best 4 consecutive images based on their scores
        best_sequence = []
        best_sum = 0
        
        for i in range(len(image_scores) - 3):
            current_sum = sum(score for _, score in image_scores[i:i+4])
            if current_sum > best_sum:
                best_sum = current_sum
                best_sequence = image_scores[i:i+4]
        
        # Ensure only the best 4 consecutive images are kept
        best_sequence_paths = set(file_path for file_path, _ in best_sequence)
        
        for file_path, _ in image_scores:
            if file_path not in best_sequence_paths:
                shutil.move(file_path, os.path.join(no_butterfly_folder, os.path.basename(file_path)))
                print(f"Moved: {file_path} to {no_butterfly_folder}")

# Paths to the subfolders
cn_folder = 'test/CN'
ad_folder = 'test/AD'
mci_folder = 'test/MCI'
template_paths = [r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\19_I17379.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\20_I17379.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\21_I17379.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\21_I30873.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\22_I30873.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\22_I40081.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\23_I30873.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\24_I30873.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\26_I83463.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\27_I30067.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\27_I83463.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\28_I30067.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\28_I743661.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\28_I83463.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\28_I88879.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\29_I30067.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\29_I47330.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\29_I88875.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\30_I47330.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\30_I743661.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\30_I88879.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\31_I47330.jpg",
                  r"C:\Users\farha\Downloads\Organized_Image_Data copy 2 - Copy\template\32_I88875.jpg"]  # Paths to your butterfly template images

# Process each folder
process_folder(cn_folder, template_paths)
process_folder(ad_folder, template_paths)
process_folder(mci_folder, template_paths)
