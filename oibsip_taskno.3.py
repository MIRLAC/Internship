from tkinter import *

def send():
   send = "You-> "+e.get()
   txt.insert(END,"\n"+send)

   if(e.get()=='Hi'):
      txt.insert(END,"\n"+"Bot -> Hi, How can I help you?")
   elif(e.get()=='hi bot'):
      txt.insert(END,"\n"+"Bot -> Hi, How can I help you?")
   elif(e.get()=='how are you bot?'):
      txt.insert(END,"\n"+"Bot -> Hi, I'm fine, how are you?")
   elif(e.get()=='thank you'):
      txt.insert(END,"\n"+"Bot -> Do visit again")
   else:
      txt.insert(END,"\n"+"Bot -> Sorry I didn't get you")
    
   e.delete(0,END)


root = Tk()
root.configure(background="black")

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=100)
e.grid(row=1, column=0)

send_button = Button(root, text="SEND", command=send)
send_button.grid(row=1, column=1)
root.title("Chatbot")

root.mainloop()
