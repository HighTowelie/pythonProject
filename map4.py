
list_words = [
    "Goldenrod",
    "Purple",
     "Salmon",
     "Turquoise",
     "Cyan"
]
# def len_words (word):
#     return list(len(list_words))
# len_words(list_words)

iter_words = map(str.upper, list_words)
for word in iter_words:
    print(word)
for word in map(str.upper, list_words):
    print(word)