from PIL import Image, ImageDraw, ImageFont

def wrap_text(text, font, max_width, draw):
    """Wrap text to fit within the max_width."""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        width = draw.textlength(test_line, font=font)
        if width <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))
    return lines

def justify_line(line, font, max_width, draw):
    """Justify a single line by distributing extra space between words."""
    words = line.split()
    if len(words) <= 1:
        return line  # No need to justify single-word lines

    # Calculate current line width and extra space needed
    line_width = draw.textlength(line, font=font)
    total_spaces = len(words) - 1
    extra_space = (max_width - line_width) / total_spaces

    # Build justified line by adding extra spaces between words
    justified_line = ""
    for i, word in enumerate(words):
        justified_line += word
        if i < total_spaces:  # Add space between words
            space_width = draw.textlength(" ", font=font)
            space_count = max(int((space_width + extra_space) / space_width), 1)
            justified_line += " " * space_count
    return justified_line

# Read corpus text
corpus_path = "corpus/text.txt"
try:
    with open(corpus_path, 'r', encoding="utf-8") as file:
        corpus_text = file.read().strip()
except FileNotFoundError:
    print("⚠️ Corpus file not found!")
    corpus_text = "Sample fallback text because the corpus file was not found."

# Create a white image
width, height = 1200, 800
image = Image.new("RGB", (width, height), color="white")  # White background
draw = ImageDraw.Draw(image)

# Set text, font, and max width
font_path = "fonts/KhmerMPTC.ttf"  # Replace with your font path
font_size = 20
font = ImageFont.truetype(font_path, font_size)
max_width = 400  # Set desired max width for the text box

# Wrap the text
wrapped_lines = wrap_text(corpus_text, font, max_width, draw)

# Positions and padding
x, y = 200, 200      # Pointer position
box_x = x + 30       # Box starting x position
padding = 15         # Padding inside the text box

# Calculate line height using textbbox
line_bbox = draw.textbbox((0, 0), "A", font=font)
line_height = (line_bbox[3] - line_bbox[1]) + 8  # Add spacing between lines

# Calculate box boundaries
end_x, end_y = box_x + max_width, y + (line_height * len(wrapped_lines))
background_box = [(box_x - padding, y - padding), (end_x + padding, end_y + padding)]

# Draw pointer (green circle)
draw.ellipse([(x - 10, y - 10), (x + 10, y + 10)], fill="green")

# Draw background rectangle (green box)
draw.rectangle(background_box, fill="green")

# Draw justified text
top = y
for i, line in enumerate(wrapped_lines):
    # Justify all lines except the last one
    justified_line = justify_line(line, font, max_width, draw) if i < len(wrapped_lines) - 1 else line
    draw.text((box_x, top), justified_line, font=font, fill="white")
    top += line_height

# Save and display the image
output_path = "output_image.png"
image.save(output_path)
print(f"✅ Image saved at: {output_path}")
