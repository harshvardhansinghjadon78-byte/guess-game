import random
def play_game():
    number = random.randint(1,100)
    attempts =  0
    while True:
        guess = int(input('enter your number'))

        attempts += 1
        if guess < number:
            print('too low')
        elif guess > number:
            print('too high')
        else:
            print(f'congratulations! you guessed the number in {attempts} attempts.')
            break
    

play_game()            