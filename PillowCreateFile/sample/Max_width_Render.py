# from PIL import Image, ImageDraw, ImageFont
# from khmernltk import word_tokenize

# def wrap_text(text, font, max_width, draw):
#     """
#     Wraps Khmer text to fit within a specified width.

#     Args:
#         text: The text to wrap.
#         font: The ImageFont object.
#         max_width: The maximum width in pixels.
#         draw: The ImageDraw object.

#     Returns:
#         A list of wrapped lines.
#     """
#     words = word_tokenize(text)  # Khmer word segmentation
#     lines = []
#     current_line = ""

#     for word in words:
#         test_line = f"{current_line} {word}".strip()
#         line_width = draw.textbbox((0, 0), test_line, font=font)[2]  # Use textbbox to calculate width

#         if line_width <= max_width:
#             current_line = test_line
#         else:
#             lines.append(current_line)
#             current_line = word

#     lines.append(current_line)  # Add the last line
#     return lines

# # Read the text from the file
# file_path = "corpus/oneline.txt"  # Path to your text file
# try:
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read().strip()  # Read all text and remove extra spaces/lines
# except FileNotFoundError:
#     print(f"⚠️ File not found at {file_path}. Please check the file path.")
#     exit()

# # Example usage:
# font_path = "fonts/KhmerMPTC.ttf"  # Replace with your Khmer font path
# font_size = 20
# max_width = 700  # Set your desired maximum width

# # Load the font
# try:
#     font = ImageFont.truetype(font_path, font_size)
# except IOError:
#     print("⚠️ Font not found! Please check the font path.")
#     exit()

# # Create a new image
# image = Image.new('RGB', (800, 600), color='white')
# draw = ImageDraw.Draw(image)

# # Wrap the text
# wrapped_lines = wrap_text(text, font, max_width, draw)

# # Draw the wrapped lines
# y_text = 50
# for line in wrapped_lines:
#     draw.text((10, y_text), line, font=font, fill=(0, 0, 0))
#     y_text += font.getbbox(line)[3] - font.getbbox(line)[1]  # Compute text height correctly

# # Save the image
# image.save("wrapped_text.png")


from PIL import Image, ImageDraw, ImageFont
from khmernltk import word_tokenize

def wrap_text(text, font, max_width, draw):
    """
    Wraps Khmer text to fit within a specified width while maintaining spaces.
    """
    words = word_tokenize(text)  # Khmer word segmentation
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()  # Keep space between words
        line_width = draw.textbbox((0, 0), test_line, font=font)[2]  # Calculate width

        if line_width <= max_width:
            current_line = test_line  # Add the word to the current line
        else:
            lines.append(current_line)  # Store the complete line
            current_line = word  # Start a new line with the current word

    if current_line:
        lines.append(current_line)  # Add the last line

    return lines

# Read text from file
file_path = "corpus/oneline.txt"
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().strip()
except FileNotFoundError:
    print(f"⚠️ File not found: {file_path}")
    exit()

# Font settings
font_path = "fonts/KhmerMPTC.ttf"  # Replace with your Khmer font path
font_size = 20
max_width = 700  # Maximum width in pixels

# Load font
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print("⚠️ Font not found! Check the font path.")
    exit()

# Create image
image = Image.new('RGB', (800, 600), color='white')
draw = ImageDraw.Draw(image)

# Wrap text while keeping spaces
wrapped_lines = wrap_text(text, font, max_width, draw)

# Draw wrapped text
y_text = 50
for line in wrapped_lines:
    draw.text((10, y_text), line, font=font, fill=(0, 0, 0))
    y_text += font.getbbox(line)[3] - font.getbbox(line)[1]  # Compute text height correctly

# Save the image
image.save("wrapped_text.png")
print("✅ Wrapped text saved as 'wrapped_text.png'")
