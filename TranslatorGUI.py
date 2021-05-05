from tkinter import *
from mtranslate import translate

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

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame1 = Frame(self, width=600 // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        self.text1 = Text(text_frame1, bg="white", state=DISABLED)
        self.text1.pack(fill=Y, expand=1)
        text_frame1.pack(side=LEFT, fill=Y)
        text_frame1.pack_propagate(False)
        # give the user some instructions for use
        self.text1.config(state=NORMAL)
        self.text1.insert(END, "Type the phrase you would like to" + "\n" + "translate "
                                                                            "then press enter/return to see the translation.")
        self.text1.config(state=DISABLED)

    # create a dictionary to save phrases and their translations
    # so the user can study them with flash cards
    allPhrases = {}
    def translation(self,ph):
        phrase = self.user_input.get()
        phrase = phrase.lower()
        translation = translate(phrase, 'es', 'auto')
        self.allPhrases[phrase] = translation
        self.text.config(state=NORMAL)
        self.text.insert(END, phrase + " --> " + translation + "\n")
        self.text.config(state=DISABLED)
        self.user_input.delete(0, END)


######################################################
window = Tk()
window.title("Translator")
window.geometry("600x600")
t = App(window)
window.configure(bg = "white")
window.mainloop()