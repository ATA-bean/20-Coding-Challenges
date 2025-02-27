def pos_first_vowel(word : str):
    if word[0] == "y":
        count = 1
    else:
        count = 0

    while count <= (len(word) - 1):
        if word[count] in ["a","e","i","o","u","y"]:
            return count
        count += 1

def word_to_pig_latin(word : str):
    non_letters = ""
    for letter in word:
        if  not ((65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122)):
            non_letters += letter
    
    word = word.replace(non_letters,"")
    
    if pos_first_vowel(word) == 0:
        word = word + "yay"
    else:
        consonant_blend = word[0:pos_first_vowel(word)]
        word = (word.replace(consonant_blend,"")) + consonant_blend + "ay" + non_letters
    return word

