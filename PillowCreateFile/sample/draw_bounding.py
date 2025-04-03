from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import os

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

# Paths and settings
header1 = "ព្រះរាជាណាចក្រកម្ពុជា"
header2 = "ជាតិ សាសនា ព្រះមហាក្សត្រ"
header3_unicode = "\u0033"
corpus_path = "corpus/text.txt"

with open(corpus_path, 'r', encoding="utf-8") as file:
    corpus_text = file.read().strip()

font_MPTCMoul = "fonts/KhmerMPTCMoul.ttf"  
font_MPTC = "fonts/KhmerMPTC.ttf"
font_SiemReap = "fonts/KhmerOS_siemreap.otf"
font_taktieng = ImageFont.truetype("fonts/TACTENG.TTF", size=80)

font_header1_size = 54
font_header2_size = 50
text_font_size = 48
footer_font_size = 40

header_color = (22, 45, 123)
text_color = (0, 0, 0)

# A4 size in pixels (300 DPI)
a4_width_px, a4_height_px = 2480, 3508

# Create image
image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
draw = ImageDraw.Draw(image)

# Load fonts
font_header1 = ImageFont.truetype(font_MPTCMoul, font_header1_size)
font_header2 = ImageFont.truetype(font_MPTCMoul, font_header2_size)
font_text = ImageFont.truetype(font_MPTC, text_font_size)
font_footer = ImageFont.truetype(font_SiemReap, footer_font_size)

# Function to draw bounding box
def draw_bbox(draw, bbox, outline_color="red", width=3):
    draw.rectangle(bbox, outline=outline_color, width=width)

# Draw header 1
header1_bbox = draw.textbbox((0, 0), header1, font=font_header1)
header1_x = (a4_width_px - (header1_bbox[2] - header1_bbox[0])) / 2
header1_y = 170
draw.text((header1_x, header1_y), header1, font=font_header1, fill=header_color)
draw_bbox(draw, [header1_x, header1_y, header1_x + header1_bbox[2], header1_y + header1_bbox[3]])

# Draw header 2
header2_bbox = draw.textbbox((0, 0), header2, font=font_header2)
header2_x = (a4_width_px - (header2_bbox[2] - header2_bbox[0])) / 2
header2_y = header1_y + (header1_bbox[3] - header1_bbox[1]) + 20
draw.text((header2_x, header2_y), header2, font=font_header2, fill=header_color)
draw_bbox(draw, [header2_x, header2_y, header2_x + header2_bbox[2], header2_y + header2_bbox[3]])


header3 = "\u0033"  # Unicode character for '3' (replace with your desired character)
font_header3 = ImageFont.truetype("fonts/TACTENG.TTF", size=80)  # Load Taktieng font

# Calculate text bounding box using the same font
confirm_bbox = draw.textbbox((0, 0), header3, font=font_header3)
confirm_width = confirm_bbox[2] - confirm_bbox[0]
confirm_height = confirm_bbox[3] - confirm_bbox[1]

# Calculate centered position
confirm_x = (a4_width_px - confirm_width) / 2
confirm_y = header2_y + 100  # Adjust as needed

# Draw centered text using the Taktieng font
draw.text((confirm_x, confirm_y), header3, font=font_header3, fill=header_color)




# Body text
max_text_width = a4_width_px - 400
wrapped_lines = wrap_text(corpus_text, font_text, max_text_width, draw)
start_x, start_y = 150, header2_y + (header2_bbox[3] - header2_bbox[1]) + 900
line_spacing = 15
top = start_y
for line in wrapped_lines:
    line_bbox = draw.textbbox((start_x, top), line, font=font_text)
    draw.text((start_x, top), line, font=font_text, fill=text_color)
    draw_bbox(draw, [line_bbox[0], line_bbox[1], line_bbox[2], line_bbox[3]])
    top += (line_bbox[3] - line_bbox[1]) + line_spacing

# Insert and mark logo
logo_path = 'img/MPTC_logo.png'
logo = Image.open(logo_path).convert('RGBA')
logo_x, logo_y = 380, 270
image.paste(logo, (logo_x, logo_y), logo)
logo_bbox = [logo_x, logo_y, logo_x + logo.width, logo_y + logo.height]
draw_bbox(draw, logo_bbox, outline_color="blue")


# QR codes and stamp
elements = {
    'Register QR': ('img/Register_qr.png', (200, top + 150)),
    'Info QR': ('img/Info_qr.png', (750, top + 150)),
    'Stamp': ('img/stamp.png', (1700, top + 150))
}

for name, (path, (x, y)) in elements.items():
    img = Image.open(path).convert('RGBA').resize((300, 300), Image.LANCZOS)
    image.paste(img, (x, y), img)
    draw_bbox(draw, [x, y, x + img.width, y + img.height], outline_color="green")

# Footer text example
footer_text = 'អគារលេខ១៣ មហាវិថីព្រះមុនីវង្ស សង្កាត់ស្រះចក'
footer_x, footer_y = 150, top + 650
footer_bbox = draw.textbbox((footer_x, footer_y), footer_text, font=font_footer)
draw.text((footer_x, footer_y), footer_text, font=font_footer, fill=header_color)
draw_bbox(draw, [footer_bbox[0], footer_bbox[1], footer_bbox[2], footer_bbox[3]], outline_color="purple")

# Save the final image with bounding boxes
output_with_bbox_path = "output/Layout_with_bounding_boxes.png"
os.makedirs("output", exist_ok=True)
image.save(output_with_bbox_path)
print(f"✅ Image with bounding boxes saved at: {output_with_bbox_path}")
