from pypresence import Presence
from tkinter import *
import time
import threading

start = int(time.time())
client_id = "1098592713106006047"
RPC = Presence(client_id)
RPC.connect()

tk = Tk()

# ButtonThread()
def thread():
    thread = threading.Thread(target=event)
    thread.daemon = True
    thread.start()

# Buttons
def event():
    if input_text.get() is None:
        label.configure(text = "Entry가 비어 있습니다.")
        
    else:
        button['text'] = 'Activating'
        while True:
            RPC.update(
                large_image = "3296160",
                large_text = "이것은 책이여",
                state = str(input_text.get()),
                start = start
            )
            time.sleep(60)

# Title
tk.title("Discord RPC")

# Label
label = Label(tk, text = "Discord RPC", font = ("맑은 고딕", 20, 'bold'))
label.pack(side = TOP)

# Input
input_text = Entry(tk, width = 50)
input_text.pack(pady = 10)

# Buttons
button = Button(tk, text = 'Activate', command = thread)
button.pack(fill = X, ipadx = 30, ipady = 30)

# GUI Resize
tk.geometry('400x300')
tk.resizable(False, False)

tk.mainloop() #pack tkinter
