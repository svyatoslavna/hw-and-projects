words = ["apple", "banana", "cherry", "date", "fig", "grape"]

for i in range(len(words)):
    if "a" in words[i]:
        words[i] = "FOUND"

print(words)
