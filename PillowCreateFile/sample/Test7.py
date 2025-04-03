from PIL import Image, ImageDraw, ImageFont
import cv2
import csv

# --- Configuration ---
font_paths = {
    "MPTCMoul": "fonts/KhmerMPTCMoul.ttf",
    "MPTC": "fonts/KhmerMPTC.ttf",
    "SiemReap": "fonts/KhmerOS_siemreap.otf",
    "Taktieng": "fonts/TACTENG.TTF"
}
font_sizes = {
    "header1": 54,
    "header2": 50,
    "text": 48,
    "footer": 40,
    "confirm": 80
}
colors = {
    "header": (22, 45, 123),
    "text": (0, 0, 0)
}
a4_width_px, a4_height_px = 2480, 3508  # A4 size at 300 DPI
output_dir = "output"

# --- Initialize Image ---
image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
draw = ImageDraw.Draw(image)

# --- Helper Functions ---
def load_font(name, size):
    return ImageFont.truetype(font_paths[name], size)

def center_text(text, font, y):
    width = draw.textlength(text, font=font)
    x = (a4_width_px - width) / 2
    draw.text((x, y), text, font=font, fill=colors['header'])
    return draw.textbbox((x, y), text, font=font)

def draw_image(path, x, y, width, height):
    img = Image.open(path).convert('RGBA').resize((width, height), Image.LANCZOS)
    image.paste(img, (x, y), img)
    return [x, y, x + width, y + height]

def save_bounding_boxes(boxes, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["class_id", "x_min", "y_min", "x_max", "y_max", "class_name"])
        writer.writerows(boxes)

# --- Draw Headers ---
font_header1 = load_font("MPTCMoul", font_sizes["header1"])
font_header2 = load_font("MPTCMoul", font_sizes["header2"])
header1_bbox = center_text("ព្រះរាជាណាចក្រកម្ពុជា", font_header1, 170)
header2_bbox = center_text("ជាតិ សាសនា ព្រះមហាក្សត្រ", font_header2, header1_bbox[3] + 20)

# --- Draw Confirmation Text ---
font_confirm = load_font("Taktieng", font_sizes["confirm"])
confirm_bbox = center_text("\u0033", font_confirm, header2_bbox[3] + 100)

# --- Draw Ministry Name ---
font_name = load_font("MPTCMoul", font_sizes["text"])
ministry_bbox = center_text("ក្រសួងប្រៃសណីយ៍និងទូរគមនាគមន៍", font_name, header2_bbox[3] + 250)

# --- Draw QR Codes and Logos ---
bounding_boxes = []
class_counter = 0

def add_box(name, bbox):
    global class_counter
    bounding_boxes.append([class_counter, *bbox, name])
    draw.rectangle(bbox, outline="red", width=2)
    draw.text((bbox[0], max(bbox[1] - 30, 0)), str(class_counter), font=load_font("MPTCMoul", 30), fill="blue")
    class_counter += 1

logo_bbox = draw_image('img/MPTC_logo.png', 380, 270, 250, 250)
add_box("logo", logo_bbox)
qr_bbox = draw_image('img/Register_qr.png', 200, header2_bbox[3] + 400, 300, 300)
add_box("register_qr", qr_bbox)

# --- Save Outputs ---
output_image_path = f"{output_dir}/Layout_with_bounding_boxes.png"
output_csv_path = f"{output_dir}/bounding_boxes.csv"
image.save(output_image_path)
save_bounding_boxes(bounding_boxes, output_csv_path)

print(f"✅ Image saved at: {output_image_path}")
print(f"✅ Bounding boxes saved to: {output_csv_path}")



from PIL import Image, ImageDraw, ImageFont
import os

# Define A4 size in pixels
a4_width_px, a4_height_px = 2480, 3508

# Define parameters
num_images = 1000
start_x = 400  # X position for text
top_margin = 100  # Start Y position
line_spacing = 15  # Space between lines

# Load text file
bullet_path = "corpus/TestBullet.txt"
with open(bullet_path, 'r', encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]

# Calculate lines per image
total_lines = len(lines)
lines_per_image = max(1, total_lines // num_images)  # Avoid division by zero

# Font paths
font_MPTC = "fonts/KhmerMPTC.ttf"
text_font_size = 48
try:
    font_text = ImageFont.truetype(font_MPTC, text_font_size)
except IOError:
    print("⚠️ Font not found! Please check the font path.")
    exit()

# Create output directories
output_dir = "output/images"
os.makedirs(output_dir, exist_ok=True)

# Generate images
line_index = 0
for image_index in range(1, num_images + 1):
    # Create a blank A4 image
    image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
    draw = ImageDraw.Draw(image)

    top = top_margin  # Reset Y position for each image

    # Draw lines on the image
    for _ in range(lines_per_image):
        if line_index >= total_lines:
            break  # Stop if all text has been used

        draw.text((start_x, top), lines[line_index], font=font_text, fill=(0, 0, 0))
        bbox = draw.textbbox((start_x, top), lines[line_index], font=font_text)
        text_height = bbox[3] - bbox[1]
        top += text_height + line_spacing

        line_index += 1  # Move to next line

    # Save image
    output_path = os.path.join(output_dir, f"kh_doc{image_index}.jpg")
    image.save(output_path, format="JPEG", quality=20, optimize=True)
    print(f"✅ Image {image_index} saved at: {output_path}")

print("🎉 All 1000 images generated successfully!")
