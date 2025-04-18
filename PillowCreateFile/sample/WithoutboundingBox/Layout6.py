
# from PIL import Image, ImageDraw, ImageFont
# import os

# # Define A4 size in pixels
# a4_width_px, a4_height_px = 2480, 3508
# max_text_height = 3350  # Max height for text before starting a new image
# max_text_width = 2200   # Max width for text rendering
# start_x = 400  # X position for text

# # YOLO annotations dictionary
# label_to_id = {
#     "nonetext": 0,
#     "text": 1
# }

# def add_yolo_box(label, bbox):
#     x_min, y_min, x_max, y_max = bbox
#     x_center = (x_min + x_max) / 2 / a4_width_px
#     y_center = (y_min + y_max) / 2 / a4_height_px
#     box_width = (x_max - x_min) / a4_width_px
#     box_height = (y_max - y_min) / a4_height_px
#     yolo_boxes.append((label, x_center, y_center, box_width, box_height))

# def draw_text_wrapped(draw, position, text, font, fill, label):
#     words = text.split(' ')
#     current_line = ''
#     x, y = position

#     for word in words:
#         test_line = current_line + word + ' '
#         bbox = draw.textbbox((x, y), test_line, font=font)
#         line_width = bbox[2] - bbox[0]

#         # Stop adding words if line width exceeds max_text_width
#         if line_width > max_text_width:
#             break
#         current_line = test_line

#     if current_line:
#         bbox = draw.textbbox((x, y), current_line, font=font)
#         draw.text((x, y), current_line, font=font, fill=fill)
#         add_yolo_box(label, bbox)
#         y = bbox[3] + 10  # add line spacing after drawing the text

#     return y

# bullet_path = "PillowCreateFile/corpus/bulletText.txt"
# with open(bullet_path, 'r', encoding="utf-8") as file:
#     lines = [line.strip() for line in file.readlines() if line.strip()]

# font_MPTC = "PillowCreateFile/fonts/KhmerMPTC.ttf"
# text_font_size = 48
# font_text = ImageFont.truetype(font_MPTC, text_font_size)

# # output_dir = "E:/16000Doc/sample5/images"
# # # output_dir = "output/images"
# # os.makedirs(output_dir, exist_ok=True)

# # output_dir1 = "E:/16000Doc/sample5/labels"
# # # output_dir1 = "output/labels"
# # os.makedirs(output_dir1, exist_ok=True)


# output_dir = r"KhmerText_Line_Detection/data/images"
# os.makedirs(output_dir, exist_ok=True)

# output_dir1 = r"KhmerText_Line_Detection/data/labels"
# os.makedirs(output_dir1, exist_ok=True)
# target_image_count = 100
# image_index = 1

# yolo_boxes = []
# top = 100

# image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
# draw = ImageDraw.Draw(image)

# for line in lines:
#     new_top = draw_text_wrapped(draw, (start_x, top), line, font_text, fill=(0, 0, 0), label="text")

#     if new_top > max_text_height:
#         output_path = os.path.join(output_dir, f"kh_doc{image_index}.jpg")
#         image.save(output_path, format="JPEG", quality=20, optimize=True)

#         annotations_path = os.path.join(output_dir1, f"kh_doc{image_index}.txt")
#         with open(annotations_path, "w", encoding="utf-8") as f:
#             for label, x_center, y_center, width_box, height_box in yolo_boxes:
#                 class_id = label_to_id.get(label, -1)
#                 f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width_box:.6f} {height_box:.6f}\n")

#         print(f"✅ Image saved at: {output_path}")
#         print(f"✅ YOLO annotations saved at: {annotations_path}")

#         image_index += 1
#         yolo_boxes = []
#         top = 100

#         image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
#         draw = ImageDraw.Draw(image)
#         new_top = draw_text_wrapped(draw, (start_x, top), line, font_text, fill=(0, 0, 0), label="text")

#     top = new_top + 15

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

# A4 size in pixels
a4_width_px, a4_height_px = 2480, 3508
max_text_height = 3350
max_text_width = 2200
start_x = 400

label_to_id = {
    "nonetext": 0,
    "text": 1
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
        if line_width > max_text_width:
            break
        current_line = test_line

    if current_line:
        bbox = draw.textbbox((x, y), current_line, font=font)
        draw.text((x, y), current_line, font=font, fill=fill)
        add_yolo_box(label, bbox)
        y = bbox[3] + 10

    return y

# Load text lines
bullet_path = "KhmerText_Line_Detection/PillowCreateFile/corpus/bulletText.txt"
with open(bullet_path, 'r', encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]

font_MPTC = "KhmerText_Line_Detection/PillowCreateFile/fonts/KhmerMPTC.ttf"
text_font_size = 48
font_text = ImageFont.truetype(font_MPTC, text_font_size)

output_dir = r"KhmerText_Line_Detection/data/images"
os.makedirs(output_dir, exist_ok=True)
output_dir1 = r"KhmerText_Line_Detection/data/labels"
os.makedirs(output_dir1, exist_ok=True)

target_image_count = 100
image_index = 1
line_index = 0  # Track current line index

while image_index <= target_image_count:
    yolo_boxes = []
    top = 100

    image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
    draw = ImageDraw.Draw(image)

    while top <= max_text_height:
        if line_index >= len(lines):
            line_index = 0  # loop back to start

        line = lines[line_index]
        line_index += 1
        new_top = draw_text_wrapped(draw, (start_x, top), line, font_text, fill=(0, 0, 0), label="text")

        # Stop if out of space
        if new_top > max_text_height:
            break
        top = new_top + 15

    # Save image and annotation
    output_path = os.path.join(output_dir, f"kh_doc{image_index}.jpg")
    image.save(output_path, format="JPEG", quality=20, optimize=True)

    annotations_path = os.path.join(output_dir1, f"kh_doc{image_index}.txt")
    with open(annotations_path, "w", encoding="utf-8") as f:
        for label, x_center, y_center, width_box, height_box in yolo_boxes:
            class_id = label_to_id.get(label, -1)
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width_box:.6f} {height_box:.6f}\n")

    print(f"✅ Saved image {image_index} and labels")

    image_index += 1

print("🎉 Completed generating all images and YOLO labels.")
