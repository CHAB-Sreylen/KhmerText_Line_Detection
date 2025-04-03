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

yolo_boxes = []
label_to_id = {
    "nonetext": 0,
    "text": 1
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

def draw_text_without_bbox(draw, position, text, font, fill, label):
    bbox = draw.textbbox(position, text, font=font)

    draw.text(position, text, font=font, fill=fill)
    add_yolo_box(label, bbox)
    return bbox

header1 = "ព្រះរាជាណាចក្រកម្ពុជា"
header2 = "ជាតិ សាសនា ព្រះមហាក្សត្រ"
header3_unicode = "\u0033"
# corpus_path = "corpus/10000Line-230Words-Cleaned.txt"

corpus_path = "corpus/Text_100_words.txt"
title_path = "corpus/Title_47_words.txt"

with open(corpus_path, 'r', encoding="utf-8") as file:
    paragraphs = [line.strip() for line in file.readlines() if line.strip()]

with open(title_path, 'r', encoding="utf-8") as file:
    titles = [line.strip() for line in file.readlines() if line.strip()]

font_MPTCMoul = "fonts/KhmerMPTCMoul.ttf"
font_MPTC = "fonts/KhmerMPTC.ttf"
font_SiemReap = "fonts/KhmerOS_siemreap.otf"
font_taktieng = ImageFont.truetype("fonts/TACTENG.TTF", size=80)

font_header1_size = 54
font_header2_size = 50
text_font_size = 48
footer_font_size = 40

# output_dir = "output/images"
# os.makedirs(output_dir, exist_ok=True)

# output_dir1 = "output/labels"
# os.makedirs(output_dir1, exist_ok=True)  # Corrected: create labels directory
output_dir = "C:/16000Doc/sample5/images"
os.makedirs(output_dir, exist_ok=True)

output_dir1 = "C:/16000Doc/sample5/labels"
os.makedirs(output_dir1, exist_ok=True)

header_color = (0x16, 0x2D, 0x7B)
text_color = (0, 0, 0)
footer_color = (0x16, 0x2D, 0x7B)

a4_width_px, a4_height_px = 2480, 3508

for i, (paragraph,title) in enumerate(zip(paragraphs,titles), start=21001):
    # Reset yolo_boxes for each new image so that annotations do not carry over
    if i > 24000:  # Stop after generating page 8000
        print("Reached page 10000. Stopping rendering.")
        break
    yolo_boxes = []

    image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
    draw = ImageDraw.Draw(image)
    try:
        font_header1 = ImageFont.truetype(font_MPTCMoul, font_header1_size)
        font_header2 = ImageFont.truetype(font_MPTCMoul, font_header2_size)
        font_text = ImageFont.truetype(font_MPTC, text_font_size)
        font_text_title = ImageFont.truetype(font_MPTCMoul, text_font_size)
    except IOError:
        print("⚠️ Font not found! Please check the font path.")
        exit()

    header1_y = 170
    header1_x = (a4_width_px - draw.textlength(header1, font=font_header1)) / 2
    header1_bbox = draw_text_without_bbox(draw, (header1_x, header1_y), header1, font_header1, fill=header_color, label="text")

    header2_y = header1_bbox[3] + 20
    header2_x = (a4_width_px - draw.textlength(header2, font=font_header2)) / 2
    header2_bbox = draw_text_without_bbox(draw, (header2_x, header2_y), header2, font=font_header2, fill=header_color, label="text")

    confirm_text = "\u0033"
    font_confirm_text = ImageFont.truetype("fonts/TACTENG.TTF", size=80)
    confirm_y = header2_bbox[3] + 100
    confirm_x = (a4_width_px - draw.textlength(confirm_text, font=font_confirm_text)) / 2
    confirm_bbox = draw_text_without_bbox(draw, (confirm_x, confirm_y), confirm_text, font=font_confirm_text, fill=header_color, label="decorative")

    logo_pil = Image.open('img/MPTC_logo.png').convert('RGBA')
    logo_x, logo_y = 380, 270
    image.paste(logo_pil, (logo_x, logo_y), logo_pil)
    logo_bbox = (logo_x, logo_y, logo_x + logo_pil.width, logo_y + logo_pil.height)
    # draw.rectangle(logo_bbox, outline=(255, 0, 0), width=2)
    add_yolo_box("logo", logo_bbox)

    text_name = 'ក្រសួងប្រៃសណីយ៍និងទូរគមនាគមន៍'
    name_x, name_y = 150, logo_y + 270
    text_font_name = ImageFont.truetype(font_MPTCMoul, text_font_size)
    draw_text_without_bbox(draw, (name_x, name_y), text_name, font=text_font_name, fill=header_color, label="text")

    text_number = 'លេខ: ......................................................'
    number_x, number_y = 150, name_y + 100
    font_text_number = ImageFont.truetype(font_MPTC, text_font_size)
    draw_text_without_bbox(draw, (number_x, number_y), text_number, font=font_text_number, fill=header_color, label="text")

    text_date = 'ថ្ងៃ ព្រហស្បតិ៍ ២កើត ខែ ឆ្នាំ រោង ឆស័ក ព.ស ២៥៦៨'
    Date_x, Date_y = 1300, name_y + 100
    font_text_date = ImageFont.truetype(font_MPTC, text_font_size)
    draw_text_without_bbox(draw, (Date_x, Date_y), text_date, font=font_text_date, fill=text_color, label="text")

    text_address = 'រាជធានីភ្នំពេញ ថ្ងៃទី ៤ ខែ មិថុនា ឆ្នាំ ២០២៣'
    Address_x, Address_y = 1460, name_y + 180
    font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
    draw_text_without_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color, label="text")

    text_confirm = 'សេចក្ដីជូនដំណឹង'
    font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
    confirm_y = header2_bbox[3] + 600
    confirm_x = (a4_width_px - draw.textlength(text_confirm, font=font_text_confirm)) / 2
    draw_text_without_bbox(draw, (confirm_x, confirm_y), text_confirm, font=font_text_confirm, fill=text_color, label="text")

    text_subtitle = 'ស្ដីពី'
    subtitle_y = confirm_y + 100
    subtitle_x = (a4_width_px - draw.textlength(text_subtitle, font=font_text_confirm)) / 2
    draw_text_without_bbox(draw, (subtitle_x, subtitle_y), text_subtitle, font=font_text_confirm, fill=text_color, label="text")

    #Title 
    max_text_width = a4_width_px - 300
    wrapped_lines = wrap_text(title, font_text_title, max_text_width, draw)

    start_subtitle_y = subtitle_y + 100
    line_spacing = 15
    top = start_subtitle_y

    for line in wrapped_lines:
    # Calculate text width
        line_width = draw.textlength(line, font=font_text_title)

    # Calculate x-coordinate for center justification
        start_x = (a4_width_px - line_width) / 2

        bbox = draw_text_without_bbox(draw, (start_x, top), line, font_text_title, fill=text_color, label="text")
        top += (bbox[3] - bbox[1]) + line_spacing

    # Text 
    max_text_width = a4_width_px - 200
    wrapped_lines = wrap_text(paragraph, font_text, max_text_width, draw)

    start_x, start_y = 150, top+40
    line_spacing = 15
    top = start_y
    for line in wrapped_lines:
        bbox = draw_text_without_bbox(draw, (start_x, top), line, font_text, fill=text_color, label="text")
        top += (bbox[3] - bbox[1]) + line_spacing

    numbers = [
    "១. វិទ្យាស្ថានវ៉ាន់ដា", "២. សាកលវិទ្យាល័យប៊ែលធី អន្តរជាតិ", "៣. សាកលវិទ្យាល័យបញ្ញាសាស្រ្តកម្ពុជា",
    "៤. សាកលវិទ្យាល័យភ្នំពេញអន្តរជាតិ", "៥. សាកលវិទ្យាល័យវេស្ទើន", "៦. សាកលវិទ្យាល័យអន្តរជាតិ",
    "៧. សាកលវិទ្យាល័យឯកទេសនៃកម្ពុជា", "៨. សាកលវិទ្យាល័យមេគង្គកម្ពុជា", "៩. សាកលវិទ្យាល័យធនធានមនុស្ស"
    ]


    start_x,start_y = 150,top+20
    
    line_spacing =  15
    for line in numbers:
        bbox = draw_text_without_bbox(draw, (start_x, start_y), line, font_text, fill=text_color, label="text")
        start_y += (bbox[3] - bbox[1]) + line_spacing

        # top += line_spacing

    number1 = ["១០. វិទ្យាស្ថានអាយ ស៊ី អេស", "១១. សាកលវិទ្យាល័យបៀលប្រាយ", "១២. សាកលវិទ្យាល័យចេនឡា",
    "១៣. សាកលវិទ្យាល័យអង្គរខេមរា", "១៤. សាកលវិទ្យាល័យកម្ពុជា", "១៥. សាកលវិទ្យាល័យសៅស៍អ៊ីសថ៍អេយសៀ",
    "១៦. វិទ្យាស្ថានអាហ្កា", "១៧. វិទ្យាស្ថានបច្ចេកវិទ្យាគិរីរម្យ", "១៨. វិទ្យាស្ថានអាយធី អេឈើដឺមី ស្ទប។"]


    start_x,start_y = 1200,top+20
    
    line_spacing =  15
    for line in number1:
        bbox = draw_text_without_bbox(draw, (start_x, start_y), line, font_text, fill=text_color, label="text")
        start_y += (bbox[3] - bbox[1]) + line_spacing



    max_text_width = a4_width_px - 200
    wrapped_lines = wrap_text(paragraph, font_text, max_text_width, draw)

    start_x, start_y = 150,start_y+40
    line_spacing = 15
    top = start_y
    for line in wrapped_lines:
        bbox = draw_text_without_bbox(draw, (start_x, top), line, font_text, fill=text_color, label="text")
        top += (bbox[3] - bbox[1]) + line_spacing
    


    line_width = 1
    draw.line([(150, top+100), (2330, top+100)], fill=header_color, width=line_width)

    def get_text_bbox(draw, position, text, font):
        """Get the bounding box of text."""
        left, top_bbox, right, bottom_bbox = draw.textbbox(position, text, font=font)
        return left, top_bbox, right, bottom_bbox

    # Store bounding box coordinates
    all_left = float('inf')
    all_top = float('inf')
    all_right = float('-inf')
    all_bottom = float('-inf')

    footer_texts = [
        ('អគារលេខ១៣ មហាវិថីព្រះមុនីវង្ស សង្កាត់ស្រះចក', 150, top+150),
        ('ខណ្ឌដូនពេញ រាជធានីភ្នំពេញ 120210', 150, top+200),
        ('123 023 724 810', 2000, top+150),
        ('www.mptc.gov.kh', 2000, top+200),
    ]

    # Draw the text elements first, then calculate the bounding box
    for text, x, y in footer_texts:
        font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
        draw.text((x, y), text, font=font_footer_text, fill=footer_color)

    # Calculate the bounding box based on the drawn text
    for text, x, y in footer_texts:
        font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
        left, top_bbox, right, bottom_bbox = get_text_bbox(draw, (x, y), text, font_footer_text)

        # Update overall bounding box
        all_left = min(all_left, left)
        all_top = min(all_top, top_bbox)
        all_right = max(all_right, right)
        all_bottom = max(all_bottom, bottom_bbox)
        
    # draw.rectangle((all_left, all_top, all_right, all_bottom), outline="red", width=2) #add some padding
    bbox = (all_left,all_top, all_right, all_bottom)
    add_yolo_box("footer",bbox)
    # draw_text_without_bbox(draw, (x,y), text, font=font_text, fill=text_color, label="footer")
    output_path = os.path.join(output_dir, f"kh_doc{i}.jpg")
    image.save(output_path, format="JPEG", quality=10, optimize=True)

    annotations_path = os.path.join(output_dir1, f"kh_doc{i}.txt")
   
    with open(annotations_path, "w", encoding="utf-8") as f:
        for label, x_center, y_center, width_box, height_box in yolo_boxes:
            class_id = label_to_id.get(label, -1)
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width_box:.6f} {height_box:.6f}\n")
    print(f"✅ Image saved at: {output_path}")
    print(f"✅ YOLO annotations saved at: {annotations_path}")
    print(f"✅ Image with bounding boxes saved at: {output_path}")

print("🎉 All images generated successfully!")
