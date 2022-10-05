#Class variable and instance variable, instance method, instantiation
class one:
    name='mahmud' #class variable 

    def __init__(self):  #init method
        print('hello')  #instance variable 

    def fun(self):       #instance method
        print('i am instance method')

lol=one()  #instantiation
lol.fun()   #object

#access and chance class variable 
class one:
    name='mahmud' #class variable 

    def __init__(self):  #init method
        print('hello')  #instance variable 

    def fun(self):       #instance method
        print('i am instance method')

lol=one()  #instantiation
#one.name='hossain' #dynamically chance class variable 
print(one.name) #access class variable 
lol.fun()   #object

#cannot change class variable by object .varible . alwayas change class name. variable name
class one:
    name='mahmud' #class variable 

    def __init__(self):  #init method
        print('hello')  #instance variable 

    def fun(self):       #instance method
        print('i am instance method')

lol1=one()  #instantiation
lol2=one()
lol.name='hossain' #dynamically chance class variable 
print(lol1.name) #access class variable 
print(lol2.name) 
lol1.fun()   #object
lol2.fun() #object


#global and local in a class
class one:

    name='mahmud' #global variable
    def fun(self,x,y): #local variable 
        self.x=x
        self.y=y  #local variable 
        sum=x+y

lol=one()
lol.fun(1,2)
print(one.name) #call global variable outer function
print(sum) #call local variable outer funtion

#class methos example
#simple class mathod with parameter and its value
class one:
    name='mahmd' #class variable
    roll=12345

    def __init__(self):
        print('hello')
    @classmethod # class instance, it use above method must
    def fun(cls): #cls is alter of self, it also mandatory
        print(cls.name) #print class variable

lol=one()
lol.fun()

#simple class method without value
#simple class mathod
class one:

    def __init__(self):
        print('hello')

    @classmethod # class instance, it use above method must
    def fun(cls): #cls is alter of self, it also mandatory
        pass

lol=one()
lol.fun()

#nested funtiuon  example 
def fun1():
    print('hello')
    def fun2():
        print('hello2')
        def fun3():
            print('hello3')
            def fun4():
                print('hello4')
            fun4()
        fun3()
    fun2()

fun1()

#nested class example 
class one:
    def __init__(self):
        print('i am first class')
        class two:
            def __init__(self):
                print('i am second class')
                class three:
                    def __init__(self):
                        print('i am third class')
                lol=three()
        lol=two()
lol=one()

#nested class with instance method 
class one:
    def __init__(self):
        print('i am first class')
    def fun1(self):
        print('i am fun1')
        class two:
            def __init__(self):
                print('i am second class')
            def fun2(self):
                print('i am fun2')
                class three:
                    def __init__(self):
                        print('i am third class')
                    def fun3(self):
                        print('i am fun3')

                lol=three()
                lol.fun3()
        lol=two()
        lol.fun2()
lol=one()
lol.fun1()

#try to nested inheritance but not work 
class one:
    def __init__(self):
        print('i am first class')
    def fun1(self):
        print('i am fun1')
        class two:
            def __init__(self):
                print('i am second class')
            def fun(self):
                print('i am fun2')
                class three:
                    def __init__(self):
                        print('i am third class')
                    def fun(self):
                        print('i am fun3')

                lol=three(one,two)
                lol.fun()
        #lol=two()
        #lol.fun2()
#lol=three(one,two)
#lol.fun()

#different type of function example
#example function ,without parameter and print function
def fun():
    print('i am a print type function')
fun()

#example function , without parameter and return function
def fun1():
    return 'i am a return type function'
fun1()
print(fun1())

#example function ,with parameter and print function
def fun2(x,y):
    print(x+y)
fun2(2 ,2)

#example function , with parameter and return function
def fun3(x,y):
    return x+y
print(fun3(2,2))

#example,local variable function
def fun4():
    x=2
    y=2
    print(x+y)
fun4()

def fun4(x,y):
    print(x+y)
fun4(2,2)

#exaple, global variable function
x=2
y=2
def fun5():
    print(x+y)

fun5()
#lambda function some example 
print((lambda x,y: x + 2 * y)(2,3))

print((lambda x,y:x+y)(2,2))

lol=((lambda x,y:x+y)(3,3))
print(lol)

#not possible 
#def fun():
#    lol=((lambda x,y : x+y))
#    print(lol)
#fun(5,5) 


def fun(x,y):
    try:
        print(x/y)
    except (ZeroDivisionError,TypeError,NameError,ValueError):
        print('dont enter zero')
        print('dont enter string value')
fun(2,o)
fun(2,a)
fun(2,'a')

#special program, convert wav audio file to text 
import speech_recognition as sr

filename = "cool.wav"
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

#by default any string convert to english
from googletrans import Translator, constants
from pprint import pprint
# init the Google API translator
translator = Translator()
# translate a spanish text to english text (by default)
translation = translator.translate("আমি তোমাকে ভালো বাসি") #example: bangla to english
#translation = translator.translate("मैं तुम्हें पसंद करता हूं")     #example: hindi to english
#translation = translator.translate("私はあなたが好きです")    #example: japan to english
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")


