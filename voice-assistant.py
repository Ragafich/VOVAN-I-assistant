from vosk import Model, KaldiRecognizer
import pyttsx3
import speech_recognition
import webbrowser
import command
import os
import json
import wave
import random

ttsEngine = pyttsx3.init()
recognizer = speech_recognition.Recognizer() #распознавание
microphone = speech_recognition.Microphone() #микрофон
voices = ttsEngine.getProperty("voices")
ttsEngine.setProperty("voice", voices[0].id)

def record_and_recognize_audio(*args: tuple): #функция записи и распознавания онлайн 
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
            recognized_data = use_offline_recognition()
        return recognized_data
    
def use_offline_recognition():#функция записи и распознавания оффлайн 

    recognized_data = ""
    try:
        # проверка наличия модели на нужном языке в каталоге приложения
        if not os.path.exists("model"):
            print("Please download the model from:\n"
                  "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
            exit(1)

        # анализ записанного в микрофон аудио (чтобы избежать повторов фразы)
        wave_audio_file = wave.open("microphone-results.wav", "rb")
        model = Model("model")
        offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())

        data = wave_audio_file.readframes(wave_audio_file.getnframes())
        if len(data) > 0:
            if offline_recognizer.AcceptWaveform(data):
                recognized_data = offline_recognizer.Result()

                # получение данных распознанного текста из JSON-строки
                # (чтобы можно было выдать по ней ответ)
                recognized_data = json.loads(recognized_data)
                recognized_data = recognized_data["text"]
    except:
        print("Sorry, speech service is unavailable. Try again later")

    return recognized_data

def play_voice_assistant_speech(text_to_speech): # говор этой скотины
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()




while True:
    voice_input =  record_and_recognize_audio()
    print(voice_input)
    if voice_input in command.PONY_PAGE:
        answer = 'по вашей просьбе открываю порнуху с понями'
        play_voice_assistant_speech(answer)
        webbrowser.open('https://ragafich.github.io/my-little-test/')
        print(answer)

    elif voice_input in command.END_PROGRAMM:
        play_voice_assistant_speech('Завершение по просьбе')
        exit('Завершение по просьбе')

    elif voice_input in command.GREETING:
        answer = random.choice(['Хай, чувак', 'Привет глупый человек'])
        play_voice_assistant_speech(answer)
        print(answer)

    else: pass
