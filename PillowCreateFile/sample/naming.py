# from PIL import Image, ImageDraw, ImageFont
# import cv2
# import os

# # Dimensions for the A4 image in pixels
# a4_width_px, a4_height_px = 2480, 3508

# # Global list to collect YOLO boxes: each entry is (label, x_center, y_center, width, height)
# yolo_boxes = []

# def add_yolo_box(label, bbox):
#     """
#     Convert a bounding box (x_min, y_min, x_max, y_max) to YOLO format (normalized)
#     and add it to the global yolo_boxes list.
#     """
#     x_min, y_min, x_max, y_max = bbox
#     x_center = (x_min + x_max) / 2 / a4_width_px
#     y_center = (y_min + y_max) / 2 / a4_height_px
#     box_width = (x_max - x_min) / a4_width_px
#     box_height = (y_max - y_min) / a4_height_px
#     yolo_boxes.append((label, x_center, y_center, box_width, box_height))

# def draw_text_with_bbox(draw, position, text, font, fill, label, bbox_color=(255, 0, 0), bbox_width=2):
#     """
#     Draws text with a rectangle around it. Also converts the rectangle to YOLO format
#     using the given label.
#     """
#     bbox = draw.textbbox(position, text, font=font)
#     draw.rectangle(bbox, outline=bbox_color, width=bbox_width)
#     draw.text(position, text, font=font, fill=fill)
#     add_yolo_box(label, bbox)
#     return bbox

# def wrap_text(text, font, max_width, draw):
#     """Wrap text to fit within a specified width."""
#     words = text.split()
#     wrapped_lines = []
#     line = ""

#     for word in words:
#         test_line = f"{line} {word}".strip()
#         line_width = draw.textlength(test_line, font=font)
#         if line_width <= max_width:
#             line = test_line
#         else:
#             wrapped_lines.append(line)
#             line = word
#     wrapped_lines.append(line)
#     return wrapped_lines

# # File and font paths
# corpus_path = "corpus/text.txt"
# with open(corpus_path, 'r', encoding="utf-8") as file:
#     corpus_text = file.read().strip()

# font_MPTCMoul = "fonts/KhmerMPTCMoul.ttf"
# font_MPTC = "fonts/KhmerMPTC.ttf"
# font_SiemReap = "fonts/KhmerOS_siemreap.otf"
# font_taktieng = ImageFont.truetype("fonts/TACTENG.TTF", size=80)

# # Font sizes
# font_header_1_size = 54
# font_header_2_size = 50
# text_font_size = 48
# footer_font_size = 40

# # Colors
# header_color = (0x16, 0x2D, 0x7B)
# text_color = (0, 0, 0)

# # Create a blank A4 white image
# image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
# draw = ImageDraw.Draw(image)

# # Load fonts (exit if any font is not found)
# try:
#     font_header_1 = ImageFont.truetype(font_MPTCMoul, font_header_1_size)
#     font_header_2 = ImageFont.truetype(font_MPTCMoul, font_header_2_size)
#     font_text = ImageFont.truetype(font_MPTC, text_font_size)
# except IOError:
#     print("⚠️ Font not found! Please check the font path.")
#     exit()

# # Draw header_1 and header_2 (label them as "header")
# header_1 = "ព្រះរាជាណាចក្រកម្ពុជា"
# header_1_y = 170
# header_1_x = (a4_width_px - draw.textlength(header_1, font=font_header_1)) / 2
# header_1_bbox = draw_text_with_bbox(draw, (header_1_x, header_1_y), header_1, font_header_1, fill=header_color, label="header")

# header_2 = "ជាតិ សាសនា ព្រះមហាក្សត្រ"
# header_2_y = header_1_bbox[3] + 20
# header_2_x = (a4_width_px - draw.textlength(header_2, font=font_header_2)) / 2
# header_2_bbox = draw_text_with_bbox(draw, (header_2_x, header_2_y), header_2, font_header_2, fill=header_color, label="header")

# # Draw header_3 (using confirm_text = "\u0033") and label it as "header"
# confirm_text = "\u0033"
# font_confirm_text = ImageFont.truetype("fonts/TACTENG.TTF", size=80)
# confirm_y = header_2_bbox[3] + 100
# confirm_x = (a4_width_px - draw.textlength(confirm_text, font=font_confirm_text)) / 2
# confirm_bbox = draw_text_with_bbox(draw, (confirm_x, confirm_y), confirm_text, font=font_confirm_text, fill=header_color, label="header")

