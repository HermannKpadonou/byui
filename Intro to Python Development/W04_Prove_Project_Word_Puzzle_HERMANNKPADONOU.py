"""
Author: Brother Hermann
Purpose: W04 Prove: Project- Word Puzzle
"""
# Welcome to my word puzzle game
# Creativiy Activity
#allow players to replay or exit
# I added a function def play_game(): and break
def play_game():
    secret_word = 'mosiah'
    hint = '_ '*len(secret_word)
    guesses = int(0)
    print('Welcome to my word guessing game!')
    print()
    print(f'Your Hint is :{hint}')
    print()
    guess = input('What is your guess: ')
    guesses += 1
    while guess.upper() != secret_word.upper() and guesses < 6:
        if len(guess) != len(secret_word):
            print(f'Sorry,The word must have : {len(secret_word)} letters')
            guess = input('What is your guess: ')
            guesses += 1
        else:
            new_hint = ''
            for i in range (len(secret_word)):
                letter_guess = guess.upper()[i]
                letter_secret_word = secret_word.upper()[i]
                if letter_guess == letter_secret_word:
                    new_hint += letter_secret_word
                elif letter_guess in secret_word.upper():
                    new_hint += letter_guess.lower()
                else:
                    new_hint += '_'
            hint = new_hint
            print(f'Your Hint is :{hint}')
            guess = input('What is your guess: ')
            guesses += 1
    if guess.upper() == secret_word.upper():
        print(f'Well Done, You found the secret Word')
    else:
        if guesses == 6:
            print(f'Sorry, GAME OVER !!!')
            print('Next time will be good')
        print(f'The word was : {secret_word}')
    print(f'It took you {guesses} guesses.')
# Creativity Activity
play_game()
while True:
    replay = input("Press enter to replay or type 'quit' to exit: ")
    if replay.lower() == 'quit':
        break
    play_game()