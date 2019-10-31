from guizero import App, TextBox, PushButton, Text
import speech_recognition as sr


def recognizethetext():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        ##print('say something')
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
            ##print('you said', text)
        output_box.value=text
        ##message.value=text

    except:
        print('Translation failed')
    

app = App(title="Transcriber", width=900, height=600, bg='white')
output_box=TextBox(app,text='Your text will appear here',height='fill', width='fill', multiline=True)
message=Text(app,text="This is a transcription app that makes your life easy @Kaya")
submit=PushButton(app,command=recognizethetext, text='Click and Transcribe')
app.display()