# # Wrap and draw the corpus text (each line labeled as "text")
# max_text_width = a4_width_px - 400
# wrapped_lines = wrap_text(corpus_text, font_text, max_text_width, draw)
# start_x, start_y = 150, header_2_bbox[3] + 900
# line_spacing = 15
# top = start_y
# for line in wrapped_lines:
#     bbox = draw_text_with_bbox(draw, (start_x, top), line, font_text, fill=text_color, label="text")
#     top += (bbox[3] - bbox[1]) + line_spacing

# # Draw and annotate the logo image (label: "logo")
# logo_pil = Image.open('img/MPTC_logo.png').convert('RGBA')
# logo_x, logo_y = 380, 270
# image.paste(logo_pil, (logo_x, logo_y), logo_pil)
# logo_bbox = (logo_x, logo_y, logo_x + logo_pil.width, logo_y + logo_pil.height)
# draw.rectangle(logo_bbox, outline=(255, 0, 0), width=2)
# add_yolo_box("logo", logo_bbox)

# # Draw text elements (their label is determined by the first part of the variable name, e.g. "text")
# text_name = 'ក្រសួងប្រៃសណីយ៍និងទូរគមនាគមន៍'
# name_x, name_y = 150, logo_y + 270
# text_font_name = ImageFont.truetype(font_MPTCMoul, text_font_size)
# draw_text_with_bbox(draw, (name_x, name_y), text_name, font=text_font_name, fill=header_color, label="text")

# text_number = 'លេខ: ......................................................'
# number_x, number_y = 150, name_y + 100
# font_text_number = ImageFont.truetype(font_MPTC, text_font_size)
# draw_text_with_bbox(draw, (number_x, number_y), text_number, font=font_text_number, fill=header_color, label="text")

# text_date = 'ថ្ងៃ ព្រហស្បតិ៍ ២កើត ខែ ឆ្នាំ រោង ឆស័ក ព.ស ២៥៦៨'
# date_x, date_y = 1300, name_y + 100
# font_text_date = ImageFont.truetype(font_MPTC, text_font_size)
# draw_text_with_bbox(draw, (date_x, date_y), text_date, font=font_text_date, fill=text_color, label="text")

# text_address = 'រាជធានីភ្នំពេញ ថ្ងៃទី ៤ ខែ មិថុនា ឆ្នាំ ២០២៣'
# address_x, address_y = 1460, name_y + 180
# font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
# draw_text_with_bbox(draw, (address_x, address_y), text_address, font=font_text_address, fill=text_color, label="text")

# # Confirm text: 'សេចក្ដីជូនដំណឹង' (labeled as "text")
# text_confirm = 'សេចក្ដីជូនដំណឹង'
# font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
# confirm2_y = header_2_bbox[3] + 600
# confirm2_x = (a4_width_px - draw.textlength(text_confirm, font=font_text_confirm)) / 2
# draw_text_with_bbox(draw, (confirm2_x, confirm2_y), text_confirm, font=font_text_confirm, fill=text_color, label="text")

# # Subtitle: 'ស្ដីពី'
# text_subtitle = 'ស្ដីពី'
# subtitle_y = confirm2_y + 100
# subtitle_x = (a4_width_px - draw.textlength(text_subtitle, font=font_text_confirm)) / 2
# draw_text_with_bbox(draw, (subtitle_x, subtitle_y), text_subtitle, font=font_text_confirm, fill=text_color, label="text")

# # Title: 'ការផ្ដល់ថវិការមិនគិតប្រាក់សម្រាប់សិក្សាថ្នាក់បិរិញ្ញាបត្រ'
# text_title = 'ការផ្ដល់ថវិការមិនគិតប្រាក់សម្រាប់សិក្សាថ្នាក់បិរិញ្ញាបត្រ'
# font_text_title = ImageFont.truetype(font_MPTCMoul, text_font_size)
# title_y = subtitle_y + 100
# title_x = (a4_width_px - draw.textlength(text_title, font=font_text_title)) / 2
# draw_text_with_bbox(draw, (title_x, title_y), text_title, font=font_text_title, fill=text_color, label="text")

