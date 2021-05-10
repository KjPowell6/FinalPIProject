from tkinter import *
from mtranslate import translate
from random import randint
from random import choice

# create the entire class
class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # setup for most of the widgets being used
        # create the input functionality
        self.pack(fill=BOTH, expand=1)
        self.user_input = Entry(self, bg="white", font=10)
        self.user_input.bind("<Return>", self.translation)
        self.user_input.pack(side=BOTTOM, fill=X)
        self.user_input.focus()

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=600 // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        self.text = Text(text_frame, bg="lightgrey", font=14, state=DISABLED)
        self.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

        # setup the text to the left of the GUI
        text_frame1 = Frame(self, width=600 // 2)
        self.text1 = Text(text_frame1, bg="light sky blue", font=14, state=DISABLED)
        self.text1.pack(fill=Y, expand=1)
        text_frame1.pack(side=LEFT, fill=Y)
        text_frame1.pack_propagate(False)
        # give the user some instructions for use
        self.text1.config(state=NORMAL)
        self.text1.insert(END, "Type the phrase you would like to\ntranslate then press enter/return to see the translation." +
                          "\n\n\n\nUse the quiz button to test yourself on \nthe translations you've entered." +
                          "\n\n\n\nUse the learn button to review the \ntranslations in a flashcard style." +
                          "\n\n\n\nUse the dropdown menu to select the \nlanguage you'd like to translate your \nphrase to." +
                          "\n\n\n\nUse the clear button to erase the \ntranslations you've entered")
        self.text1.config(state=DISABLED)

        # setup the buttons that will be used for quiz mode, learn mode, selecting the language, and clearing the screen
        quiz = Button(text="Quiz", bg="orchid1", padx=50, command=lambda : self.quiz())
        quiz.pack(side=LEFT)
        # deletes the users previous translations
        clear = Button(text="Clear", bg="orchid1", padx=50, command=lambda : self.clear())
        clear.pack(side=RIGHT)
        # learn mode which is similar to flash cards
        learn = Button(text="Learn", bg="orchid1", padx=50, command=lambda : self.learn())
        learn.pack(side=LEFT)
        # drop down menu so the user can pick a language to translate to
        languages = ["Italian", "Spanish", "German", "French", "Swedish"]
        self.var = StringVar()
        self.var.set("Italian")
        drop = OptionMenu(master, self.var, *languages,)
        drop.config(bg="orchid1")
        drop.pack(side=RIGHT)

    # create a list to save phrases and their translations
    # so the user can study them with flash cards
    # or take quizzes
    phrases = []
    translatedPhrase = []

    # translate phrases and save them to respective lists
    def translation(self,ph):
        # get the language the user wants to translate to
        if self.var.get() == "Italian":
            language = 'it'
        elif self.var.get() == "Spanish":
            language = 'es'
        elif self.var.get() == "German":
            language = 'de'
        elif self.var.get() == "French":
            language = 'fr'
        else:
            language = 'sv'
        # get the users phrase, translate it, then show the translation
        # on the right side of the screen
        phrase = self.user_input.get()
        phrase = phrase.lower()
        translation = translate(phrase, language, 'auto')
        self.phrases.append(phrase)
        self.translatedPhrase.append(translation)
        self.text.config(state=NORMAL)
        self.text.insert(END, phrase + " --> " + translation + "\n")
        self.text.config(state=DISABLED)
        self.user_input.delete(0, END)

    # clear the users previously translated phrases
    def clear(self):
        self.text.config(state=NORMAL)
        self.text.delete('1.0', END)
        self.text.config(state=DISABLED)
        self.phrases.clear()
        self.translatedPhrase.clear()
        self.index = 0

    # create a window where the user will be quizzed
    def quiz(self):
        if len(self.translatedPhrase) == 0:
            # create the new window
            self.quizWindow = Tk()
            self.quizWindow.title("Quiz")
            self.quizWindow.geometry("160x20")
            self.quizWindow.configure(bg="red")
            self.quizFrame = Frame(self.quizWindow, width=200)
            self.quizLabel = Label(self.quizFrame, bg="red", text="There are no phrases to learn")
            self.quizLabel.pack()
            self.quizFrame.pack(side=LEFT, fill=Y)
            self.quizFrame.pack_propagate(False)
        else:
            for x in range(0, len(self.translatedPhrase)):
                self.numbers.append(x)
            self.index = choice(self.numbers)
            self.numbers.remove(self.index)
            # create the new window
            self.quizWindow = Tk()
            self.quizWindow.title("Quiz")
            self.quizWindow.geometry("300x180")
            self.quizWindow.configure(bg="white")
            # create a text widget to display the questions
            self.quizFrame = Frame(self.quizWindow, width=300)
            self.questionText = Text(self.quizFrame, bg="plum1", font=14, state=DISABLED)
            self.questionText.pack(fill=Y, expand=1)
            self.questionText.config(state=NORMAL)
            self.questionText.insert(END, self.translatedPhrase[self.index])
            self.questionText.config(state=DISABLED)
            self.quizInput = Entry(self.quizWindow, bg="white", font=14)
            self.quizInput.bind("<Return>", self.checkAnswer)
            self.quizInput.pack(side=BOTTOM, fill=X)
            self.quizFrame.pack(side=LEFT, fill=Y)
            self.quizFrame.pack_propagate(False)

    # a list to keep up with phrases when quizzing/learning
    numbers = []
    index = 0
    def checkAnswer(self, ph):
        userAnswer = self.quizInput.get()
        userAnswer = userAnswer.lower()
        questionAnswer = self.phrases[self.index]
        questionAnswer = questionAnswer.lower()
        # if the user answers the question right, go to the next question
        if (userAnswer == questionAnswer) and (len(self.numbers) > 0):
            self.index = choice(self.numbers)
            self.numbers.remove(self.index)
            self.questionText.config(state=NORMAL)
            self.questionText.delete('1.0', END)
            self.questionText.insert(END, self.translatedPhrase[self.index])
            self.questionText.config(state=DISABLED)
            self.quizInput.delete(0, END)
        # when they answer all the questions, let them know
        elif len(self.numbers) == 0 and (userAnswer == questionAnswer):
            self.questionText.config(state=NORMAL)
            self.questionText.delete('1.0', END)
            self.questionText.insert(END, "You have successfully translated all the \nphrases! \n\nYou can close this window to exit.")
            self.questionText.config(state=DISABLED)
            self.quizInput.destroy()
        # if they answer incorrectly, the question doesn't change
        else:
            self.questionText.config(state=NORMAL)
            self.questionText.delete('1.0', END)
            self.questionText.insert(END, (self.translatedPhrase[self.index] + "\nTry again"))
            self.questionText.config(state=DISABLED)
            self.quizInput.delete(0, END)

    # learn mode, similar to a flashcard
    # create variables text and card to keep up
    # with the cards that have been used
    buttonText = "Show Translation"
    card = 0
    def learn(self):
        if len(self.translatedPhrase) == 0:
            # create the new window
            self.learnWindow = Tk()
            self.learnWindow.title("Learn")
            self.learnWindow.geometry("160x20")
            self.learnWindow.configure(bg="red")
            self.learnFrame = Frame(self.learnWindow, width=200)
            self.learnLabel = Label(self.learnFrame, bg="red", text="There are no phrases to learn")
            self.learnLabel.pack()
            self.learnFrame.pack(side=LEFT, fill=Y)
            self.learnFrame.pack_propagate(False)
        else:
            # create the new window
            self.learnWindow = Tk()
            self.learnWindow.title("Learn")
            self.learnWindow.geometry("290x200")
            self.learnWindow.configure(bg="white")
            # create a frame to display the translated phrase
            self.learnFrame = Frame(self.learnWindow, width=290)
            self.learnText = Text(self.learnFrame, bg="plum1", font=14, state=NORMAL)
            self.learnText.pack(fill=Y, expand=1)
            self.learnText.insert(END, self.translatedPhrase[self.card])
            self.learnText.config(state=DISABLED)
            self.learnButton = Button(self.learnWindow, text=self.buttonText, padx=50, command=lambda : self.learnCheck())
            self.learnButton.pack(side=BOTTOM, fill=X)
            self.learnFrame.pack(side=LEFT, fill=Y)
            self.learnFrame.pack_propagate(False)

    def learnCheck(self):
        if (self.buttonText == "Show Translation") and (self.card < len(self.translatedPhrase)):
            self.learnButton['text'] = "Next"
            self.buttonText = "Next"
            self.learnText.config(state=NORMAL)
            self.learnText.insert(END, "\n\n" + self.phrases[self.card])
            self.learnText.config(state=DISABLED)
            self.card += 1
        elif (self.buttonText == "Next") and (self.card < len(self.translatedPhrase)):
            self.learnButton['text'] = "Show Translation"
            self.buttonText = "Show Translation"
            self.learnText.config(state=NORMAL)
            self.learnText.delete('1.0', END)
            self.learnText.insert(END, self.translatedPhrase[self.card])
            self.learnText.config(state=DISABLED)
        else:
            self.learnButton['text'] = "Exit"
            self.learnButton['command'] = lambda : self.learnWindow.destroy()
            self.buttonText = "Show Translation"
            self.learnText.config(state=NORMAL)
            self.learnText.delete('1.0', END)
            self.learnText.insert(END, "You have reviewed all the phrases." + "\nPress the exit button to close the window")
            self.learnText.config(state=DISABLED)
            self.card = 0



######################################################
window = Tk()
window.title("Translator")
window.geometry("600x600")
t = App(window)
window.configure(bg="white")
window.mainloop()
