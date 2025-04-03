from PIL import Image, ImageDraw, ImageFont
import os

# Define A4 size in pixels
a4_width_px, a4_height_px = 2480, 3508
max_text_height = 700  # Max height for text before starting a new image
positions = [(300, 200), (300, 1000)]  # Positions for text

# YOLO annotations dictionary
label_to_id = {
    "header": 0,
    "text": 1,
    "logo": 2,
    "qr": 3,
    "stamp": 4,
    "footer": 5
}

def add_yolo_box(label, bbox, yolo_boxes):
    x_min, y_min, x_max, y_max = bbox
    x_center = (x_min + x_max) / 2 / a4_width_px
    y_center = (y_min + y_max) / 2 / a4_height_px
    box_width = (x_max - x_min) / a4_width_px
    box_height = (y_max - y_min) / a4_height_px
    yolo_boxes.append((label, x_center, y_center, box_width, box_height))

def draw_text_with_bbox(draw, position, text, font, fill, label, yolo_boxes):
    bbox = draw.textbbox(position, text, font=font)
    draw.text(position, text, font=font, fill=fill)
    add_yolo_box(label, bbox, yolo_boxes)
    return bbox

font_path = "fonts/KhmerMPTC.ttf"
font_size = 48
font = ImageFont.truetype(font_path, font_size)

output_dir = "output/images"
os.makedirs(output_dir, exist_ok=True)

output_labels = "output/labels"
os.makedirs(output_labels, exist_ok=True)

bullet_path = "corpus/TestBullet.txt"
with open(bullet_path, 'r', encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]

image_index = 1
line_index = 0

while line_index < len(lines):
    image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
    draw = ImageDraw.Draw(image)
    yolo_boxes = []

    for start_x, top in positions:
        current_height = 0
        while line_index < len(lines):
            bbox = draw.textbbox((start_x, top + current_height), lines[line_index], font=font)
            text_height = bbox[3] - bbox[1]

            if current_height + text_height > max_text_height:
                break

            draw_text_with_bbox(draw, (start_x, top + current_height), lines[line_index], font, "black", label_to_id["text"], yolo_boxes)

            current_height += text_height + 10  # Spacing between lines
            line_index += 1

    static_text = '២. បេក្ខជនដែលត្រូវបានជ្រើសរើសជាប់ជាស្ថាពរត្រូវភ្ជាប់មកជាមួយឯកសារតម្រូវ​ រួមមាន៖'
    draw_text_with_bbox(draw, (150, 100), static_text, font, "black", label_to_id["text"], yolo_boxes)

    image_path = os.path.join(output_dir, f"kh_doc{image_index}.jpg")
    image.save(image_path, format="JPEG", quality=20, optimize=True)

    annotations_path = os.path.join(output_labels, f"kh_doc{image_index}.txt")
    with open(annotations_path, "w", encoding="utf-8") as f:
        for box in yolo_boxes:
            f.write(f"{box[0]} {box[1]:.6f} {box[2]:.6f} {box[3]:.6f} {box[4]:.6f}\n")

    print(f"✅ Image saved at: {image_path}")
    print(f"✅ YOLO annotations saved at: {annotations_path}")

    image_index += 1

print("🎉 All images generated successfully!")