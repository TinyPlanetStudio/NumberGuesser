import random
import time
global number


print("Choose a difficulty. Easy/medium/hard/insane")
difficulty = input()
if difficulty.lower() == "easy":
    number = int(random.randint(1,10))
elif difficulty.lower() == "medium":
    number = int(random.randint(1,100))
elif difficulty.lower() == "hard":
    number = (random.randint(1,1000))
elif difficulty.lower() == "insane":
    number = (random.randint(1,10000))
with open(f"{difficulty.lower()}_leaderboard.txt", "r") as file:
    leaderboard = file.read()
if leaderboard == '':
    with open(f"{difficulty.lower()}_leaderboard.txt", "w") as file:
        file.write("100000000000")
StartTime = time.time()
def guess():
    print("Guess the number")
    UserGuess = int(input())
    if UserGuess > number:
        print("Too high")
        guess()
    elif UserGuess < number:
        print("Too low")
        guess()
    elif UserGuess == number:
        EndTime = time.time()
        FinalTime = EndTime - StartTime
        IntFinalTime = int(FinalTime)
        print("You won! Your final time was "+str(IntFinalTime)+" seconds!")
        with open(f"{difficulty.lower()}_leaderboard.txt", "r") as file:
            BestTime = file.read()
        IntBestTime = int(float(BestTime))
        FloatBestTime = float(BestTime)
        if IntBestTime > IntFinalTime:
            TimeDifference = FloatBestTime - FinalTime
            print(f"You beat the high score by {TimeDifference} seconds!")
            with open(f"{difficulty.lower()}_leaderboard.txt", "w") as file:
                file.write(str(FinalTime))
        elif IntBestTime < IntFinalTime:
            print("You did not beat your high score. Better luck next time!")
        exit()

guess()