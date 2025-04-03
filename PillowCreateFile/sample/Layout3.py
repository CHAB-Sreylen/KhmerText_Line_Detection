from PIL import Image, ImageDraw, ImageFont
import cv2
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


def draw_text_with_bbox(draw, position, text, font, fill, bbox_color=(255, 0, 0), bbox_width=2):
    bbox = draw.textbbox(position, text, font=font)
    draw.rectangle(bbox, outline=bbox_color, width=bbox_width)
    draw.text(position, text, font=font, fill=fill)
    return bbox


header_1 = "ព្រះរាជាណាចក្រកម្ពុជា"
header_2 = "ជាតិ សាសនា ព្រះមហាក្សត្រ"
header_3_unicode = "\u0033"

corpus_path = "corpus/text1.txt"

with open(corpus_path, 'r', encoding="utf-8") as file:
    corpus_text = file.read().strip()

font_MPTCMoul = "fonts/KhmerMPTCMoul.ttf"
font_MPTC = "fonts/KhmerMPTC.ttf"
font_SiemReap = "fonts/KhmerOS_siemreap.otf"
font_taktieng = ImageFont.truetype("fonts/TACTENG.TTF", size=80)

font_header_1_size = 54
font_header_2_size = 50
text_font_size = 48
footer_font_size = 40

header_color = (0x16, 0x2D, 0x7B)
text_color = (0, 0, 0)

a4_width_px, a4_height_px = 2480, 3508

image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')

try:
    font_header_1 = ImageFont.truetype(font_MPTCMoul, font_header_1_size)
    font_header_2 = ImageFont.truetype(font_MPTCMoul, font_header_2_size)
    font_text = ImageFont.truetype(font_MPTC, text_font_size)
except IOError:
    print("⚠️ Font not found! Please check the font path.")
    exit()

draw = ImageDraw.Draw(image)

header_1_y = 170
header_1_x = (a4_width_px - draw.textlength(header_1, font=font_header_1)) / 2
header_1_bbox = draw_text_with_bbox(draw, (header_1_x, header_1_y), header_1, font_header_1, fill=header_color)

header_2_y = header_1_bbox[3] + 20
header_2_x = (a4_width_px - draw.textlength(header_2, font=font_header_2)) / 2
header_2_bbox = draw_text_with_bbox(draw, (header_2_x, header_2_y), header_2, font=font_header_2, fill=header_color)

confirm_text = "\u0033"
font_confirm_text = ImageFont.truetype("fonts/TACTENG.TTF", size=80)
confirm_y = header_2_bbox[3] + 100
confirm_x = (a4_width_px - draw.textlength(confirm_text, font=font_confirm_text)) / 2
confirm_bbox = draw_text_with_bbox(draw, (confirm_x, confirm_y), confirm_text, font=font_confirm_text, fill=header_color)

max_text_width = a4_width_px - 300
wrapped_lines = wrap_text(corpus_text, font_text, max_text_width, draw)

start_x, start_y = 150, header_2_bbox[3] + 900
line_spacing = 15
top = start_y
for line in wrapped_lines:
    bbox = draw_text_with_bbox(draw, (start_x, top), line, font_text, fill=text_color)
    top += (bbox[3] - bbox[1]) + line_spacing

logo_pil = Image.open('img/MPTC_logo.png').convert('RGBA')
logo_x, logo_y = 380, 270
image.paste(logo_pil, (logo_x, logo_y), logo_pil)
logo_bbox = (logo_x, logo_y, logo_x + logo_pil.width, logo_y + logo_pil.height)
draw.rectangle(logo_bbox, outline=(255, 0, 0), width=2)

text_name = 'ក្រសួងប្រៃសណីយ៍និងទូរគមនាគមន៍'
name_x, name_y = 150, logo_y + 270
text_font_name = ImageFont.truetype(font_MPTCMoul, text_font_size)
draw_text_with_bbox(draw, (name_x, name_y), text_name, font=text_font_name, fill=header_color)

logo_pil = Image.open('img/num_logo.png').convert('RGBA')
logo_x, logo_y = 1800, 270
image.paste(logo_pil, (logo_x, logo_y), logo_pil)
logo_bbox = (logo_x, logo_y, logo_x + logo_pil.width, logo_y + logo_pil.height)
draw.rectangle(logo_bbox, outline=(255, 0, 0), width=2)

text_name = 'សកលវិទ្យាល័យជាតិគ្រប់គ្រង'
name_x, name_y = 1600, logo_y + 270
text_font_name = ImageFont.truetype(font_MPTCMoul, text_font_size)
draw_text_with_bbox(draw, (name_x, name_y), text_name, font=text_font_name, fill=header_color)

text_number = 'លេខ: ......................................................'
number_x, number_y = 150, name_y + 100
font_text_number = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (number_x, number_y), text_number, font=font_text_number, fill=header_color)



