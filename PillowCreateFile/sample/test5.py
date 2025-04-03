from PIL import Image, ImageDraw, ImageFont
import textwrap

def draw_wrapped_text(image, text, font, color, max_width):
    draw = ImageDraw.Draw(image)  # Create the draw object *inside* the function

    # Correct way to get the width of a character:
    char_width = draw.textsize("a", font=font)[0]
    words = textwrap.wrap(text, width=max_width // char_width)

    current_y = 0
    for line in words:
        line_width, line_height = draw.textsize(line, font=font)
        draw.text((0, current_y), line, fill=color, font=font)
        current_y += line_height

# Example usage (same as before):
image_width = 300
image_height = 200
image = Image.new("RGB", (image_width, image_height), "white")

font_size = 16
try:
    font = ImageFont.truetype("arial.ttf", size=font_size)  # Or the path to your font file
except IOError:
    print("Error: Font file not found. Please provide a valid font file.")
    exit()  # Or handle the error appropriately

text = "This is a long string of text that needs to be wrapped within the image boundaries.  We'll see how it handles long words too, like supercalifragilisticexpialidocious."
color = "black"
max_width = image_width - 20

draw_wrapped_text(image, text, font, color, max_width)

image.save("wrapped_text_image.png")
image.show()