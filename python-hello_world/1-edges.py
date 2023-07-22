word1, word2 = "Holberton", "School"

# Extracting substrings from word1 and word2
word1_first_3, word1_last_2, word1_middle = word1[:3], word1[-2:], word1[1:-1]
word2_first_3, word2_last_2, word2_middle = word2[:3], word2[-2:], word2[1:-1]

print(
    "First 3 letters of word1: {}\nLast 2 letters of word1: {}\nMiddle word of word1: {}".format(
        word1_first_3, word1_last_2, word1_middle
    )
)
print(
    "First 3 letters of word2: {}\nLast 2 letters of word2: {}\nMiddle word of word2: {}".format(
        word2_first_3, word2_last_2, word2_middle
    )
)
