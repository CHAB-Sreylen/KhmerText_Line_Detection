# from PIL import Image, ImageDraw, ImageFont
# import os

# # Define A4 size in pixels
# a4_width_px, a4_height_px = 2480, 3508
# max_text_height = 3350  # Max height for text before starting a new image
# start_x = 400  # X position for text

# # YOLO annotations dictionary
# label_to_id = {
#     "header": 0,
#     "text": 1,
#     "logo": 2,
#     "qr": 3,
#     "stamp": 4,
#     "footer": 5
# }

# def add_yolo_box(label, bbox):
#     """ Convert bounding box to YOLO format and store in list """
#     x_min, y_min, x_max, y_max = bbox
#     x_center = (x_min + x_max) / 2 / a4_width_px
#     y_center = (y_min + y_max) / 2 / a4_height_px
#     box_width = (x_max - x_min) / a4_width_px
#     box_height = (y_max - y_min) / a4_height_px
#     yolo_boxes.append((label, x_center, y_center, box_width, box_height))

# def draw_text_without_bbox(draw, position, text, font, fill, label):
#     """ Draw text on image and record its bounding box """
#     bbox = draw.textbbox(position, text, font=font)
#     draw.text(position, text, font=font, fill=fill)
#     add_yolo_box(label, bbox)
#     return bbox

# # Load text file
# bullet_path = "corpus/bulletText.txt"
# with open(bullet_path, 'r', encoding="utf-8") as file:
#     lines = [line.strip() for line in file.readlines() if line.strip()]

# # Font paths
# font_MPTCMoul = "fonts/KhmerMPTCMoul.ttf"
# font_MPTC = "fonts/KhmerMPTC.ttf"

# # Font sizes
# text_font_size = 48
# try:
#     font_text = ImageFont.truetype(font_MPTC, text_font_size)
# except IOError:
#     print("⚠️ Font not found! Please check the font path.")
#     exit()

# # Create output directories
# output_dir = "E:/16000Doc/sample5/images"
# os.makedirs(output_dir, exist_ok=True)

# output_dir1 = "E:/16000Doc/sample5/labels"
# os.makedirs(output_dir1, exist_ok=True)

# # Image counter
# image_index = 3204
# yolo_boxes = []
# top = 100  # Start Y position

# # Create the first image
# image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
# draw = ImageDraw.Draw(image)

# # Process text and distribute across images
# for line in lines:
#     bbox = draw_text_without_bbox(draw, (start_x, top), line, font_text, fill=(0, 0, 0), label="text")
#     text_height = bbox[3] - bbox[1]

#     # Check if adding this text exceeds max height
#     if top + text_height > max_text_height:
#         # Save current image
#         output_path = os.path.join(output_dir, f"kh_doc{image_index}.jpg")
#         image.save(output_path, format="JPEG", quality=20, optimize=True)

#         # Save YOLO annotations
#         annotations_path = os.path.join(output_dir1, f"kh_doc{image_index}.txt")
#         with open(annotations_path, "w", encoding="utf-8") as f:
#             for label, x_center, y_center, width_box, height_box in yolo_boxes:
#                 class_id = label_to_id.get(label, -1)
#                 f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width_box:.6f} {height_box:.6f}\n")

#         print(f"✅ Image saved at: {output_path}")
#         print(f"✅ YOLO annotations saved at: {annotations_path}")

#         # Reset for new image
#         image_index += 1
#         yolo_boxes = []
#         top = 100  # Reset Y position

#         # Create a new blank image
#         image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
#         draw = ImageDraw.Draw(image)

#         # Redraw current line in new image
#         bbox = draw_text_without_bbox(draw, (start_x, top), line, font_text, fill=(0, 0, 0), label="text")
#         text_height = bbox[3] - bbox[1]

#     # Move down for next line
#     top += text_height + 15

# # Save the last image if any text was drawn
# if yolo_boxes:
#     output_path = os.path.join(output_dir, f"kh_doc{image_index}.jpg")
#     image.save(output_path, format="JPEG", quality=20, optimize=True)

#     annotations_path = os.path.join(output_dir1, f"kh_doc{image_index}.txt")
#     with open(annotations_path, "w", encoding="utf-8") as f:
#         for label, x_center, y_center, width_box, height_box in yolo_boxes:
#             class_id = label_to_id.get(label, -1)
#             f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width_box:.6f} {height_box:.6f}\n")

