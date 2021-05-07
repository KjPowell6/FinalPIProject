from tkinter import *
from mtranslate import translate
from random import randint
from random import choice

# create the entire class
class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.pack(fill=BOTH, expand=1)
        # create the input functionality
        self.user_input = Entry(self, bg="white")
        self.user_input.bind("<Return>", self.translation)
        self.user_input.pack(side=BOTTOM, fill=X)
        self.user_input.focus()

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=600 // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        self.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        self.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

        # setup the text to the left of the GUI
        text_frame1 = Frame(self, width=600 // 2)
        self.text1 = Text(text_frame1, bg="white", state=DISABLED)
        self.text1.pack(fill=Y, expand=1)
        text_frame1.pack(side=LEFT, fill=Y)
        text_frame1.pack_propagate(False)
        # give the user some instructions for use
        self.text1.config(state=NORMAL)
        self.text1.insert(END, "Type the phrase you would like to" + "\n" + "translate "
                                                                            "then press enter/return to see the translation.")
        self.text1.config(state=DISABLED)

        # setup the buttons that will be used to enter study mode, select the language, and clear the screen
        study = Button(text="Study", padx=50, command=lambda : self.study())
        study.pack()
        clear = Button(text="Clear", padx=50, command=lambda : self.clear())
        clear.pack()

    # create a dictionary to save phrases and their translations
    # so the user can study them with flash cards
    phrases = []
    translatedPhrase = []
    def translation(self,ph):
        phrase = self.user_input.get()
        phrase = phrase.lower()
        translation = translate(phrase, 'es', 'auto')
        self.phrases.append(phrase)
        self.translatedPhrase.append(translation)
        self.text.config(state=NORMAL)
        self.text.insert(END, phrase + " --> " + translation + "\n")
        self.text.config(state=DISABLED)
        self.user_input.delete(0, END)

    def clear(self):
        self.text.config(state=NORMAL)
        self.text.delete('1.0', END)
        self.text.config(state=DISABLED)
        self.phrases.clear()
        self.translatedPhrase.clear()
        self.index = 0

    def study(self):
        for x in range(1, len(self.translatedPhrase)):
            self.numbers.append(x)
        # create the new window
        studyWindow = Tk()
        studyWindow.title("Study")
        studyWindow.geometry("300x300")
        studyWindow.configure(bg="white")
        # create a text widget to display the questions
        studyFrame = Frame(studyWindow, width=300)
        self.questionText = Text(studyFrame, bg="lightgrey", state=DISABLED)
        self.questionText.pack(fill=Y, expand=1)
        self.questionText.config(state=NORMAL)
        self.questionText.insert(END, self.translatedPhrase[self.index])
        print(self.index)
        print(self.numbers)
        self.questionText.config(state=DISABLED)
        self.studyInput = Entry(studyWindow, bg="white")
        self.studyInput.bind("<Return>", self.checkAnswer)
        self.studyInput.pack(side=BOTTOM, fill=X)
        studyFrame.pack(side=LEFT, fill=Y)
        studyFrame.pack_propagate(False)
        # randomly chose terms to study

    numbers = []
    numbers.append(0)
    index = choice(numbers)
    def checkAnswer(self, ph):
        userAnswer = self.studyInput.get()
        userAnswer = userAnswer.lower()
        questionAnswer = self.phrases[self.index]
        questionAnswer = questionAnswer.lower()
        if (userAnswer == questionAnswer) and (len(self.numbers) > 0):
            self.index = choice(self.numbers)
            self.numbers.remove(self.index)
            self.questionText.config(state=NORMAL)
            self.questionText.delete('1.0', END)
            self.questionText.insert(END, self.translatedPhrase[self.index])
            self.questionText.config(state=DISABLED)
            self.studyInput.delete(0, END)
        elif len(self.numbers) == 0:
            self.questionText.config(state=NORMAL)
            self.questionText.delete('1.0', END)
            self.questionText.insert(END, "You have successfully translated all the phrases!\n"
                                     + "You can close this window to exit.")
            self.questionText.config(state=DISABLED)
            self.studyInput.delete(0, END)
        else:
            self.questionText.config(state=NORMAL)
            self.questionText.delete('1.0', END)
            self.questionText.insert(END, self.translatedPhrase[self.index])
            self.questionText.config(state=DISABLED)
            self.studyInput.delete(0, END)



######################################################
window = Tk()
window.title("Translator")
window.geometry("600x600")
t = App(window)
window.configure(bg = "white")
window.mainloop()