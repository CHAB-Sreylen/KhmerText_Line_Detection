import textwrap

# Array of symbols
symbols = ['១.','-','-','១.','-','-','-','-','-','១.','-','-','-','-','១. ','-','-','-','-', '-','១.','-','-','-','-','-','-','-','១. ','-','-','-','-', '-','-','-','-']
numbers = ['២.','-','-','-','-', '-','៣.','-','-','-','-','២.','-','-','-','-', '-','៤.','-','-','-','-','-','-','-','៥.','-','-','-','-', '-','-','-','-','៦.','-','-','-','-','៧.','-','-','-','-','៨.','-','-','-','-','៩.','-','-','-','-','១០.','-','-','-','-']
bullets = ['-']
# numbers = ['ចំនួន ១​​ ច្បាប់','ចំនួន ២​ ច្បាប់','ចំនួន ៣​​ ច្បាប់','ចំនួន ៤​​ ច្បាប់','ចំនួន ៥​ ច្បាប់','ចំនួន ៦ ច្បាប់','ចំនួន ៧ ច្បាប់','ចំនួន ​៨ ច្បាប់','ចំនួន ​៩ ច្បាប់','ចំនួន ១​០​ ច្បាប់']

corpus_path = "corpus/Title_47_words.txt"


with open(corpus_path,'r',encoding="utf-8") as file:
# Split text into chunks of about 10 words
    text = file.read()
lines= textwrap.wrap(text, width=50, break_long_words=False)

# Render text with symbols
output1 = '\n'.join(f'{symbols[i % len(symbols)]} {line}' for i, line in enumerate(lines))

output2 = '\n'.join(f'{numbers[i % len(numbers)]} {line}' for i, line in enumerate(lines))

output3 = '\n'.join(f'{bullets[i % len(bullets)]} {line}' for i, line in enumerate(lines))


# Save to file
with open('corpus/output1.txt', 'w', encoding='utf-8') as f:
    f.write(output1)

with open('corpus/output2.txt','w',encoding = 'utf-8') as f:
    f.write(output2)

with open('corpus/output3.txt','w',encoding = 'utf-8') as f:
    f.write(output3)

print(output1)
print(output2)

# import textwrap

# # Array of symbols
# symbols = ['១.','-','-','២.','-','-','-','-', '-','១.','-','-','-','-','២.','-','-','-','-', '-','១.','-','-','-','-','-','-','-','២.','-','-','-','-', '-','-','-','-']

# numbers = ['១. វិទ្យាស្ថានវ៉ាន់ដា','២. សាកលវិទ្យាល័យប៊ែលធី អន្តរជាតិ','៣​​. សាកលវិទ្យាល័យបញ្ញាសាស្រ្តកម្ពុជា ','៤. សាកលវិទ្យាល័យភ្នំពេញអន្តរជាតិ','៥. សាកលវិទ្យាល័យវេស្ទើន','៦. សាកលវិទ្យាល័យអន្តរជាតិ','៧. សាកលវិទ្យាល័យឯកទេសនៃកម្ពុជា','៨. សាកលវិទ្យាល័យមេគង្គកម្ពុជា','៩. សាកលវិទ្យាល័យធនធានមនុស្ស','១០. វិទ្យាស្ថានអាយ ស៊ី អេស់់​',' ១១. សាកលវិទ្យាល័យបៀលប្រាយ','១២. សាកលវិទ្យាល័យចេនឡា','១៣. សាកលវិទ្យាល័យអង្គរខេមរា','១៤. សាកលវិទ្យាល័យកម្ពុជា','១៥. សាកលវិទ្យាល័យសៅស៍អ៊ីសថ៍អេយសៀ','១៦. វិទ្យាស្ថានអាហ្កា','១៧. វិទ្យាស្ថានបច្ចេកវិទ្យាគិរីរម្យ','១៨. វិទ្យាស្ថានអាយធី អេឈើដឺមី ស្ទប។']

# corpus_path = "corpus/Title_47_words.txt"


# with open(corpus_path,'r',encoding="utf-8") as file:
# # Split text into chunks of about 10 words
#     text = file.read()
# lines= textwrap.wrap(text, width=50, break_long_words=False)

# # Render text with symbols
# output1 = '\n'.join(f'{symbols[i % len(symbols)]} {line}' for i, line in enumerate(lines))

# output2 = '\n'.join(f'{symbols[i % len(symbols)]} {line} {numbers[i % len(numbers)]}' for i, line in enumerate(lines))


# # Save to file
# with open('corpus/output1.txt', 'w', encoding='utf-8') as f:
#     f.write(output1)

# with open('corpus/output2.txt','w',encoding = 'utf-8') as f:
#     f.write(output2)

# print(output1)
# print(output2)




# from PIL import Image, ImageDraw, ImageFont

# # Create an image with a white background
# width, height = 800, 900
# image = Image.new("RGB", (width, height), "white")
# draw = ImageDraw.Draw(image)

# # Path to a Khmer-supported font (Update this with the actual path on your system)
# font_path = "fonts/khmerMPTC.ttf"  # Example: "/usr/share/fonts/KhmerOS.ttf"
# font_size = 24
# font = ImageFont.truetype(font_path, font_size)

# # List of universities in Khmer
# numbers = [
#     "១. វិទ្យាស្ថានវ៉ាន់ដា", "២. សាកលវិទ្យាល័យប៊ែលធី អន្តរជាតិ", "៣. សាកលវិទ្យាល័យបញ្ញាសាស្រ្តកម្ពុជា",
#     "៤. សាកលវិទ្យាល័យភ្នំពេញអន្តរជាតិ", "៥. សាកលវិទ្យាល័យវេស្ទើន", "៦. សាកលវិទ្យាល័យអន្តរជាតិ",
#     "៧. សាកលវិទ្យាល័យឯកទេសនៃកម្ពុជា", "៨. សាកលវិទ្យាល័យមេគង្គកម្ពុជា", "៩. សាកលវិទ្យាល័យធនធានមនុស្ស",
#     "១០. វិទ្យាស្ថានអាយ ស៊ី អេស", "១១. សាកលវិទ្យាល័យបៀលប្រាយ", "១២. សាកលវិទ្យាល័យចេនឡា",
#     "១៣. សាកលវិទ្យាល័យអង្គរខេមរា", "១៤. សាកលវិទ្យាល័យកម្ពុជា", "១៥. សាកលវិទ្យាល័យសៅស៍អ៊ីសថ៍អេយសៀ",
#     "១៦. វិទ្យាស្ថានអាហ្កា", "១៧. វិទ្យាស្ថានបច្ចេកវិទ្យាគិរីរម្យ", "១៨. វិទ្យាស្ថានអាយធី អេឈើដឺមី ស្ទប។"
# ]

# # Positioning variables
# x, y = 20, 20
# line_spacing = 40

# # Draw text on the image
# for line in numbers:
#     draw.text((x, y), line, fill="black", font=font)
#     y += line_spacing

# # Save the image
# image_path = "khmer_universities.png"
# image.save(image_path)

# print(f"Image saved as {image_path}")


