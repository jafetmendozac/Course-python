import random


def main():
    number_question = 10
    try: 
        level= get_level("Level: ")
        score = generate_integer(level, number_question)
        if score != None:
            return print("Score:", score)
    except:
        pass

def get_level(prompt):
    while True:
        try:
            level = int(input(prompt))
            if(level > 0 and level < 4):
                return level
            else: 
                continue
        except ValueError:
            continue
        except EOFError:
            break

def generate_integer(level, number_question):
    score = 0
    guess = 0
    x=0
    y=0
    while number_question > 0:
        try:
            if(guess == 0):
                x = random.randint(0, 10**level-1)
                y = random.randint(0,10)
            response = int(input(f"{x} + {y} = "))
            correctAnswer = x + y
            if(correctAnswer == response):
                number_question -= 1
                score+=1
                guess=0
            else: 
                guess +=1
                print("EEE")
            if guess == 3:
                print(f"{x} + {y} =", correctAnswer)
                number_question -= 1
                guess=0
            if number_question == 0:
                return score
        except ValueError:
            print("EEE")
        except EOFError:
            break


if __name__ == "__main__":
    main()




# OPTIMIZATED
import random


def main():
    number_of_questions = 10
    level = get_level()

    score = 0
    for _ in range(number_of_questions):
        if ask_question(level):
            score += 1

    print("Score:", score)


def get_level():
    """Prompt user for difficulty level (1, 2, or 3)."""
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass  # just reprompt


def generate_integer(level):
    """Generate two random integers depending on the level."""
    start = 10 ** (level - 1) if level > 1 else 0
    end = 10**level - 1
    return random.randint(start, end), random.randint(start, end)


def ask_question(level):
    """Ask one math question, allow up to 3 tries."""
    x, y = generate_integer(level)
    correct_answer = x + y

    for _ in range(3):
        try:
            response = int(input(f"{x} + {y} = "))
            if response == correct_answer:
                return True
            else:
                print("EEE")
        except ValueError:
            print("EEE")

    # After 3 wrong tries
    print(f"{x} + {y} = {correct_answer}")
    return False


if __name__ == "__main__":
    main()
