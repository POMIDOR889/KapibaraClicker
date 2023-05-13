from tkinter import *
from tkinter import messagebox,ttk
from threading import Thread
from playsound import playsound

def on_closing():
     if messagebox.askokcancel("Вы хотите выйти?", "Внимание весь прогресс будет потерян.Спасибо за игру! Разраб-Мулярчук Герман, или же Помидорка:)"):
        root.destroy()

root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title("Kapibara Clicker")
root.geometry("500x600")
root.resizable(0, 0)
root.iconbitmap("Kapibara.ico")
root.wm_attributes("-topmost", 1)
clicks=0
PUDGE=100
count=0.5
update=0.1
count2=0.9
update2=0.9

def click():
    global clicks
    clicks = round((clicks + update +update2),3)
    label['text'] = str(clicks) + '$'
    if clicks >= 10:
        Button(root, width=300, height=300, image=our_button, highlightthickness=0, bd=2, bg="Grey", command=click).place(x=180, y=100)
    if clicks >= 50:
        Button(root, width=300, height=300, image=our_button4, highlightthickness=0, bd=2, bg="Purple", command=click).place(x=180, y=100)
    if clicks >= 100:
        Button(root, width=300, height=300, image=our_button5, highlightthickness=0, bd=2, bg="Red", command=click).place(x=180, y=100)
    if clicks >= 500:
        Button(root, width=300, height=300, image=our_button6, highlightthickness=0, bd=2, bg="Yellow", command=click).place(x=180, y=100)
    if clicks >= 1000:
        Button(root, width=300, height=300, image=Fresko2, highlightthickness=0, bd=2, bg="Orange", command=click).place(x=180, y=100)

def dopclick():
    global clicks
    global update
    global count
    if clicks >= count:
        clicks = round((clicks - count),3)
        update = update + update/4
        count = update * 4
    label2['text'] = 'Цена:' + str(round(count, 3)) + '$'
    if update >= 0.899:
        Button(root, width=135, height=139,image=Energy, highlightthickness=0, bd=2, bg="Orange", command=dopclick).place(x=1, y=320)

def dopclickMEGA():
    global clicks
    global update2
    global count2
    if clicks >= count2:
        clicks = round((clicks - count2),5)
        update2 = update2 + update2/4
        count2 = update2 * 5
    label3['text'] = 'Цена:' + str(round(count2, 5)) + '$'
    if update2 >= 0.999999999:
        Button(root, width=184, height= 145,image=Tesla, highlightthickness=0, bd=2, bg="Orange", command=dopclickMEGA).place(x=150, y=410)

our_button4 =PhotoImage(file='../pythonProject22/Kapibara2.png')
our_button4 = our_button4.subsample(2, 2)
Box =PhotoImage(file='../pythonProject22/Cardboard-Box-PNG-Pic.png')
Box = Box.subsample(10, 10)
Tesla=PhotoImage(file='../pythonProject22/White-Tesla-Model-S-PNG-Picture.png')
Tesla= Tesla.subsample(3, 3)
Energy =PhotoImage(file='../pythonProject22/5d0018c3bd65f16b4860bcc0.png')
Energy = Energy.subsample(6, 6)
Fresko =PhotoImage(file='../pythonProject22/1661906225_6-papik-pro-p-smailik-s-krasnimi-glazami-png-6.png')
Fresko = Fresko.subsample(1, 1)
Fresko2 =PhotoImage(file='../pythonProject22/pngimg.com - elon_musk_PNG43.png')
Fresko2 = Fresko2.subsample(5, 5)
our_button5 =PhotoImage(file='../pythonProject22/Kapibara3.png')
our_button5 = our_button5.subsample(2, 2)
our_button6 =PhotoImage(file='../pythonProject22/pudge.png')
our_button6 = our_button6.subsample(4, 4)
Button(root, image=Fresko, width=500, height=600, highlightthickness=0, bd=1, bg="Orange").place(x=0, y=1)
our_button = PhotoImage(file='../pythonProject22/Kapibara.png')
our_button = our_button.subsample(2, 2)
Button(root, image=Box, width=300, height=300, highlightthickness=0, bd=2, bg="Black", command=click).place(x=180, y=100)
our_button2 = PhotoImage(file='../pythonProject22/pngimg.com - mandarin_PNG12.png')
our_button2 = our_button2.subsample(20, 20)
Button(root, image=our_button2, highlightthickness=0, bd=2, bg="grey", command=dopclick).place(x=1, y=320)
our_button3 = PhotoImage(file='../pythonProject22/kamaz_PNG49.png')
our_button3 = our_button3.subsample(1, 1)
Button(root, image=our_button3, highlightthickness=0, bd=2, bg="grey", command=dopclickMEGA).place(x=150, y=410)
label = Label(root, text=str(clicks)+'$',bg="Orange", font=('Times 30'))
label.pack(anchor='nw')
label2 = Label(root, text='Цена: '+str(round(count,3))+'$',bg="Orange", font=('Times 15'))
label2.pack(expand=True)
label2.pack(anchor='sw')
label3 = Label(root, text='Цена: '+str(round(count2,3))+'$',bg="Orange", font=('Times 18'))
label3.pack(expand=True)
label3.pack(anchor='s')
root.mainloop()