# # Draw QR Codes and stamp images, and annotate their bounding boxes.
# qr_register = Image.open('img/Register_qr.png').convert('RGBA').resize((300, 300), Image.LANCZOS)
# register_qr_x, register_qr_y = 200, top + 150
# image.paste(qr_register, (register_qr_x, register_qr_y), qr_register)
# qr_reg_bbox = (register_qr_x, register_qr_y, register_qr_x + 300, register_qr_y + 300)
# draw.rectangle(qr_reg_bbox, outline=(255, 0, 0), width=2)
# add_yolo_box("qr", qr_reg_bbox)  # "qr_register" becomes "qr"

# qr_info = Image.open('img/Info_qr.png').convert('RGBA').resize((300, 300), Image.LANCZOS)
# info_qr_x, info_qr_y = 750, top + 150
# image.paste(qr_info, (info_qr_x, info_qr_y), qr_info)
# qr_info_bbox = (info_qr_x, info_qr_y, info_qr_x + 300, info_qr_y + 300)
# draw.rectangle(qr_info_bbox, outline=(255, 0, 0), width=2)
# add_yolo_box("qr", qr_info_bbox)  # "qr_info" becomes "qr"

# stamp = Image.open('img/stamp.png').convert('RGBA').resize((300, 300), Image.LANCZOS)
# stamp_x, stamp_y = 1700, top + 150
# image.paste(stamp, (stamp_x, stamp_y), stamp)
# stamp_bbox = (stamp_x, stamp_y, stamp_x + 300, stamp_y + 300)
# draw.rectangle(stamp_bbox, outline=(255, 0, 0), width=2)
# add_yolo_box("stamp", stamp_bbox)

# # Draw QR instructions as text (labeled as "text")
# text_qr = 'សូមស្គេន QR Code ដើម្បីចុះឈ្មោះ និងអានព័ត៌មានបន្ថែម'
# qr_text1_x, qr_text1_y = 150, top + 40
# font_text_qr = ImageFont.truetype(font_MPTC, text_font_size)
# draw_text_with_bbox(draw, (qr_text1_x, qr_text1_y), text_qr, font=font_text_qr, fill=text_color, label="text")

# text_qr_url = 'https://cdsr.co/enskh'
# qr_text2_x, qr_text2_y = 150, top + 500
# draw_text_with_bbox(draw, (qr_text2_x, qr_text2_y), text_qr_url, font=font_text_qr, fill=text_color, label="text")

# qr_text3_x, qr_text3_y = 700, top + 500
# draw_text_with_bbox(draw, (qr_text3_x, qr_text3_y), text_qr_url, font=font_text_qr, fill=text_color, label="text")

# # Draw a separating line (not annotated as a box)
# line_width = 1
# draw.line([(150, top+630), (2330, top+630)], fill=header_color, width=line_width)

# # Draw footer texts (labeled as "footer")
# footer_text1 = 'អគារលេខ១៣ មហាវិថីព្រះមុនីវង្ស សង្កាត់ស្រះចក'
# footer1_x, footer1_y = 150, top + 650
# font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
# draw_text_with_bbox(draw, (footer1_x, footer1_y), footer_text1, font=font_footer_text, fill=text_color, label="footer")

# footer_text2 = 'ខណ្ឌដូនពេញ រាជធានីភ្នំពេញ 120210'
# footer2_x, footer2_y = 150, top + 710
# draw_text_with_bbox(draw, (footer2_x, footer2_y), footer_text2, font=font_footer_text, fill=text_color, label="footer")

# footer_text3 = '123   023 724 810'
# footer3_x, footer3_y = 2000, top + 650
# draw_text_with_bbox(draw, (footer3_x, footer3_y), footer_text3, font=font_footer_text, fill=text_color, label="footer")

# footer_text4 = 'www.mptc.gov.kh'
# footer4_x, footer4_y = 2000, top + 710
# draw_text_with_bbox(draw, (footer4_x, footer4_y), footer_text4, font=font_footer_text, fill=text_color, label="footer")

# # Write out YOLO annotations to a text file.
# output_dir = "output"
# os.makedirs(output_dir, exist_ok=True)
# annotations_path = os.path.join(output_dir, "annotations.txt")
# with open(annotations_path, "w", encoding="utf-8") as f:
#     for label, x_center, y_center, width_box, height_box in yolo_boxes:
#         # Each line: label x_center y_center width height (normalized)
#         f.write(f"{label} {x_center:.6f} {y_center:.6f} {width_box:.6f} {height_box:.6f}\n")
# print(f"✅ YOLO annotations saved at: {annotations_path}")