#     print(f"✅ Image saved at: {output_path}")
#     print(f"✅ YOLO annotations saved at: {annotations_path}")

# print("🎉 All images generated successfully!")

from PIL import Image, ImageDraw, ImageFont
import os

# Define A4 size in pixels
a4_width_px, a4_height_px = 2480, 3508
max_text_height = 3350  # Max height for text before starting a new image
max_text_width = 2200   # Max width for text rendering
start_x = 400  # X position for text

# YOLO annotations dictionary
label_to_id = {
    "decorative": 0,
    "text": 1,
    "logo": 2,
    "qr": 3,
    "stamp": 4,
    "footer": 5
}

def add_yolo_box(label, bbox):
    x_min, y_min, x_max, y_max = bbox
    x_center = (x_min + x_max) / 2 / a4_width_px
    y_center = (y_min + y_max) / 2 / a4_height_px
    box_width = (x_max - x_min) / a4_width_px
    box_height = (y_max - y_min) / a4_height_px
    yolo_boxes.append((label, x_center, y_center, box_width, box_height))

def draw_text_wrapped(draw, position, text, font, fill, label):
    words = text.split(' ')
    current_line = ''
    x, y = position

    for word in words:
        test_line = current_line + word + ' '
        bbox = draw.textbbox((x, y), test_line, font=font)
        line_width = bbox[2] - bbox[0]

        # Stop adding words if line width exceeds max_text_width
        if line_width > max_text_width:
            break
        current_line = test_line

    if current_line:
        bbox = draw.textbbox((x, y), current_line, font=font)
        draw.text((x, y), current_line, font=font, fill=fill)
        add_yolo_box(label, bbox)
        y = bbox[3] + 10  # add line spacing after drawing the text

    return y

bullet_path = "corpus/bulletText.txt"
with open(bullet_path, 'r', encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]

font_MPTC = "fonts/KhmerMPTC.ttf"
text_font_size = 48
font_text = ImageFont.truetype(font_MPTC, text_font_size)

# output_dir = "E:/16000Doc/sample5/images"
# # output_dir = "output/images"
# os.makedirs(output_dir, exist_ok=True)

# output_dir1 = "E:/16000Doc/sample5/labels"
# # output_dir1 = "output/labels"
# os.makedirs(output_dir1, exist_ok=True)


output_dir = "C:/16000Doc/sample5/images"
os.makedirs(output_dir, exist_ok=True)

output_dir1 = "C:/16000Doc/sample5/labels"
os.makedirs(output_dir1, exist_ok=True)

image_index = 17831

yolo_boxes = []
top = 100

image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
draw = ImageDraw.Draw(image)

for line in lines:
    new_top = draw_text_wrapped(draw, (start_x, top), line, font_text, fill=(0, 0, 0), label="text")

    if new_top > max_text_height:
        output_path = os.path.join(output_dir, f"kh_doc{image_index}.jpg")
        image.save(output_path, format="JPEG", quality=20, optimize=True)

        annotations_path = os.path.join(output_dir1, f"kh_doc{image_index}.txt")
        with open(annotations_path, "w", encoding="utf-8") as f:
            for label, x_center, y_center, width_box, height_box in yolo_boxes:
                class_id = label_to_id.get(label, -1)
                f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width_box:.6f} {height_box:.6f}\n")

        print(f"✅ Image saved at: {output_path}")
        print(f"✅ YOLO annotations saved at: {annotations_path}")

        image_index += 1
        yolo_boxes = []
        top = 100

        image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
        draw = ImageDraw.Draw(image)
        new_top = draw_text_wrapped(draw, (start_x, top), line, font_text, fill=(0, 0, 0), label="text")

    top = new_top + 15

if yolo_boxes:
    output_path = os.path.join(output_dir, f"kh_doc{image_index}.jpg")
    image.save(output_path, format="JPEG", quality=20, optimize=True)

    annotations_path = os.path.join(output_dir1, f"kh_doc{image_index}.txt")
    with open(annotations_path, "w", encoding="utf-8") as f:
        for label, x_center, y_center, width_box, height_box in yolo_boxes:
            class_id = label_to_id.get(label, -1)
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width_box:.6f} {height_box:.6f}\n")

    print(f"✅ Image saved at: {output_path}")
    print(f"✅ YOLO annotations saved at: {annotations_path}")

print("🎉 All images generated successfully!")
