text = input("enter your text: ")
result = " "
for index, char in enumerate(text):
    if not(text[index] == " " and text[index+1] == " "):
        result += char
print("text without Extra Space-")
print(result)
