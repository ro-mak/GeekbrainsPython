def some_func():
    print("Some func")


listOfSomething = ["el1", 2, {1, 5, 9}, {1: 2, 2: "213"}, some_func, 1.0, ("1el", "2el", "Kal'el")]
for i in listOfSomething:
    print(type(i))