# Confirm Text ('សេចក្ដីជូនដំណឹង')
text_confirm = 'សេចក្ដីជូនដំណឹង'
font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
confirm_y = header_2_bbox[3] + 600
confirm_x = (a4_width_px - draw.textlength(text_confirm, font=font_text_confirm)) / 2
draw_text_with_bbox(draw, (confirm_x, confirm_y), text_confirm, font=font_text_confirm, fill=text_color)

# Subtitle ('ស្ដីពី')
text_subtitle = 'ស្ដីពី'
subtitle_y = confirm_y + 100
subtitle_x = (a4_width_px - draw.textlength(text_subtitle, font=font_text_confirm)) / 2
draw_text_with_bbox(draw, (subtitle_x, subtitle_y), text_subtitle, font=font_text_confirm, fill=text_color)

# Title ('ការផ្ដល់ថវិការមិនគិតប្រាក់សម្រាប់សិក្សាថ្នាក់បិរិញ្ញាបត្រ')
text_title = 'ការផ្ដល់ថវិការមិនគិតប្រាក់សម្រាប់សិក្សាថ្នាក់បិរិញ្ញាបត្រ'
font_text_title = ImageFont.truetype(font_MPTCMoul, text_font_size)
title_y = subtitle_y + 100
title_x = (a4_width_px - draw.textlength(text_title, font=font_text_title)) / 2
draw_text_with_bbox(draw, (title_x, title_y), text_title, font=font_text_title, fill=text_color)

# # QR Codes and Stamps

stamp = Image.open('img/num_stamp.png').convert('RGBA').resize((700, 500), Image.LANCZOS)
stamp_x, stamp_y = int(a4_width_px /2) + 350 , top+60
image.paste(stamp, (stamp_x, stamp_y), stamp)
draw.rectangle((stamp_x, stamp_y, stamp_x + 700, stamp_y + 500), outline=(255, 0, 0), width=2)


stamp = Image.open('img/MPTC_stamp.png').convert('RGBA').resize((650, 500), Image.LANCZOS)
stamp_x, stamp_y = int(a4_width_px /2) - 650 , top+150
image.paste(stamp, (stamp_x, stamp_y), stamp)
draw.rectangle((stamp_x, stamp_y, stamp_x + 650, stamp_y + 500), outline=(255, 0, 0), width=2)

font_qr = 22
text_date = 'សូមទាញយកឯកសារតាមរយ:​'
Date_x, Date_y = 390, top + 350
font_text_date = ImageFont.truetype(font_MPTC,font_qr)
draw_text_with_bbox(draw, (Date_x, Date_y), text_date, font=font_text_date, fill=text_color)


font_qr = 22
text_date = 'QR Code ឫ តំណភ្ជាប់ខាងក្រោម៖​'
Date_x, Date_y = 390, top + 400
font_text_date = ImageFont.truetype(font_MPTC,font_qr)
draw_text_with_bbox(draw, (Date_x, Date_y), text_date, font=font_text_date, fill=text_color)


qr_info = Image.open('img/Gov_qr.png').convert('RGBA').resize((300, 300), Image.LANCZOS)
info_qr_x, info_qr_y = 390, top + 450
image.paste(qr_info, (info_qr_x, info_qr_y), qr_info)
draw.rectangle((info_qr_x, info_qr_y, info_qr_x + 300, info_qr_y + 300), outline=(255, 0, 0), width=2)

font_qr = 28
text_date = 'go.gov.kh/dgc/240212ntif'
font_english = ImageFont.truetype('arial.ttf', font_qr) 
Date_x, Date_y = 390, top + 800
# font_text_date = ImageFont.truetype(font_MPTC,font_qr)
draw_text_with_bbox(draw, (Date_x, Date_y), text_date, font=font_english, fill=text_color)


text_date = 'ថ្ងៃ ព្រហស្បតិ៍ ២កើត ខែ ឆ្នាំ រោង ឆស័ក ព.ស ២៥៦៧'
Date_x, Date_y = int(a4_width_px /2) - 350, top + 50
font_text_date = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Date_x, Date_y), text_date, font=font_text_date, fill=text_color)

text_address = 'រាជធានីភ្នំពេញ ថ្ងៃទី ៤ ខែ មិថុនា ឆ្នាំ ២០២៣'
Address_x, Address_y = int(a4_width_px /2) - 250, top + 150
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)



rgb_image = image.convert("RGB")
output_jpeg = "output/Layout_with_bounding_boxes33.jpg"
rgb_image.save(output_jpeg, format="JPEG", quality=85, optimize=True)


# output_path = "output/Layout_with_bounding_boxes3.png"
image.save(output_jpeg)

print(f"✅ Image with bounding boxes saved at: {output_jpeg}")
