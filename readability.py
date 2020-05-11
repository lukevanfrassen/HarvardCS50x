import math
from cs50 import get_string

text = get_string("Text:\n")
letters = 0
words = 0
sentences = 0
L = 0
S = 0
index = 0
count = 0
for i in range(len(text)):
    if text[i] == ' ':
        words = words +1
    else:
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            sentences = sentences +1
        else:
            if (text[i] >= 'a' and text[i] <= 'z') or (text[i] >= 'A' and text[i] <= 'Z'):
                letters = letters + 1
words = words + 1
print("Words: \n"+ str(words))
print("Letters: \n"+ str(letters))
print("Sentences: \n"+ str(sentences))
L = (letters/words) * 100
S = (sentences/words) * 100
print("L: \n"+ str(L))
print("S: \n"+ str(S))
index = (0.0588 * L - 0.296 * S - 15.8)
index = round(index)
print("Grade: \n"+ str(index))