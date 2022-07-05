import customtkinter
from PIL import Image, ImageTk  # <- import PIL for the images
import os
import speech_recognition as sr 
PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()  # create CTk window like you do with the Tk window (you can also use normal tkinter.Tk window)
app.geometry("450x450")
app.title("Smart wheelchair control")
# Creating button commands.
def button_functionUP():
    print("Moving upwards")
def button_functionDown():
    print("Moving downwards")
def button_functionLeft():
    print("Moving left")
def button_functionRight():
    print("Moving right")
def speakModeOn():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        command = r.recognize_google(audio)
        print("You said: " + command)
    if(command.lower().find("up" or "upwards") != -1):
        button_functionUP()
    elif(command.lower().find("down" or "downwards") != -1):
        button_functionDown()
    elif(command.lower().find("left" or "leftwards") != -1):
        button_functionLeft()
    elif(command.lower().find("right" or "rightwards") != -1):
        button_functionRight()
    elif(command.lower().find("stop") != -1):
        print("Stopping")
    else:
        print("I don't understand")
    
# load images as PhotoImage
image_size = 25
# add images to the button
up = ImageTk.PhotoImage(Image.open(PATH + "/test_images/up.png").resize((image_size, image_size)))
down = ImageTk.PhotoImage(Image.open(PATH + "/test_images/down.png").resize((image_size, image_size)))
left = ImageTk.PhotoImage(Image.open(PATH + "/test_images/left.png").resize((image_size, image_size)))
right = ImageTk.PhotoImage(Image.open(PATH + "/test_images/right.png").resize((image_size, image_size)))
command = ""
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1, minsize=200)

frame_1 = customtkinter.CTkFrame(master=app, width=250, height=240, corner_radius=15)
frame_1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

frame_1.grid_columnconfigure(0, weight=1)
frame_1.grid_columnconfigure(1, weight=1)
frame_1.grid_rowconfigure(0, minsize=10)  # adding a main frame.

frame_2 = customtkinter.CTkFrame(master=app, width=250, height=240, corner_radius=15)
frame_2.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

frame_2.grid_columnconfigure(0, weight=1)
frame_2.grid_columnconfigure(1, weight=1)
frame_2.grid_rowconfigure(0, minsize=10) # adding lower frame. 

button_1 = customtkinter.CTkButton(master=frame_1, image=up, text="", width=50, height=50,
                                   corner_radius=10, fg_color="gray40", hover_color="gray25", command=button_functionUP)
button_1.grid(row=1, column=1, columnspan=1, padx=20, pady=10, sticky="w")

button_3 = customtkinter.CTkButton(master=frame_1, image=left, text="", width=50, height=50,
                                   corner_radius=10, fg_color="gray40", hover_color="gray25", command=button_functionLeft)
button_3.grid(row=2, column=0, columnspan=1, padx=20, pady=10, sticky="w")

button_4 = customtkinter.CTkButton(master=frame_1, image=right, text="", width=50, height=50,
                                   corner_radius=10, fg_color="gray40", hover_color="gray25", command=button_functionRight)
button_4.grid(row=2, column=2, columnspan=1, padx=20, pady=10, sticky="e")

button_2 = customtkinter.CTkButton(master=frame_1, image= down, text="", width=50, height=50,
                                   corner_radius=10, fg_color="gray40", hover_color="gray25", command=button_functionDown)
button_2.grid(row=3, column=1, columnspan=1, padx=20, pady=10, sticky="w")

button_5 = customtkinter.CTkButton(master = frame_2, text = "Speak Mode", width = 50, height = 50, corner_radius = 10, fg_color = "gray40", hover_color = "gray25", command = speakModeOn)
button_5.grid(row = 4, column = 1, columnspan = 1, padx = 20, pady = 10, sticky = "w")

#labelInfo = customtkinter.CTkLabel(master=frame_2, text="Command given is: \n\n", fg_color=None, corner_radius=10, text_color="gray90", text_font= "Helvetica",justify=tkinter.LEFT)
#labelInfo.grid(row=0, column=0, padx=10, pady=10, sticky="nwe")



app.mainloop()
