
from PIL import Image, ImageDraw, ImageFont

def render_khmer_text(text, font_path, font_size=32, width=800, padding=20, bg_color="white", text_color="black"):
    """
    Render complete Khmer text without truncation
    
    Args:
        text (str): Khmer text to render
        font_path (str): Path to a font file that supports Khmer script
        font_size (int): Font size in pixels
        width (int): Width of the image in pixels
        padding (int): Padding around text in pixels
        bg_color (str): Background color
        text_color (str): Text color
    
    Returns:
        PIL.Image: Image with rendered text
    """
    # Load font
    font = ImageFont.truetype(font_path, font_size)
    
    # Calculate available width
    available_width = width - (2 * padding)
    
    def split_text_to_lines(text, max_width):
        """Split text into lines that fit within max_width"""
        words = text.split()
        lines = []
        current_line = []
        current_width = 0
        
        for word in words:
            # Include space in measurement except for line start
            space_width = font.getlength(" ") if current_line else 0
            word_width = font.getlength(word) + space_width
            
            if current_width + word_width <= max_width:
                current_line.append(word)
                current_width += word_width
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
                current_width = font.getlength(word)
        
        if current_line:
            lines.append(" ".join(current_line))
        
        return lines
    
    # Get text lines
    lines = split_text_to_lines(text, available_width)
    
    # Calculate required height with extra spacing for Khmer diacritics
    line_height = int(font_size * 2)  # Increased spacing for Khmer
    height = (len(lines) * line_height) + (2 * padding)
    
    # Create image
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # Draw text with proper spacing
    y = padding
    for line in lines:
        # Draw the complete line
        draw.text((padding, y), line, font=font, fill=text_color, features=['kern'])
        y += line_height
    
    return image

# Example usage
if __name__ == "__main__":
    # Complete Khmer text
    khmer_text = """សួស្តី!នេះគឺជាអត្ថបទសាកល្បងសម្រាប់ការសរសេរអក្សរខ្មែរ។ បើងនឹងធ្វើការសាកល្បងការរុំអត្ថបទនៅពេលដែលអត្ថបទវែងជាងទទឹងដែលយើងបានកំណត់។
"""
    
    # Create image
    image = render_khmer_text(
        text=khmer_text,
        font_path="fonts/KhmerMPTC.ttf",
        font_size=32,
        width=800,
        padding=20
    )
    
    # Save or display the image
    image.save("khmer_text_complete.png")
    image.show()