import tkinter as tk
root = tk.Tk()
root.geometry("400x240")
root.config(bg='red')

def getTextInput():
    result=textExample.get("1.0","end")
    print(result)

textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read", 
                    command=getTextInput)

btnRead.pack()

root.mainloop()

result=textExample.get("1.0", "end")