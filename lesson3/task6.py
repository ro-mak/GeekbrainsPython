def int_func(word: str):
    for s in word:
        if s.isupper():
            raise ValueError("All symbols should be lower case")
    return word.capitalize()


words = input("Enter space-separated line: ").split()
capitalized_words: list[str] = []
for word in words:
    capitalized_words.append(int_func(word))
result_line = ""
for index, word in enumerate(capitalized_words):
    if index != 0:
        result_line += " "
    result_line += word
print(result_line)
