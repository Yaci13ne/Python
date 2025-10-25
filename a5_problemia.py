phrase = input("Enter a phrase: ")
words = phrase.split()  
cmp = len(words)      
print("words:", words)
print("Number of words:", cmp)

set = set(words)
print("Unique words:", set)

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}",end=" ,")


