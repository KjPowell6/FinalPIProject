####################################################################################
# Final Pi Project
# Team 4
####################################################################################
from mtranslate import translate

class Translator:
    # create a dictionary to save phrases and their translations
    # so the user can study them with flash cards
    allPhrases = {}

    # ask the user for a phrase to translate
    def GetInput(self):
        userPhrase = input(str("What would you like to translate? "))
        return userPhrase

    # translate the phrase that was given in the GetInput function
    def Translate(self):
        while True:
            phrase = self.GetInput()
            translation = (translate(phrase, 'es', 'auto'))
            # add the phrase and the translation to the dictionary
            self.allPhrases[phrase] = translation
            print(translation)


########################################################################################
T1 = Translator()
T1.Translate()