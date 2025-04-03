import os
from PIL import Image

input_folder = 'img'
output_folder = 'image'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.png'):
        file_path = os.path.join(input_folder, filename)
        # Open the PNG image
        with Image.open(file_path) as img:
            # Convert to RGB (JPEG doesn't support transparency)
            rgb_img = img.convert('RGB')
            # Construct output file path (change extension to .jpg)
            base_filename = os.path.splitext(filename)[0]
            output_file = os.path.join(output_folder, base_filename + '.jpg')
            # Save as JPEG with a quality setting (adjust quality as needed)
            rgb_img.save(output_file, 'JPEG', quality=85)
            print(f"Converted {file_path} to {output_file}")