#any string or language translating a specific language 
from googletrans import Translator, constants
from pprint import pprint
# init the Google API translator
translator = Translator()
translation = translator.translate("আমি তোমাকে ভালো বাসি", dest="ar") #bangla to arabic(ar)
#translation = translator.translate("আমি তোমাকে ভালো বাসি", dest="bn") #bangla to bangla(bn)
#translation = translator.translate("আমি তোমাকে ভালো বাসি", dest="en") #bangla to english(en)
#translation = translator.translate("আমি তোমাকে ভালো বাসি", dest="el") #bangla to greek(el)
#translation = translator.translate("আমি তোমাকে ভালো বাসি", dest="de") #bangla to garman(de)
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

#any specific source language  translating  to english
from googletrans import Translator, constants
from pprint import pprint
# init the Google API translator
translator = Translator()
# specify source language
#translation = translator.translate("আমি তোমাকে ভালো বাসি?", src="bn") #bangla
#translation = translator.translate("私はあなたが好きです", src="ja")    #japani
#translation = translator.translate("EGO amo te", src="la")  #latin
translation = translator.translate("أنا أحبك", src="ar")   #arabic
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

#to get extra information ,we use extra data funtion al last line
from googletrans import Translator, constants
from pprint import pprint
# init the Google API translator
translator = Translator()
# specify source language
translation = translator.translate("আমি তোমাকে ভালো বাসি?", src="bn") #bangla
#translation = translator.translate("私はあなたが好きです", src="ja")    #japani
#translation = translator.translate("EGO amo te", src="la")  #latin
#translation = translator.translate("أنا أحبك", src="ar")   #arabic
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
# print all translations and other data
pprint(translation.extra_data)

#convert english phase or more sentence to specific language with extra . function 
from googletrans import Translator, constants
from pprint import pprint
# init the Google API translator
translator = Translator()
# specify source language
# translate more than a phrase
sentences = [
    "Hello everyone",
    "How are you ?",
    "Do you speak english ?",
    "Good bye!"
]
translations = translator.translate(sentences, dest="en")
for translation in translations:
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
pprint(translation.extra_data)

#in here give any language sentence and found the language code
from googletrans import Translator, constants
from pprint import pprint
# init the Google API translator
# detect a language
translator = Translator()
#detection = translator.detect("नमस्ते दुनिया") #hindi code(hi)
detection = translator.detect("আমি তোমাকে ভালো বাসি ") # bangla code(bn)
#detection = translator.detect("EGO amo te") #latin code(la)
#detection = translator.detect("أنا أحبك")   #arabic code(ar)
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)

#in here give any language sentence and found the language code, and fun language
from googletrans import Translator, constants
from pprint import pprint
# init the Google API translator
# detect a language
translator = Translator()
#detection = translator.detect("नमस्ते दुनिया") #hindi code(hi)
detection = translator.detect("আমি তোমাকে ভালো বাসি ") # bangla code(bn)
#detection = translator.detect("EGO amo te") #latin code(la)
#detection = translator.detect("أنا أحبك")   #arabic code(ar)
print("Language code:", detection.lang)
print("Confidence:", detection.confidence)
print("Language:", constants.LANGUAGES[detection.lang])

#by this program we can find totall python language avaliable 
from googletrans import Translator, constants
from pprint import pprint
# print all available languages
print("Total supported languages:", len(constants.LANGUAGES))
print("Languages:")
pprint(constants.LANGUAGES)

#small audion wav file convert to text program
import speech_recognition as sr
filename = "lol.wav"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

#online text to  audio file convert 
import gtts
from playsound import playsound
# make request to google to get synthesis
tts = gtts.gTTS("Hello worlde i am mahmud hossain how are you")
# save the audio file
tts.save("hello.mp3")

#by this proram ,can easily read any english text as default spaking rate in offline
import pyttsx3
# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
text = "Python is a great programming language"
engine.say(text)
# play the speech
engine.runAndWait()

#by this proram ,can easily read any english text and show the default speaking rate in offline
import pyttsx3
# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
text = "Python is a great programming language"
engine.say(text)
# play the speech
engine.runAndWait()
# get details of speaking rate
rate = engine.getProperty("rate")
print(rate)

#by this program, easily read any english text with specific speaking rate in offline
import pyttsx3
# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
text = "hello i am mahmud hossain"
# setting new voice rate (faster)
engine.setProperty("rate", 1)
engine.say(text)
engine.runAndWait()

#create any thing QR code
import qrcode
# example data
data = "https://www.facebook.com/mahmud.hossain.12135/" #my fb id link
data='i am mahmud hossain' #any sentence 
# output file name
filename = "lol.png" #give file name and type
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)

#it take a QR code and decod it and show its data and also show the QR code also
import cv2
# read the QRCODE image
img = cv2.imread("si.png")
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)
print(data)

# display the result
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#if want to show blue or other color all side or QR code use this program
import cv2
# read the QRCODE image
img = cv2.imread("site.png")
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
# detect and decode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# if there is a QR code
if bbox is not None:
    print(f"QRCode data:\n{data}")
    # display the image with lines
    # length of bounding box
    n_lines = len(bbox)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img, point1, point2, color=(0,0,0), thickness=5)

# display the result
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#this code scan QR code by laptop camera
import cv2
# initalize the cam
cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)
    # check if there is a QRCode in the image
    if bbox is not None:
        # display the image with lines
        for i in range(len(bbox)):
            # draw all lines
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
        if data:
            print("[+] QR Code detected, data:", data)
    # display the result
    cv2.imshow("img", img)    
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