# # Save the final image with bounding boxes.
# output_path = os.path.join(output_dir, "Layout_with_bounding_boxes.png")
# image.save(output_path)
# print(f"✅ Image with bounding boxes saved at: {output_path}")




from PIL import Image, ImageDraw, ImageFont
import cv2
import os

# Dimensions for the A4 image in pixels
a4_width_px, a4_height_px = 2480, 3508

# Global list to collect YOLO boxes: each entry is (label, x_center, y_center, width, height)
yolo_boxes = []

# Define a mapping from string labels to numeric class IDs.
label_to_id = {
    "header": 0,
    "text": 1,
    "logo": 2,
    "qr": 3,
    "stamp": 4,
    "footer": 5
}

def add_yolo_box(label, bbox):
    """
    Convert a bounding box (x_min, y_min, x_max, y_max) to YOLO format (normalized)
    and add it to the global yolo_boxes list.
    """
    x_min, y_min, x_max, y_max = bbox
    x_center = (x_min + x_max) / 2 / a4_width_px
    y_center = (y_min + y_max) / 2 / a4_height_px
    box_width = (x_max - x_min) / a4_width_px
    box_height = (y_max - y_min) / a4_height_px
    yolo_boxes.append((label, x_center, y_center, box_width, box_height))

def draw_text_with_bbox(draw, position, text, font, fill, label, bbox_color=(255, 0, 0), bbox_width=2):
    """
    Draws text with a rectangle around it. Also converts the rectangle to YOLO format
    using the given label.
    """
    bbox = draw.textbbox(position, text, font=font)
    draw.rectangle(bbox, outline=bbox_color, width=bbox_width)
    draw.text(position, text, font=font, fill=fill)
    add_yolo_box(label, bbox)
    return bbox

def wrap_text(text, font, max_width, draw):
    """Wrap text to fit within a specified width."""
    words = text.split()
    wrapped_lines = []
    line = ""

    for word in words:
        test_line = f"{line} {word}".strip()
        line_width = draw.textlength(test_line, font=font)
        if line_width <= max_width:
            line = test_line
        else:
            wrapped_lines.append(line)
            line = word
    wrapped_lines.append(line)
    return wrapped_lines

# File and font paths
corpus_path = "corpus/Text-Test.txt"
with open(corpus_path, 'r', encoding="utf-8") as file:
    corpus_text = file.read().strip()

font_MPTCMoul = "fonts/KhmerMPTCMoul.ttf"
font_MPTC = "fonts/KhmerMPTC.ttf"
font_SiemReap = "fonts/KhmerOS_siemreap.otf"
font_taktieng = ImageFont.truetype("fonts/TACTENG.TTF", size=80)

# Font sizes
font_header_1_size = 54
font_header_2_size = 50
text_font_size = 48
footer_font_size = 40

# Colors
header_color = (0x16, 0x2D, 0x7B)
text_color = (0, 0, 0)

# Create a blank A4 white image
image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
draw = ImageDraw.Draw(image)

# Load fonts (exit if any font is not found)
try:
    font_header_1 = ImageFont.truetype(font_MPTCMoul, font_header_1_size)
    font_header_2 = ImageFont.truetype(font_MPTCMoul, font_header_2_size)
    font_text = ImageFont.truetype(font_MPTC, text_font_size)
except IOError:
    print("⚠️ Font not found! Please check the font path.")
    exit()

# Draw header_1 and header_2 (label them as "header")
header_1 = "ព្រះរាជាណាចក្រកម្ពុជា"
header_1_y = 170
header_1_x = (a4_width_px - draw.textlength(header_1, font=font_header_1)) / 2
header_1_bbox = draw_text_with_bbox(draw, (header_1_x, header_1_y), header_1, font_header_1, fill=header_color, label="header")

header_2 = "ជាតិ សាសនា ព្រះមហាក្សត្រ"
header_2_y = header_1_bbox[3] + 20
header_2_x = (a4_width_px - draw.textlength(header_2, font=font_header_2)) / 2
header_2_bbox = draw_text_with_bbox(draw, (header_2_x, header_2_y), header_2, font=font_header_2, fill=header_color, label="header")

