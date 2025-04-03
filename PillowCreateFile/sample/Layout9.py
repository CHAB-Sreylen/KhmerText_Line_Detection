from PIL import Image, ImageDraw, ImageFont
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

# Define paths
corpus_text_path = "corpus/text.txt"
corpus_title_path = "corpus/Title_text.txt"
output_dir = "output/layout7/images"
os.makedirs(output_dir, exist_ok=True)
output_labels_dir = "output/layout7/labels"
os.makedirs(output_labels_dir, exist_ok=True)

# Load fonts
font_path = "fonts/KhmerMPTC.ttf"
font_size = 48
try:
    font_text = ImageFont.truetype(font_path, font_size)
except IOError:
    print("⚠️ Font not found! Please check the font path.")
    exit()

# Load text lines
with open(corpus_text_path, 'r', encoding="utf-8") as f:
    text_lines = [line.strip() for line in f.readlines() if line.strip()]

with open(corpus_title_path, 'r', encoding="utf-8") as f:
    title_lines = [line.strip() for line in f.readlines() if line.strip()]

# Ensure matching line count
min_lines = min(len(text_lines), len(title_lines))

# A4 dimensions in pixels
a4_width_px, a4_height_px = 2480, 3508

for i in range(min_lines):
    image = Image.new('RGB', (a4_width_px, a4_height_px), color='white')
    draw = ImageDraw.Draw(image)
    
    # Get single line from text and title
    text_line = text_lines[i]
    title_line = title_lines[i]
    
    # Positioning
    text_x, text_y = 200, 1200
    title_x, title_y = 200, 600
    
    # Draw title
    draw.text((title_x, title_y), title_line, font=font_text, fill=(0, 0, 0))
    
    # Draw text
    draw.text((text_x, text_y), text_line, font=font_text, fill=(0, 0, 0))
    
    # Save image
    image_path = os.path.join(output_dir, f"kh_data_{i+1}.jpg")
    image.save(image_path, format="JPEG", quality=95)
    
    # Save label file
    label_path = os.path.join(output_labels_dir, f"kh_data_{i+1}.txt")
    with open(label_path, "w", encoding="utf-8") as f:
        f.write(f"1 0.5 0.2 0.8 0.1\n")  # Example YOLO annotation (adjust as needed)
    
    print(f"✅ Image saved at: {image_path}")
    print(f"✅ YOLO annotations saved at: {label_path}")

print("🎉 All images generated successfully!")
