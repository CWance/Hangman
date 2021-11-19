import random
from words import words
from hangman_visual import lives_visual_dict
import string
import turtle
from tkinter import messagebox

wn = turtle.Screen()
wn.title("Hangman")
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)

#Lives Pen
livesPen = turtle.Turtle()
livesPen.speed(0)
livesPen.color("white")
livesPen.penup()
livesPen.hideturtle()
livesPen.goto(0, 360)

#Current Words Pen
currentWordPen = turtle.Turtle()
currentWordPen.speed(0)
currentWordPen.color("white")
currentWordPen.penup()
currentWordPen.hideturtle()
currentWordPen.goto(0, -260)

#Gallow Pen
gallowPen = turtle.Turtle()
gallowPen.speed(0)
gallowPen.color("white")
gallowPen.penup()
gallowPen.hideturtle()
gallowPen.goto(-50, 0)

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7
    livesPen.write("You have {} lives left and you have used these letters: ".format(lives), align="center", font=("Courier", 12, "normal"))

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        wn.update()
        # letters used
        livesPen.clear()
        livesPen.write("You have {} lives left and you have used these letters: {}".format(lives, "".join(used_letters)), align="center", font=("Courier", 12, "normal"))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        gallowPen.write(lives_visual_dict[lives])
        wordList = "".join(word_list)
        currentWordPen.clear()
        currentWordPen.write("Current word: {}".format(wordList), align="center", font=("Courier", 12, "normal"))

        user_letter = turtle.textinput("Guess a letter", "")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                messagebox.showinfo("","Your letter {} is not in the word.".format(user_letter))

        elif user_letter in used_letters:
            messagebox.showinfo("","You have already used that letter. Guess another letter.")

        else:
            messagebox.showinfo("", "That is not a valid letter.")

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        messagebox.showinfo("","You died, sorry. The word was {}".format(word))

    else:
        messagebox.showinfo("", "YAY! You guessed the word {}!!".format(word))



if __name__ == '__main__':
    hangman()