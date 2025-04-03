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
corpus_path = "corpus/spaced_text.txt"

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

draw = ImageDraw.Draw(image)


try:
    font_header_1 = ImageFont.truetype(font_MPTCMoul, font_header_1_size)
    font_header_2 = ImageFont.truetype(font_MPTCMoul, font_header_2_size)
    font_text = ImageFont.truetype(font_MPTC, text_font_size)
except IOError:
    print("⚠️ Font not found! Please check the font path.")
    exit()


text_address = '២. បេខ្ខជនដែលត្រូ​វ​បានជ្រើសរើស​ជាប់ជា​ស្ថាពរត្រូវភ្ជាប់មកជាមួយនូវឯកសារតម្រូវ​ រួមមាន៖'
Address_x, Address_y = 350,250
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)

text_address = '+ វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 400 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = 'វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '៣. បេខ្ខជនដែលត្រូ​វ​បានជ្រើសរើស​ជាប់ជា​ស្ថាពរត្រូវភ្ជាប់មកជាមួយនូវឯកសារតម្រូវ​ រួមមាន៖'
Address_x, Address_y = 350,Address_y+100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)

text_address = '+ វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 400 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = 'វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)

text_address = '៤. បេខ្ខជនដែលត្រូ​វ​បានជ្រើសរើស​ជាប់ជា​ស្ថាពរត្រូវភ្ជាប់មកជាមួយនូវឯកសារតម្រូវ​ រួមមាន៖'
Address_x, Address_y = 350,Address_y+100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)

text_address = '+ វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 400 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)

text_address = '៥. បេខ្ខជនដែលត្រូ​វ​បានជ្រើសរើស​ជាប់ជា​ស្ថាពរត្រូវភ្ជាប់មកជាមួយនូវឯកសារតម្រូវ​ រួមមាន៖'
Address_x, Address_y = 350,Address_y+100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)

text_address = '+ វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 400 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)



text_confirm = 'គ.គ្រឹះស្ថានឧត្តមសិក្សា និងជំនាញសិក្សា'
font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
confirm_y = Address_y + 100
confirm_x = 270
draw_text_with_bbox(draw, (confirm_x, confirm_y), text_confirm, font=font_text_confirm, fill=header_color)


text_address = 'វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 400 , confirm_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)

text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)

text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_confirm = 'ឃ.គ្រឹះស្ថានឧត្តមសិក្សា និងជំនាញសិក្សា'
font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
confirm_y = Address_y + 100
confirm_x = 270
draw_text_with_bbox(draw, (confirm_x, confirm_y), text_confirm, font=font_text_confirm, fill=header_color)

text_address = '១. បេខ្ខជនដែលត្រូ​វ​បានជ្រើសរើស​ជាប់ជា​ស្ថាពរត្រូវភ្ជាប់មកជាមួយនូវឯកសារតម្រូវ​ រួមមាន៖'
Address_x, Address_y = 350,confirm_y+100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)

text_address = '+ វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 400 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)

text_address = '- វិទ្យាសាស្រ្តកុំព្យូទ័រ (Coputer  Science)'
Address_x, Address_y = 450 , Address_y+ 100
font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
draw_text_with_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color)


output_path = "output/Layout_with_bounding_boxes5.jpg"
image.save(output_path)

print(f"✅ Image with bounding boxes saved at: {output_path}")
