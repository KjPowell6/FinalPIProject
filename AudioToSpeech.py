import speech_recognition as sr
def speech_recog():
    # recognizer class
    r = sr.Recognizer()
    # Specifing the microphone to be activated
    mic = sr.Microphone(device_index=1)

    # listening to the user
    with mic as s:
        audio = r.listen(s, timeout=5)
        r.adjust_for_ambient_noise(s)

    # Converting the audio to text
    try:
        """I use google engine to convert the speech 
         text but you may use other engines such as 
         sphinx,IBM speech to text etc."""
        speech = r.recognize_google(audio)
        return speech

    """When engine couldn't recognize the speech 
    throws this"""
    except sr.UnknownValueError:
    # calling the text to speech function
    print("couldn't hear")


"""This error shows up when the microphone cant 
pick up any speech"""
except sr.WaitTimeoutError as e:\
    print("please try again")
