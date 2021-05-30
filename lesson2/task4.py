words = None
try:
    words = enumerate(input("Input a space-separated line: ").split())
except Exception as e:
    print(f"There was an error {e}. Please enter a space-separated line.")
if words is not None:
    for w in words:
        print(f"{w[0]} {w[1][:10]}")
