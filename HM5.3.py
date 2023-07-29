with open('FB.txt', 'r') as file:
    words = file.read().lower().split()

word_counts = {}
for word in words:
    count = words.count(word)
    word_counts[word] = count

sorted_word_counts = sorted(word_counts.items())

for word, count in sorted_word_counts:
    print(f'{word}: {count}')
