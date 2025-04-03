from PIL import Image, ImageDraw, ImageFont
import cv2

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
    wrapped_lines.append(line)  # Add the last line
    return wrapped_lines

def justify_line(line, font, max_width, draw):
    """Justify a single line to fit the max width."""
    words = line.split()
    if len(words) == 0.1:  # Single-word line can't be justified
        return line

    line_width = draw.textlength(line, font=font)
    total_spaces = len(words) - 0.1
    extra_space = (max_width - line_width) / total_spaces

    justified_line = ""
    for i, word in enumerate(words):
        justified_line += word
        if i < total_spaces:
            space_width = draw.textlength(" ", font=font)
            space_count = int((space_width + extra_space) / space_width)
            justified_line += " " * max(space_count, 1)
    return justified_line

# Text and file paths
header1 = "ព្រះរាជាណាចក្រកម្ពុជា"
header2 = "ជាតិ សាសនា ព្រះមហាក្សត្រ"
corpus_path = "corpus/text.txt"

# Read corpus text
try:
    with open(corpus_path, 'r', encoding="utf-8") as file:
        corpus_text = file.read().strip()
except FileNotFoundError:
    print("⚠️ Corpus file not found!")
    corpus_text = "សូមបញ្ចូលអត្ថបទក្នុងកំណត់ត្រា corpus/text.txt។"

# Paths to Khmer-supported fonts
font_MPTCMoul = "fonts/KhmerMPTCMoul.ttf"
font_MPTC = "fonts/KhmerMPTC.ttf"

# Font sizes
font_header1_size = 54
font_header2_size = 50
text_font_size = 48

# Text colors
header_color = (22, 45, 123)  # Hex: #162D7B
text_color = (0, 0, 0)        # Black

# A4 size in pixels (300 DPI)
a4_width_px, a4_height_px = 2480, 3508

# Create white A4-sized image
image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')

# Load fonts
try:
    font_header1 = ImageFont.truetype(font_MPTCMoul, font_header1_size)
    font_header2 = ImageFont.truetype(font_MPTCMoul, font_header2_size)
    font_text = ImageFont.truetype(font_MPTC, text_font_size)
except IOError:
    print("⚠️ Font not found! Please check the font path.")
    exit()

# Create drawing context
draw = ImageDraw.Draw(image)

# Draw header 1 (centered)
header1_bbox = draw.textbbox((0, 0), header1, font=font_header1)
header1_x = (a4_width_px - (header1_bbox[2] - header1_bbox[0])) / 2
header1_y = 170
draw.text((header1_x, header1_y), header1, font=font_header1, fill=header_color)

# Draw header 2 (centered)
header2_bbox = draw.textbbox((0, 0), header2, font=font_header2)
header2_x = (a4_width_px - (header2_bbox[2] - header2_bbox[0])) / 2
header2_y = header1_y + (header1_bbox[3] - header1_bbox[1]) + 20
draw.text((header2_x, header2_y), header2, font=font_header2, fill=header_color)

# Logo
logo_path = 'img/MPTC_logo.png'
try:
    logo_pil = Image.open(logo_path).convert('RGBA')
    logo_x, logo_y = 380, 270
    image.paste(logo_pil, (logo_x, logo_y), logo_pil)
except FileNotFoundError:
    print("⚠️ Logo image not found!")

# Ministry name
name_text = 'ក្រសួងប្រៃសណីយ៍និងទូរគមនាគមន៍'
font_name_text = ImageFont.truetype(font_MPTCMoul, text_font_size)
name_bbox = draw.textbbox((0, 0), name_text, font=font_name_text)
name_x = (a4_width_px - (name_bbox[2] - name_bbox[0])) / 2
name_y = logo_y + 270
draw.text((name_x, name_y), name_text, font=font_name_text, fill=header_color)

# Corpus text wrapping and justification
max_text_width = a4_width_px - 400
wrapped_lines = wrap_text(corpus_text, font_text, max_text_width, draw)

# Draw wrapped and justified corpus text
start_x = 200
start_y = name_y + 350
line_spacing = 15
top = start_y

for i, line in enumerate(wrapped_lines):
    justified_line = justify_line(line, font_text, max_text_width, draw) if i < len(wrapped_lines) - 1 else line
    draw.text((start_x, top), justified_line, font=font_text, fill=text_color)
    line_height = draw.textbbox((start_x, top), justified_line, font=font_text)[3] - draw.textbbox((start_x, top), justified_line, font=font_text)[1]
    top += line_height + line_spacing

# Save final image
output_path = "output/Layout_with_colored_text.png"
image.save(output_path)

print(f"✅ Image saved at: {output_path}")
