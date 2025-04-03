
from PIL import Image, ImageDraw, ImageFont

# Create an A4 sized canvas (A4 is 210x297mm, at 300 DPI that's about 2480x3508 pixels)
a4_width, a4_height = 2480, 3508  # A4 at 300 DPI for better quality
a4_paper = Image.new('RGBA', (a4_width, a4_height), (255, 255, 255, 255))  # White background

# Load the stamp image
stamp_image = Image.open('img/num_stamp.png').convert('RGBA')

# Calculate position to place the stamp (centered horizontally, upper portion vertically)
stamp_x = (a4_width - stamp_image.width) // 2
stamp_y = a4_height // 3  # Positioned at approximately 1/3 down the page

# Paste the stamp onto the A4 paper
a4_paper.paste(stamp_image, (stamp_x, stamp_y), stamp_image)

# Create a draw object to add text
draw = ImageDraw.Draw(a4_paper)

# Define font and text
try:
    font = ImageFont.truetype("arial.ttf", 80)
except IOError:
    # Fallback to default font if arial.ttf is not available
    font = ImageFont.load_default()

text = "Text in front of image"

# Calculate text size to center it - using the newer method
# For Pillow 9.2.0 and later, use font.getbbox or getlength
try:
    # For Pillow 9.2.0 and later
    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
except AttributeError:
    try:
        # For older Pillow versions
        text_width, text_height = draw.textsize(text, font=font)
    except AttributeError:
        # Fallback method if all else fails
        text_width = len(text) * font.size // 2  # Rough estimate
        text_height = font.size

text_x = (a4_width - text_width) // 2
text_y = stamp_y + stamp_image.height // 2 - text_height // 2  # Center text vertically on the stamp

# Draw text on top of the image (in black)
draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

# Save the result
a4_paper.save('a4_with_stamp_and_text.png')