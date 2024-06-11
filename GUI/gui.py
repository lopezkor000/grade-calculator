import tkinter as tk
from summary.summary_gui import SummaryMain

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Grades Summary")
        root = tk.Frame(self)
        root.pack()
        self.frames = {}
        for F in (SummaryMain, SummaryMain):
            page_name = F.__name__
            frame = F(parent=root)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0)
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()