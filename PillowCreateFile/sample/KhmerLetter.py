import textwrap

# Array of symbols
khmer_consonants = [
    'ក. ', 'ខ. ', 'គ. ', 'ឃ. ', 'ង. ',
    'ច. ', 'ឆ. ', 'ជ. ', 'ឈ. ', 'ញ. ',
    'ដ. ', 'ឋ. ', 'ឌ. ', 'ឍ. ', 'ណ. ',
    'ត. ', 'ថ. ', 'ទ. ', 'ធ. ', 'ន. ',
    'ប. ', 'ផ. ', 'ព. ', 'ភ. ', 'ម. ',
    'យ. ', 'រ. ', 'ល. ', 'វ. ', 'ស. ',
    'ហ. ', 'ឡ. ', 'អ. '
]


corpus_path = "corpus/Title_47_words.txt"


with open(corpus_path,'r',encoding="utf-8") as file:
# Split text into chunks of about 10 words
    text = file.read()
lines= textwrap.wrap(text, width=50, break_long_words=False)

# Render text with symbols
output = '\n'.join(f'{khmer_consonants[i % len(khmer_consonants)]} {line}' for i, line in enumerate(lines))



# Save to file
with open('corpus/TextwithLetter.txt', 'w', encoding='utf-8') as f:
    f.write(output)

print(output)
