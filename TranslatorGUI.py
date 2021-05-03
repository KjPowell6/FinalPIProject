from tkinter import *
from mtranslate import translate

# create the entire class
class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # create the output functionality
        #self.outputText = Label(master, text="just a test")
        #self.outputText.grid(row=0, column=1)
#
        ## create the microphone functionality
        #self.microphoneStart = Button(master, text="start", fg="blue", bg="green")
        #self.microphoneStart.grid(row=1, column=0)
#
        #self.microphoneStop = Button(master, text="stop", fg="blue", bg="green")
        #self.microphoneStop.grid(row=1, column=1)


    def setup(self):
        self.pack(fill=BOTH, expand=1)
        # create the input functionality
        self.user_input = Entry(self, bg="white")
        self.user_input.bind("<Return>", self.translate())
        self.user_input.pack(side=BOTTOM, fill=X)
        self.user_input.focus()

    # create a dictionary to save phrases and their translations
    # so the user can study them with flash cards
    allPhrases = {}
    def translate(self):
        phrase = setup.user_input.get()
        phrase = phrase.lower()
        translation = translate(phrase, 'es', 'auto')
        self.allPhrases[phrase] = translation


######################################################
window = Tk()
window.title("Translator")
window.geometry("800x800")
t = App(window)
t.setup()
window.configure(bg = "white")
window.mainloop()