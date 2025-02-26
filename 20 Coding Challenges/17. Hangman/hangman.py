import random
words = ["orange","kangaroo","bubble","mathematics","bedroom","chicken","trophy","carousel"]
word = random.choice(words)
guessed_word = list("_"*len(word))

lives = 5
previous_letters = []
wrong_letters = []
while guessed_word != list(word) and lives != 0:

    output = ""
    for letter in guessed_word:
        output += letter + " "
    print(output)

    print(f"lives: {lives}")
    print(f"wrong guesses: {wrong_letters}")
    guess = input("Input a letter: ")
    while (not guess.isalpha()) or( 0 >= len(guess) >= 2) or (guess in previous_letters):
        guess = input("Incorrect Input! Type in a letter: ").strip().lower()
    previous_letters += guess

    if guess in word:
        print("Correct!")
        position = -1
        for x in range(word.count(guess)):
            position = word.index(guess, position+1)
            guessed_word.pop(position)
            guessed_word.insert(position, guess)
    else:
        print("Wrong! You lose a life!")
        wrong_letters += guess
        lives -= 1



if lives == 0:
    print("Uh Oh, You ran out of lives!")
else:
    print("YOU WIN! Well done!")
print(f"The word was '{word}'")