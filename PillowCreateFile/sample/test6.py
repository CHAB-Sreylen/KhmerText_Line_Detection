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

header1 = "ព្រះរាជាណាចក្រកម្ពុជា"
header2 = "ជាតិ សាសនា ព្រះមហាក្សត្រ"
header3_unicode = "\u0033"

corpus_path = "corpus/text.txt"

with open(corpus_path,'r',encoding="utf-8") as file:
    corpus_text = file.read().strip()

# Path to Khmer-supported fonts
font_MPTCMoul = "fonts/KhmerMPTCMoul.ttf"  
font_MPTC = "fonts/KhmerMPTC.ttf"
font_SiemReap = "fonts/KhmerOS_siemreap.otf"
font_taktieng = ImageFont.truetype("fonts/TACTENG.TTF", size=80)
# Font sizes
font_header1_size = 54
font_header2_size = 50
text_font_size = 48  # Equivalent to 11.5 pt at 300 DPI
footer_font_size = 40
# Text color using the provided hex values
header_color = (0x16, 0x2D, 0x7B)  # (22, 45, 123)
text_color = (0,0,0)
# A4 size in pixels (300 DPI)
a4_width_px, a4_height_px = 2480, 3508

# Create a new white A4-sized image
image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')

# Load fonts
try:
    font_header1 = ImageFont.truetype(font_MPTCMoul, font_header1_size)
    font_header2 = ImageFont.truetype(font_MPTCMoul, font_header2_size)
    font_text = ImageFont.truetype(font_MPTC, text_font_size)
except IOError:
    print("⚠️ Font not found! Please check the font path.")
    exit()

# Create a drawing context
draw = ImageDraw.Draw(image)

# Centered Header 1 at y=50px with color
header1_bbox = draw.textbbox((0, 0), header1, font=font_header1)
header1_width = header1_bbox[2] - header1_bbox[0]
header1_x = (a4_width_px - header1_width) / 2
header1_y = 70+100
draw.text((header1_x, header1_y), header1, font=font_header1, fill=header_color)

# Centered Header 2 below Header 1 with color
header2_bbox = draw.textbbox((0, 0), header2, font=font_header2)
header2_width = header2_bbox[2] - header2_bbox[0]
header2_x = (a4_width_px - header2_width) / 2
header2_y = header1_y + (header1_bbox[3] - header1_bbox[1]) + 20  # 20px spacing
draw.text((header2_x, header2_y), header2, font=font_header2, fill=header_color)


# ✅ Correct usage: Use the same font for both bounding box calculation and drawing
confirm_text = "\u0033"  # Unicode character for '3' (replace with your desired character)
font_confirm_text = ImageFont.truetype("fonts/TACTENG.TTF", size=80)  # Load Taktieng font

# Calculate text bounding box using the same font
confirm_bbox = draw.textbbox((0, 0), confirm_text, font=font_confirm_text)
confirm_width = confirm_bbox[2] - confirm_bbox[0]
confirm_height = confirm_bbox[3] - confirm_bbox[1]

# Calculate centered position
confirm_x = (a4_width_px - confirm_width) / 2
confirm_y = header2_y + 100  # Adjust as needed

# Draw centered text using the Taktieng font
draw.text((confirm_x, confirm_y), confirm_text, font=font_confirm_text, fill=header_color)

# Maximum width for wrapped text
max_text_width = a4_width_px - 400

# Wrap the body text
wrapped_lines = wrap_text(corpus_text, font_text, max_text_width, draw)

# Starting position for body text
start_x, start_y = 150, header2_y + (header2_bbox[3] - header2_bbox[1]) + 900  # 50px below header2
line_spacing = 15

# Draw the wrapped text with the specified color
top = start_y
for line in wrapped_lines:
    draw.text((start_x, top), line, font=font_text, fill=text_color)
    line_bbox = draw.textbbox((start_x, top), line, font=font_text)
    line_height = line_bbox[3] - line_bbox[1]
    top += line_height + line_spacing


#logo 
logo = cv2.imread('img/MPTC_logo.png')
logo =  cv2.cvtColor(logo,cv2.COLOR_BGR2RGB)
logo_pil = Image.open('img/MPTC_logo.png').convert('RGBA')
logo_x,logo_y = 380,270
image.paste(logo_pil, (logo_x, logo_y), logo_pil if logo_pil.mode == 'RGBA' else None)

#Ministry name 
text_name = 'ក្រសួងប្រៃសណីយ៍និងទូរគមនាគមន៍'
name_x,name_y = 150, logo_y + 270 
text_font_name = ImageFont.truetype(font_MPTCMoul, text_font_size)
draw.text((name_x,name_y),text_name,font=text_font_name,fill=header_color)

# number
text_number = 'លេខ: ......................................................'
number_x,number_y = 150, name_y + 100
font_text_number = ImageFont.truetype(font_MPTC, text_font_size)
draw.text((number_x,number_y),text_number,font=font_text_number,fill=header_color)

#Date
text_date = 'ថ្ងៃ ព្រហស្បតិ៍ ២កើត ខែ ឆ្នាំ រោង ឆស័ក ព.ស ២៥៦៨'
Date_x,Date_y =1300, name_y + 100
font_text_date = ImageFont.truetype(font_MPTC, text_font_size)
draw.text((Date_x,Date_y),text_date,font=font_text_date,fill=text_color)

#Addres
text_address = 'រាជធានីភ្នំពេញ ថ្ងៃទី ៤ ខែ មិថុនា ឆ្នាំ ២០២៣'
Address_x,Address_y =1460, name_y + 180
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw.text((Address_x,Address_y),text_address,font=font_text_address,fill=text_color)


