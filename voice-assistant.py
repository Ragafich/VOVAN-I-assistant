import speech_recognition
recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()
def record_and_recognize_audio(*args: tuple):
    with microphone:
        recognized_data = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=2)
        try:
            print("Вован слухает...")
            audio = recognizer.listen(microphone, 5, 5)
        except speech_recognition.WaitTimeoutError:
            print("МИКРО ДЕРЬМО")
            return
        try:
            print("Вован думает")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()
        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            print("ИНТЕРНЕТ В АУЛЕ ОТРУБИЛИ")
        return recognized_data
while True:
    voice_input = record_and_recognize_audio()
    print(voice_input)