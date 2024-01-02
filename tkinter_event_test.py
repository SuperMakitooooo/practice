import tkinter

def event_handler(event):
    print(event)

app = tkinter.Tk()

for event_type in tkinter.EventType.__members__.keys():
    event_seq= "<" + event_type + ">"
    try:
        app.bind_all(event_seq, event_handler)
        print(event_type)
    except tkinter.TclError:
        #print("bind error:", event_type)
        pass

app.mainloop()
