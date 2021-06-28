class NotANumberException(Exception):
    pass


question = ""
data = []
stop_word = "stop"
while True:
    question = input("Enter an element: ")
    if question == stop_word:
        break
    try:
        if not question.isdigit():
            raise NotANumberException("You should enter a digit")
    except NotANumberException as err:
        print(err)
        pass
    else:
        data.append(int(question))

print(data)
