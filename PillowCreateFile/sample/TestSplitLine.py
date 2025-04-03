# from PIL import Image, ImageDraw, ImageFont

# # Define parameters
# image_width = 800  # Adjust as needed
# image_height = 100  # Stop rendering after this height
# bg_color = "white"
# text_color = "black"
# font_path = "fonts/KhmerMPTC.ttf"  # Update with your font path
# font_size = 20  # Adjust as needed

# # Load the text
# text = """This is an example text.
# It will be rendered line by line.
# The rendering stops when we reach 500 pixels in height.
# Each line will be positioned accordingly.
# This is an example text.
# It will be rendered line by line.
# The rendering stops when we reach 500 pixels in height.
# Each line will be positioned accordingly."""

# # Initialize Image
# img = Image.new("RGB", (image_width, image_height), bg_color)
# draw = ImageDraw.Draw(img)

# # Load font
# font = ImageFont.truetype(font_path, font_size)

# # Initialize text position
# x, y = 10, 10  # Start position
# line_spacing = 5  # Space between lines

# # Render text line by line
# for line in text.split("\n"):
#     # Use textbbox() for more accurate height calculation
#     bbox = draw.textbbox((x, y), line, font=font)
#     text_height = bbox[3] - bbox[1]  # Height from bbox

#     # Check if next line exceeds max height
#     if y + text_height > image_height:
#         break

#     # Draw text
#     draw.text((x, y), line, font=font, fill=text_color)

#     # Move y-position down
#     y += text_height + line_spacing

# # Save or Show Image
# img.show()  # Opens the image
# img.save("rendered_text.png")  # Save the output


from PIL import Image, ImageDraw, ImageFont

# Define parameters
image_width = 800  # Adjust as needed
image_height = 200  # Overall image height
stop_rendering_at = 100  # Stop text rendering when near 70 pixels
bg_color = "white"
text_color = "black"
font_path = "fonts/KhmerMPTC.ttf"  # Update with your font path
font_size = 20  # Adjust as needed

# Load the text
text = """This is an example text.
It will be rendered line by line.
The rendering stops when we reach 500 pixels in height.
Each line will be positioned accordingly.
This is an example text.
It will be rendered line by line.
The rendering stops when we reach 500 pixels in height.
Each line will be positioned accordingly."""

# Initialize Image
img = Image.new("RGB", (image_width, image_height), bg_color)
draw = ImageDraw.Draw(img)

# Load font
font = ImageFont.truetype(font_path, font_size)

# Initialize text position
x, y = 10, 10  # Start position
line_spacing = 5  # Space between lines

# Render text line by line
for line in text.split("\n"):
    line = line.strip()  # Remove extra spaces or newlines
    if not line:
        continue  # Skip empty lines

    # Use textbbox() for accurate height calculation
    bbox = draw.textbbox((x, y), line, font=font)
    text_height = bbox[3] - bbox[1]  # Calculate height

    # Check if the next line would exceed the stop height (70 pixels)
    if y + text_height > stop_rendering_at:
        break  # Stop rendering if it exceeds 70 pixels

    # Draw text
    draw.text((x, y), line, font=font, fill=text_color)

    # Move y-position down
    y += text_height + line_spacing

# Save or Show Image
img.show()  # Opens the image
img.save("rendered_text.png")  # Save the output


    # for line in bullet_text.split("\n"):
    #     bbox = draw_text_without_bbox(draw, (start_x, top), line, font_text, fill=text_color, label="text")
    #     text_height = bbox[3]-bbox[1]
    #     if text_height> max_text_height:
    #         break 
    #     top += text_height+line_spacing