import random
def main():
    while True:
        try:
            level = int(input("level: "))
            if level > 0:
                numbers_list = list(range(1, level + 1))
                random_number = random.choice(numbers_list)
                convert(random_number)
                break
            else:
                raise ValueError
        except ValueError:
            pass
def convert(x):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess > x:
                    print("Too large!")
                elif guess < x:
                    print("Too small!")
                elif guess == x:
                    print("Just right!")
                    break
            else:
                raise ValueError
        except ValueError:
            pass
main()

index = 0
for i in text:
    index+=1
    if i.isdigit():
        if i == 0:
            return False
        else:
            if text[index:].isdigit():
                return True
            else:
                return False
        