# Draw header_3 (using confirm_text = "\u0033") and label it as "header"
confirm_text = "\u0033"
font_confirm_text = ImageFont.truetype("fonts/TACTENG.TTF", size=80)
confirm_y = header_2_bbox[3] + 100
confirm_x = (a4_width_px - draw.textlength(confirm_text, font=font_confirm_text)) / 2
confirm_bbox = draw_text_with_bbox(draw, (confirm_x, confirm_y), confirm_text, font=font_confirm_text, fill=header_color, label="header")

# Wrap and draw the corpus text (each line labeled as "text")
max_text_width = a4_width_px - 300
wrapped_lines = wrap_text(corpus_text, font_text, max_text_width, draw)
start_x, start_y = 150, header_2_bbox[3] + 900
line_spacing = 15
top = start_y
for line in wrapped_lines:
    bbox = draw_text_with_bbox(draw, (start_x, top), line, font_text, fill=text_color, label="text")
    top += (bbox[3] - bbox[1]) + line_spacing

# Draw and annotate the logo image (label: "logo")
logo_pil = Image.open('img/MPTC_logo.png').convert('RGBA')
logo_x, logo_y = 380, 270
image.paste(logo_pil, (logo_x, logo_y), logo_pil)
logo_bbox = (logo_x, logo_y, logo_x + logo_pil.width, logo_y + logo_pil.height)
draw.rectangle(logo_bbox, outline=(255, 0, 0), width=2)
add_yolo_box("logo", logo_bbox)

# Draw text elements (their label is determined by the first part of the variable name, e.g. "text")
text_name = 'ក្រសួងប្រៃសណីយ៍និងទូរគមនាគមន៍'
name_x, name_y = 150, logo_y + 270
text_font_name = ImageFont.truetype(font_MPTCMoul, text_font_size)
draw_text_with_bbox(draw, (name_x, name_y), text_name, font=text_font_name, fill=header_color, label="text")

text_number = 'លេខ: ......................................................'
number_x, number_y = 150, name_y + 100
font_text_number = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (number_x, number_y), text_number, font=font_text_number, fill=header_color, label="text")

text_date = 'ថ្ងៃ ព្រហស្បតិ៍ ២កើត ខែ ឆ្នាំ រោង ឆស័ក ព.ស ២៥៦៨'
date_x, date_y = 1300, name_y + 100
font_text_date = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (date_x, date_y), text_date, font=font_text_date, fill=text_color, label="text")

text_address = 'រាជធានីភ្នំពេញ ថ្ងៃទី ៤ ខែ មិថុនា ឆ្នាំ ២០២៣'
address_x, address_y = 1460, name_y + 180
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (address_x, address_y), text_address, font=font_text_address, fill=text_color, label="text")

# Confirm text: 'សេចក្ដីជូនដំណឹង' (labeled as "text")
text_confirm = 'សេចក្ដីជូនដំណឹង'
font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
confirm2_y = header_2_bbox[3] + 600
confirm2_x = (a4_width_px - draw.textlength(text_confirm, font=font_text_confirm)) / 2
draw_text_with_bbox(draw, (confirm2_x, confirm2_y), text_confirm, font=font_text_confirm, fill=text_color, label="text")

# Subtitle: 'ស្ដីពី'
text_subtitle = 'ស្ដីពី'
subtitle_y = confirm2_y + 100
subtitle_x = (a4_width_px - draw.textlength(text_subtitle, font=font_text_confirm)) / 2
draw_text_with_bbox(draw, (subtitle_x, subtitle_y), text_subtitle, font=font_text_confirm, fill=text_color, label="text")

# Title: 'ការផ្ដល់ថវិការមិនគិតប្រាក់សម្រាប់សិក្សាថ្នាក់បិរិញ្ញាបត្រ'
text_title = 'ការផ្ដល់ថវិការមិនគិតប្រាក់សម្រាប់សិក្សាថ្នាក់បិរិញ្ញាបត្រ'
font_text_title = ImageFont.truetype(font_MPTCMoul, text_font_size)
title_y = subtitle_y + 100
title_x = (a4_width_px - draw.textlength(text_title, font=font_text_title)) / 2
draw_text_with_bbox(draw, (title_x, title_y), text_title, font=font_text_title, fill=text_color, label="text")

