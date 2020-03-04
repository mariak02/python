text = "this \nis my \ntext"
print(text)
result = ""
for char in text:
    if char != '\n':
        result += char
print("after removing new line, your text will be-")
print(result)
