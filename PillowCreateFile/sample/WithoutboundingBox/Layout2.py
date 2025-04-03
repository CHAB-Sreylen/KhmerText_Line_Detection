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
    # The rectangle drawing is removed:
    # draw.rectangle(bbox, outline=(255, 0, 0), width=2)
    draw.text(position, text, font=font, fill=fill)
    add_yolo_box(label, bbox)
    return bbox



header_1 = "ព្រះរាជាណាចក្រកម្ពុជា"
header_2 = "ជាតិ សាសនា ព្រះមហាក្សត្រ"
header_3_unicode = "\u0033"

corpus_path = "PillowCreateFile/corpus/paragraph.txt"
title_path = "PillowCreateFile/corpus/Title_47_words.txt"

def read_lines_reverse(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            return lines[::-1]  # Reverse the list using slicing
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


paragraphs = read_lines_reverse(corpus_path)
titles = read_lines_reverse(title_path)

font_MPTCMoul = "PillowCreateFile/fonts/KhmerMPTCMoul.ttf"
font_MPTC = "PillowCreateFile/fonts/KhmerMPTC.ttf"
font_SiemReap = "PillowCreateFile/fonts/KhmerOS_siemreap.otf"
font_taktieng = ImageFont.truetype("PillowCreateFile/fonts/TACTENG.TTF", size=80)

font_header_1_size = 54
font_header_2_size = 50
text_font_size = 48
footer_font_size = 40


output_dir = "KhmerText_Line_Detection\data/images"
os.makedirs(output_dir, exist_ok=True)

output_labels = "KhmerText_Line_Detection\data/labels"
os.makedirs(output_labels, exist_ok=True)

# output_dir = "E:/16000Doc/sample5/images"
# os.makedirs(output_dir, exist_ok=True)

# output_dir1 = "E:/16000Doc/sample5/labels"
# os.makedirs(output_dir1, exist_ok=True)

# output_dir = "output/images"
# os.makedirs(output_dir, exist_ok=True)

# output_dir1 = "output/labels"
# os.makedirs(output_dir1, exist_ok=True)  # Corrected: create labels directory

header_color = (0x16, 0x2D, 0x7B)
text_color = (0, 0, 0)
footer_color = (0x16, 0x2D, 0x7B)

a4_width_px, a4_height_px = 2480, 3508

for i, (paragraph,title) in enumerate(zip(paragraphs,titles), start=1):
    if i > 2:  # Stop after generating page 8000
        print("Reached page 4000. Stopping rendering.")
        break
    image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')

    try:
        font_header_1 = ImageFont.truetype(font_MPTCMoul, font_header_1_size)
        font_header_2 = ImageFont.truetype(font_MPTCMoul, font_header_2_size)
        font_text = ImageFont.truetype(font_MPTC, text_font_size)
        font_text_title = ImageFont.truetype(font_MPTCMoul, text_font_size)

    except IOError:
        print("⚠️ Font not found! Please check the font path.")
        exit()

    draw = ImageDraw.Draw(image)

    header_1_y = 170
    header_1_x = (a4_width_px - draw.textlength(header_1, font=font_header_1)) / 2
    header_1_bbox = draw_text_without_bbox(draw, (header_1_x, header_1_y), header_1, font_header_1, fill=header_color,label="text")

    header_2_y = header_1_bbox[3] + 20
    header_2_x = (a4_width_px - draw.textlength(header_2, font=font_header_2)) / 2
    header_2_bbox = draw_text_without_bbox(draw, (header_2_x, header_2_y), header_2, font=font_header_2, fill=header_color,label="text")

    confirm_text = "\u0033"
    font_confirm_text = ImageFont.truetype("PillowCreateFile/fonts/TACTENG.TTF", size=80)
    confirm_y = header_2_bbox[3] + 100
    confirm_x = (a4_width_px - draw.textlength(confirm_text, font=font_confirm_text)) / 2
    confirm_bbox = draw_text_without_bbox(draw, (confirm_x, confirm_y), confirm_text, font=font_confirm_text, fill=header_color,label="nonetext")

    logo_pil = Image.open('PillowCreateFile/img/MPTC_logo.png').convert('RGBA')
    logo_x, logo_y = 380, 270
    image.paste(logo_pil, (logo_x, logo_y), logo_pil)
    logo_bbox = (logo_x, logo_y, logo_x + logo_pil.width, logo_y + logo_pil.height)
    # draw.rectangle(logo_bbox, outline=(255, 0, 0), width=2)
    add_yolo_box("nonetext", logo_bbox)

    text_name = 'ក្រសួងប្រៃសណីយ៍និងទូរគមនាគមន៍'
    name_x, name_y = 150, logo_y + 270
    text_font_name = ImageFont.truetype(font_MPTCMoul, text_font_size)
    draw_text_without_bbox(draw, (name_x, name_y), text_name, font=text_font_name, fill=header_color,label="text")

    text_number = 'លេខ: ......................................................'
    number_x, number_y = 150, name_y + 100
    font_text_number = ImageFont.truetype(font_MPTC, text_font_size)
    draw_text_without_bbox(draw, (number_x, number_y), text_number, font=font_text_number, fill=header_color,label="text")

    # Confirm Text ('សេចក្ដីជូនដំណឹង')
    text_confirm = 'សេចក្ដីជូនដំណឹង'
    font_text_confirm = ImageFont.truetype(font_MPTCMoul, text_font_size)
    confirm_y = header_2_bbox[3] + 600
    confirm_x = (a4_width_px - draw.textlength(text_confirm, font=font_text_confirm)) / 2
    draw_text_without_bbox(draw, (confirm_x, confirm_y), text_confirm, font=font_text_confirm, fill=text_color,label="text")

    # Subtitle ('ស្ដីពី')
    text_subtitle = 'ស្ដីពី'
    subtitle_y = confirm_y + 100
    subtitle_x = (a4_width_px - draw.textlength(text_subtitle, font=font_text_confirm)) / 2
    draw_text_without_bbox(draw, (subtitle_x, subtitle_y), text_subtitle, font=font_text_confirm, fill=text_color,label="text")

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

    max_text_width = a4_width_px - 200
    wrapped_lines = wrap_text(paragraph, font_text, max_text_width, draw)

    start_x, start_y = 150, top+40
    line_spacing = 15
    top = start_y
    for line in wrapped_lines:
        bbox = draw_text_without_bbox(draw, (start_x, top), line, font_text, fill=text_color, label="text")
        top += (bbox[3] - bbox[1]) + line_spacing


    text_date = 'ថ្ងៃ ព្រហស្បតិ៍ ២កើត ខែ ឆ្នាំ រោង ឆស័ក ព.ស ២៥៦៨'
    Date_x, Date_y = 1300, top + 50
    font_text_date = ImageFont.truetype(font_MPTC, text_font_size)
    draw_text_without_bbox(draw, (Date_x, Date_y), text_date, font=font_text_date, fill=text_color,label="text")

    text_address = 'រាជធានីភ្នំពេញ ថ្ងៃទី ៤ ខែ មិថុនា ឆ្នាំ ២០២៣'
    Address_x, Address_y = 1460, top + 150
    font_text_address = ImageFont.truetype(font_MPTC, text_font_size)
    draw_text_without_bbox(draw, (Address_x, Address_y), text_address, font=font_text_address, fill=text_color,label="text")


    stamp = Image.open('PillowCreateFile/img/stamp_with_name.png').convert('RGBA').resize((500, 300), Image.LANCZOS)
    stamp_x, stamp_y = 1700, Address_y + 100
    image.paste(stamp, (stamp_x, stamp_y), stamp)
    # add_yolo_box("stamp", stamp)
    stamp = (stamp_x, stamp_y, stamp_x + 500, stamp_y + 300)
    add_yolo_box("nonetext", stamp)

    line_width = 1
    Line_y= top+630
    draw.line([(150, Line_y), (2330, Line_y)], fill=header_color, width=line_width)


    footer_text = 'អគារលេខ១៣ មហាវិថីព្រះមុនីវង្ស សង្កាត់ស្រះចក'
    Date_x, Date_y = 150, Line_y + 30
    font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
    draw_text_without_bbox(draw, (Date_x, Date_y), footer_text, font=font_footer_text, fill=header_color, label="text")

    footer_text = 'ខណ្ឌដូនពេញ រាជធានីភ្នំពេញ 120210'
    Date_x, Date_y = 150, Line_y + 80
    font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
    draw_text_without_bbox(draw, (Date_x, Date_y), footer_text, font=font_footer_text, fill=header_color, label="text")

    footer_text = '123   023 724 810'
    Date_x, Date_y = 2000, Line_y + 30
    font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
    draw_text_without_bbox(draw, (Date_x, Date_y), footer_text, font=font_footer_text, fill=header_color, label="text")

    footer_text = 'www.mptc.gov.kh'
    Date_x, Date_y = 2000, Line_y + 80
    font_footer_text = ImageFont.truetype(font_SiemReap, footer_font_size)
    draw_text_without_bbox(draw, (Date_x, Date_y), footer_text, font=font_footer_text, fill=header_color, label="text")
    
    # draw_text_without_bbox(draw, (x,y), text, font=font_text, fill=text_color, label="footer")
    output_path = os.path.join(output_dir, f"kh_doc{i}.jpg")
    image.save(output_path, format="JPEG", quality=20, optimize=True)

    annotations_path = os.path.join(output_labels, f"kh_doc{i}.txt")
   
    with open(annotations_path, "w", encoding="utf-8") as f:
        for label, x_center, y_center, width_box, height_box in yolo_boxes:
            class_id = label_to_id.get(label, -1)
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width_box:.6f} {height_box:.6f}\n")
    print(f"✅ Image saved at: {output_path}")
    print(f"✅ YOLO annotations saved at: {annotations_path}")
    print(f"✅ Image with bounding boxes saved at: {output_path}")

print("🎉 All images generated successfully!")