# Confirm 
text_confirm = 'សេចក្ដីជូនដំណឹង'
font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
confirm_bbox = draw.textbbox((0, 0), text_confirm, font=font_text_confirm)
confirm_width = confirm_bbox[2] - confirm_bbox[0]
confirm_x,confirm_y =(a4_width_px - confirm_width) / 2 , logo_y + 600
# confirm_bbox = draw.textbbox((0, 0), text_confirm, font=font_text_confirm) 
font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
draw.text((confirm_x,confirm_y),confirm_text,font=font_text,fill=text_color)

#ស្ដីពី
text_confirm = 'ស្ដីពី'
font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
confirm_bbox = draw.textbbox((0, 0), text_confirm, font=font_text_confirm)
confirm_width = confirm_bbox[2] - confirm_bbox[0]
confirm_x,confirm_y =(a4_width_px - confirm_width) / 2 , logo_y + 700
# confirm_bbox = draw.textbbox((0, 0), text_confirm, font=font_text_confirm) 
font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
draw.text((confirm_x,confirm_y),text_confirm,font=font_text_confirm,fill=text_color)


text_title = 'ការផ្ដល់ថវិការមិនគិតប្រាក់សម្រាប់សិក្សាថ្នាក់បិរិញ្ញាបត្រ'
font_text_title = ImageFont.truetype(font_MPTCMoul, text_font_size)
confirm_bbox = draw.textbbox((0, 0), text_title, font=font_text_title)
confirm_width = confirm_bbox[2] - confirm_bbox[0]
confirm_x,confirm_y =(a4_width_px - confirm_width) / 2 , logo_y + 800
# confirm_bbox = draw.textbbox((0, 0), text_title, font=font_text_title) 
font_text_title = ImageFont.truetype(font_MPTCMoul, text_font_size)
draw.text((confirm_x,confirm_y),text_title,font=font_text_title,fill=text_color)

#logo 
# ✅ Load the QR image using PIL (no need for OpenCV)
qr_register = Image.open('img/Register_qr.png').convert('RGBA')

# ✅ Resize the QR code before pasting
desired_width, desired_height = 300, 300  # Desired width and height
qr_register = qr_register.resize((desired_width, desired_height), Image.LANCZOS)

# ✅ Paste the resized QR image onto the main image
register_qr_x, register_qr_y = 200, top +150 # Position for the QR code
image.paste(qr_register, (register_qr_x, register_qr_y), qr_register)

# Save the final image
output_path = "output/Layout_with_colored_text.png"
image.save(output_path)



# ✅ Load the QR image using PIL (no need for OpenCV)
qr_info = Image.open('img/Info_qr.png').convert('RGBA')

# ✅ Resize the QR code before pasting
desired_width, desired_height = 300, 300  # Desired width and height
qr_info = qr_info.resize((desired_width, desired_height), Image.LANCZOS)

# ✅ Paste the resized QR image onto the main image
register_qr_x, register_qr_y = 750, top +150 # Position for the QR code
image.paste(qr_info, (register_qr_x, register_qr_y), qr_info)


stamp = Image.open('img/stamp.png').convert('RGBA')

# ✅ Resize the QR code before pasting
desired_width, desired_height = 300, 300  # Desired width and height
stamp = stamp.resize((desired_width, desired_height), Image.LANCZOS)

# ✅ Paste the resized QR image onto the main image
register_qr_x, register_qr_y = 1700, top +150 # Position for the QR code
image.paste(stamp, (register_qr_x, register_qr_y), stamp)

text_qr = 'សូមស្គេន QR Code ដើម្បីចុះឈ្មោះ និងអានព័ត៌មានបន្ថែម'
Date_x,Date_y =150, top +40
font_text_qr = ImageFont.truetype(font_MPTC, text_font_size)
draw.text((Date_x,Date_y),text_qr,font=font_text_qr,fill=text_color)


text_qr = 'https://cdsr.co/enskh'
Date_x,Date_y =150, top +500
font_text_qr = ImageFont.truetype(font_MPTC, text_font_size)
draw.text((Date_x,Date_y),text_qr,font=font_text_qr,fill=header_color)

text_qr = 'https://cdsr.co/enskh'
Date_x,Date_y =700, top +500
font_text_qr = ImageFont.truetype(font_MPTC, text_font_size)
draw.text((Date_x,Date_y),text_qr,font=font_text_qr,fill=header_color)


line_width = 1
draw.line([(150, top+630), (2330, top+630)], fill=header_color, width=line_width)



footer_text = 'អគារលេខ១៣ មហាវិថីព្រះមុនីវង្ស សង្កាត់ស្រះចក'
Date_x,Date_y =150, top +650
font_footer_text = ImageFont.truetype(font_SiemReap,footer_font_size)
draw.text((Date_x,Date_y),footer_text,font=font_footer_text,fill=header_color)

footer_text = 'ខណ្ឌដូនពេញ រាជធានីភ្នំពេញ 120210'
Date_x,Date_y =150, top +710
font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
draw.text((Date_x,Date_y),footer_text,font=font_footer_text,fill=header_color)


footer_text = '123   023 724 810'
Date_x,Date_y =2000, top +650
font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
draw.text((Date_x,Date_y),footer_text,font=font_footer_text,fill=header_color)


footer_text = 'www.mptc.gov.kh'
Date_x,Date_y =2000, top +710
font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
draw.text((Date_x,Date_y),footer_text,font=font_footer_text,fill=header_color)


# footer_font_size

# Save the final image
output_path = "output/Layout_with_colored_text.png"
image.save(output_path)

print(f"✅ Image saved at: {output_path}")
Can you help draw bouding box on the image and save as a new image 
Moreover , extract the bounding box as the yolo format of all element to csv 

