# import khmernltk

# corpus_path = "corpus/Title_text.txt"
# # output_path = "corpus/spaced_text.txt"
# output_path = "corpus/Title_47_words.txt"

# with open(corpus_path, 'r', encoding="utf-8") as file:
#     corpus_text = file.read().strip()

# tokens = khmernltk.word_tokenize(corpus_text)
# print(len(tokens))

# # # Adding 5 spaces between words
# # modified_text = ' '.join(tokens)  # 5 spaces

# # # Save the modified text to a new file
# # with open(output_path, 'w', encoding="utf-8") as file:
# #     file.write(modified_text)

# # print(f"Modified text saved to {output_path}")

import khmernltk

corpus_path = "corpus/10000Line-230Words-Cleaned.txt"
output_path = "corpus/Text_100_words.txt"

# Read the input file
with open(corpus_path, 'r', encoding="utf-8") as file:
    lines = file.readlines()

trimmed_lines = []

# Process each line
for line in lines:
    tokens = khmernltk.word_tokenize(line.strip())
    if len(tokens) > 100:  # Trim the line to 47 words
        tokens = tokens[:100]
    trimmed_lines.append("".join(tokens))  # Join back into a line

# Write the trimmed lines to the output file
with open(output_path, 'w', encoding="utf-8") as file:
    file.write("\n".join(trimmed_lines))

print(f"Lines have been trimmed to 47 words and saved to {output_path}.")
