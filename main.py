from tkinter import*
from tkinter import ttk
import cv2
import numpy as np
import pyautogui
import threading

root=Tk()
root.title('Py-Screen-Recorder')
root.geometry('600x500')
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )
root.config(bg='white')
#---------------------------------------------------------------------------
stop=1
name=0
SR=0
ASR=1
def recording():
    global stop,name,SR,ASR

    label.config(text='Recording..')
    label.config(fg='red')
    label.place(x=180,y=200)

    SCREEN_SIZE = (1920, 1080)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(f"output{name}.avi", fourcc, 20.0, (SCREEN_SIZE))
    def again():
        global SR
        cv2.destroyAllWindows()
        SR=0

    def change(bools):
        global SR
        close=ttk.Button(root,text='close the Window',command=lambda:again())
        close.place(x=450,y=100)
        if bools:
            SR+=1
    show=ttk.Button(root,text='Show Recording..',command=lambda:change(True))
    show.place(x=300,y=100)
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if SR==1:
            cv2.imshow("screenshot", frame)
            
        if cv2.waitKey(1) == ord("q") or stop==0:
            stop=1
            name+=1
            SR=0
            break
    cv2.destroyAllWindows()
    out.release()
def stopV():
    global stop
    stop=0
    label.config(text='Start Recording..')
    label.config(fg='green')
    label.place(x=115,y=200)

label=Label(root,text='Start Recording',bg='white',fg='green',font=('Comic Sans MS',30, 'bold'))
label.place(x=115,y=200)

record=ttk.Button(root,text='Start Recording..',command=lambda:threading.Thread(target=recording).start())
record.place(x=60,y=100)

stop=ttk.Button(root,text='stop..',command=lambda:threading.Thread(target=stopV).start())
stop.place(x=200,y=100)


root.mainloop()