# Draw QR Codes and stamp images, and annotate their bounding boxes.
qr_register = Image.open('img/Register_qr.png').convert('RGBA').resize((300, 300), Image.LANCZOS)
register_qr_x, register_qr_y = 200, top + 150
image.paste(qr_register, (register_qr_x, register_qr_y), qr_register)
qr_reg_bbox = (register_qr_x, register_qr_y, register_qr_x + 300, register_qr_y + 300)
draw.rectangle(qr_reg_bbox, outline=(255, 0, 0), width=2)
add_yolo_box("qr", qr_reg_bbox)  # both QR images use the same label "qr"

qr_info = Image.open('img/Info_qr.png').convert('RGBA').resize((300, 300), Image.LANCZOS)
info_qr_x, info_qr_y = 750, top + 150
image.paste(qr_info, (info_qr_x, info_qr_y), qr_info)
qr_info_bbox = (info_qr_x, info_qr_y, info_qr_x + 300, info_qr_y + 300)
draw.rectangle(qr_info_bbox, outline=(255, 0, 0), width=2)
add_yolo_box("qr", qr_info_bbox)

stamp = Image.open('img/stamp.png').convert('RGBA').resize((300, 300), Image.LANCZOS)
stamp_x, stamp_y = 1700, top + 150
image.paste(stamp, (stamp_x, stamp_y), stamp)
stamp_bbox = (stamp_x, stamp_y, stamp_x + 300, stamp_y + 300)
draw.rectangle(stamp_bbox, outline=(255, 0, 0), width=2)
add_yolo_box("stamp", stamp_bbox)

# Draw QR instructions as text (labeled as "text")
text_qr = 'សូមស្គេន QR Code ដើម្បីចុះឈ្មោះ និងអានព័ត៌មានបន្ថែម'
qr_text1_x, qr_text1_y = 150, top + 40
font_text_qr = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (qr_text1_x, qr_text1_y), text_qr, font=font_text_qr, fill=text_color, label="text")

text_qr_url = 'https://cdsr.co/enskh'
qr_text2_x, qr_text2_y = 150, top + 500
draw_text_with_bbox(draw, (qr_text2_x, qr_text2_y), text_qr_url, font=font_text_qr, fill=text_color, label="text")

qr_text3_x, qr_text3_y = 700, top + 500
draw_text_with_bbox(draw, (qr_text3_x, qr_text3_y), text_qr_url, font=font_text_qr, fill=text_color, label="text")

# Draw a separating line (not annotated as a box)
line_width = 1
draw.line([(150, top+630), (2330, top+630)], fill=header_color, width=line_width)

# Draw footer texts (labeled as "footer")
footer_text1 = 'អគារលេខ១៣ មហាវិថីព្រះមុនីវង្ស សង្កាត់ស្រះចក'
footer1_x, footer1_y = 150, top + 650
font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
draw_text_with_bbox(draw, (footer1_x, footer1_y), footer_text1, font=font_footer_text, fill=text_color, label="footer")

footer_text2 = 'ខណ្ឌដូនពេញ រាជធានីភ្នំពេញ 120210'
footer2_x, footer2_y = 150, top + 710
draw_text_with_bbox(draw, (footer2_x, footer2_y), footer_text2, font=font_footer_text, fill=text_color, label="footer")

footer_text3 = '123   023 724 810'
footer3_x, footer3_y = 2000, top + 650
draw_text_with_bbox(draw, (footer3_x, footer3_y), footer_text3, font=font_footer_text, fill=text_color, label="footer")

footer_text4 = 'www.mptc.gov.kh'
footer4_x, footer4_y = 2000, top + 710
draw_text_with_bbox(draw, (footer4_x, footer4_y), footer_text4, font=font_footer_text, fill=text_color, label="footer")

# Write out YOLO annotations to a text file using numeric class IDs.
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
annotations_path = os.path.join(output_dir, "annotations.txt")
with open(annotations_path, "w", encoding="utf-8") as f:
    for label, x_center, y_center, width_box, height_box in yolo_boxes:
        class_id = label_to_id.get(label, -1)  # use -1 if label not found in mapping
        f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width_box:.6f} {height_box:.6f}\n")
print(f"✅ YOLO annotations saved at: {annotations_path}")

# Save the final image with bounding boxes.
output_path = os.path.join(output_dir, "Layout_with_bounding_boxes.png")
image.save(output_path)
print(f"✅ Image with bounding boxes saved at: {output_path}")
