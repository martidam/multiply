from random import randint

outer_count = 0
while outer_count < 5:

    num1 = randint(1, 10)
    num2 = randint(1, 10)
    product = num1 * num2

    print(f"Question {outer_count + 1}: What is {num1} x {num2}?")

    inner_count = 0

    while inner_count < 5:
        guess = int(input("Your answer: "))
        print(f"You answered: {guess}")

    if guess == product:
        print("Correct!")
        break
    else:
        print("Incorrect. Try again.")
        inner_count += 1

outer_count += 1 #