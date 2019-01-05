
from tkinter import *

class Window(Frame) :
    def __init__(self, master = None) :
        Frame.__init__(self, master)
        self.master = master
        self.init_window()  #Creating the actual window in the frame by calling the function

    def init_window(self) :
        self.master.title("[SG]SQUARE GAME")
        self.pack(fill = BOTH, expand = 1)
        B = [[0 for x in range(0,100,25)] for y in range(0,100,25)]
        print(B)
        k=0
        for i in range(4):
            for j in range(4):
                B[i][j] = Button(self, text = str(list_[k]))
                k+=1
                B[i][j].place(x = 25*i ,y = 25*j)
        #Creating a button and giving it a title, Button() is an inbuilt function
        #some_Button = Button(self, text = "Some Text On The Button")

        #Setting the position of the button on the screen, x and y are in pixels
        #some_Button.place(x = 80, y = 25)
root = Tk()
root.geometry("200x200")
app = Window(root)
root.mainloop()
