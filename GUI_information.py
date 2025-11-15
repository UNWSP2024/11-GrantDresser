##
# Program 1: GUI_information
# Grant Dresser
# 11/14/2025
## 

import tkinter

class GUI_information:
    def __init__(self):
        ## main window

        self.main_window = tkinter.Tk()
        self.main_window.geometry("300x200")
        self.main_window.title("My Information")

        ## frames for label and buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        ## holds name and address text
        self.info_var = tkinter.StringVar()

        self.info_label = tkinter.Label(self.top_frame,
                                        textvariable=self.info_var,
                                        borderwidth=2,
                                        relief="flat",
                                        padx=10,
                                        pady=10)

        ## buttons in the bottom frame
        self.show_button = tkinter.Button(self.bottom_frame,
                                          text="Show Info",
                                          command=self.show_info)

        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)

        ## display widgets (pack)
        self.info_label.pack()

        self.show_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.bottom_frame.pack()

        ## enter the tkinter main loop
        tkinter.mainloop()

    def show_info(self):
        """Callback for the Show Info button."""
        self.info_var.set("Grant Dresser\n"
                          "320 CloverLeaf Dr\n"
                          "Minneapolis, MN 55432")

## create instance of GUI_information
if __name__ == "__main__":
    info_gui = GUI_information()