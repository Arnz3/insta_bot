# GUI here but not todayy
from tkinter import *
from main import InstaBot

HEIGHT = 200
WIDTH = 350


def start_bot():
	user = username_e.get()
	pasw = password_e.get()
	hashtag = hashtag_e.get()
	freq = int(freq_e.get())
	ber = int(ber_e.get())
	pause = int(pause_e.get())

	bot = InstaBot("C:\Program Files (x86)\chromedriver.exe", user, pasw, hashtag, freq, ber, pause)
	bot.start()
	root.withdraw()


root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()


instabot = LabelFrame(root, text="INSTA-BOT", bd=5)
instabot.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.96)

username_l = Label(instabot, text="Username:")
username_l.place(relx=0.02, rely=0, relwidth=0.2)
username_e = Entry(instabot)
username_e.place(relx=0.25, rely=0, relwidth=0.7)

password_l = Label(instabot, text="Password:")
password_l.place(relx=0.02, rely=0.14, relwidth=0.2)
password_e = Entry(instabot)
password_e.place(relx=0.25, rely=0.14, relwidth=0.7)

hashtag_l = Label(instabot, text="Hashtag:")
hashtag_l.place(relx=0.02, rely=0.28, relwidth=0.2)
hashtag_e = Entry(instabot)
hashtag_e.place(relx=0.25, rely=0.28, relwidth=0.7)

freq_l = Label(instabot, text="frequentie:")
freq_l.place(relx=0.02, rely=0.42, relwidth=0.2)
freq_e = Spinbox(instabot, from_=5, to=15)
freq_e.place(relx=0.25, rely=0.42, relwidth=0.7)

ber_l = Label(instabot, text="bereik:")
ber_l.place(relx=0.02, rely=0.56, relwidth=0.2)
ber_e = Spinbox(instabot, from_=3, to=9)
ber_e.place(relx=0.25, rely=0.56, relwidth=0.7)

pause_l = Label(instabot, text="Pause:")
pause_l.place(relx=0.02, rely=0.7, relwidth=0.2)
pause_e = Spinbox(instabot, from_=1, to=10)
pause_e.place(relx=0.25, rely=0.7, relwidth=0.7)

start = Button(instabot, text="START", command= start_bot)
start.place(relx=0.4, rely=0.84, relwidth=0.2)

root.mainloop()