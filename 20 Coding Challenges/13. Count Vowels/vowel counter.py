sentence = list(input("enter a text: ").lower())
total = 0
for vowel in ["a","e","i","o","u"]:
    count = sentence.count(vowel)
    print(f"{vowel}: {count}")
    total += count
print(f"total: {total}")