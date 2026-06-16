import random

secret_number = random.randint(1, 20)

# NEW: Start the player with 5 lives
lives = 5

print("📱 Welcome to the UPGRADED Guessing Game!")
print("I'm thinking of a number between 1 and 20. You have 5 lives!")

while True:
    # NEW: Every time they guess, subtract 1 life
    lives = lives - 1
    
    guess = int(input("\nTake a guess: "))
    
    if guess < secret_number:
        print(f"Too low! Remaining lives: {lives}")
    elif guess > secret_number:
        print(f"Too high! Remaining lives: {lives}")
    else:
        print(f"🎉 Correct! You won the game!")
        break
        
    # NEW: Check if the player is dead
    if lives == 0:
        print(f"💀 Game Over! The secret number was {secret_number}.")
        break
