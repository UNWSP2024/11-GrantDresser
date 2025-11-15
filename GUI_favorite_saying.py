##
# Program 1: GUI_favorite_saying 
# Grant Dresser
# 11/14/2025
## 

import tkinter 

class GUI_favorite_saying:
    def __init__(self):
       ## main window
       self.main_window = tkinter.Tk()
       self.main_window.geometry("400x200")
       self.main_window.title("Favorite Saying") 

       ## lable with favorite saying and some stlying
       self.saying_label = tkinter.Label(
           self.main_window,
            text="Do the thing!",
            font =("Arial", 24,"bold"),
            fg="pink",
       )
       
       ## display label (pack)
       self.saying_label.pack()

       ## enter main loop
       tkinter.mainloop()

## create instance of GUI_favorite_saying
if __name__ == "__main__":
    gui = GUI_favorite_saying()

