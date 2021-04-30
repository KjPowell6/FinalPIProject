from tkinter import *

# create the entire class
class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # self.inputText = Entry(master)
        # self.outputText = Label(master, text = )



# create the input functionality
    self.inputText = Entry(master)
    self.inputText.bind("<Return>", self.process)
    self.inputText.grid(row = 0, column = 0)


# create the output functionality
    self.outputText = Label(master, text = "just a test")
    self.outputText.grid(row = 0, column = 1)


# create the microphone functionality
    self.microphoneStart = Button(master, text = "start", fg = "blue", bg = "green")
    self.microphoneStart.grid(row = 1, column = 0)

    self.microphoneStop = Button(master, text = "stop", fg = "blue", bg = "green")
    self.microphoneStop.grid(row = 1, column = 1)



######################################################
window = Tk()
window.geometry("800x800")
window.configure(bg = "white")
window.mainloop()
