import random

def main():
    dice_rolls = 25
    dice_sum = 0
    count = 0
    for i in range(0, dice_rolls):
        if dice_sum < 100:
            roll = random.randint(1,6)
            dice_sum += roll
            count += 1
            if roll == 1:
                print(f'You rolled a {roll}, thats something')
            elif roll == 6:
                print(f'You rolled a {roll}, wowzers!')
            elif roll % 2 != 1:
                print(f'you rolled a {roll}, you can even split it evenly')
            else:
                print(f'You rolled a {roll}, try not to share it')
        else:
            pass
    print(f"Your total is {dice_sum} in {count} rolls. not bad!")
if __name__== "__main__":
  main()
