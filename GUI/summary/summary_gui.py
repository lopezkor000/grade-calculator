import tkinter as tk
import sys
sys.path.insert(0, '/Users/korie/Documents/VS-Code/Personal-Projects/grade-calculator')
from main import main

class SummaryMain(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent)
        self.frame = tk.LabelFrame(self.parent, text="Courses")
        self.frame.grid(row=0, column=0, padx=70, pady=10)
        self.showFrame = 0
        self.summary(self.showFrame)

    def next(self):
        self.showFrame += 1
        self.frame.destroy()
        self.frame = tk.LabelFrame(self.parent, text="Courses")
        if self.showFrame >= 0:
            self.summary(self.showFrame)

    def summary(self, num):
        sumGrades = main()
        for i, course in enumerate(sumGrades):
            course_name_label = tk.Label(self.frame, text=f"{course[0]}")
            course_name_label.grid(row=i, column=0)
            course_grade_label = tk.Label(self.frame, text=f"{course[1]}")
            course_grade_label.grid(row=i, column=1)

        for widget in self.frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        gpa_frame = tk.LabelFrame(self.parent, text="GPA")
        gpa_frame.grid(row=1, column=0, padx=20, pady=10)

        gpa_label = tk.Label(gpa_frame, text=f"{4.0}")
        gpa_label.grid(row=0, column=0)

        controls_frame = tk.Frame(self.parent)
        controls_frame.grid(row=2, column=0, padx=20, pady=10)

        prev_button = tk.Button(controls_frame, text="Prev")
        prev_button.grid(row=0, column=0, padx=20, pady=10)
        next_button = tk.Button(controls_frame, text=f"Next {num}", command=self.next)
        next_button.grid(row=0, column=1, padx=20, pady=10)
        