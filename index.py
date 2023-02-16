sentence = ""
end_of_sentence = False
num_chars = 0
num_words = 0
num_vowels = 0
vowels = "aeiouAEIOU"

while not end_of_sentence:
    char = input("Enter a character: ")
    if char == ".":
        end_of_sentence = True
    else:
        sentence += char
        num_chars += 1
        if char == " ":
            num_words += 1
        elif char in vowels:
            num_vowels += 1

# We need to increment the number of words by 1 since the last word
# won't have a space after it
num_words += 1

print("The sentence is:", sentence)
print("The length of the sentence is:", num_chars)
print("The number of words in the sentence is:", num_words)
print("The number of vowels in the sentence is:", num_vowels)
