import tkinter as tk

class SummaryMain(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        courses_frame = tk.LabelFrame(parent, text="Courses")
        courses_frame.grid(row=0, column=0, padx=70, pady=10)

        for i in range(4):
            course_name_label = tk.Label(courses_frame, text=f"Course {i}")
            course_name_label.grid(row=i, column=0)
            course_grade_label = tk.Label(courses_frame, text=f"Grade {i}")
            course_grade_label.grid(row=i, column=1)

        for widget in courses_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        gpa_frame = tk.LabelFrame(parent, text="GPA")
        gpa_frame.grid(row=1, column=0, padx=20, pady=10)

        gpa_label = tk.Label(gpa_frame, text=f"{4.0}")
        gpa_label.grid(row=0, column=0)

        controls_frame = tk.Frame(parent)
        controls_frame.grid(row=2, column=0, padx=20, pady=10)

        prev_button = tk.Button(controls_frame, text="Prev")
        prev_button.grid(row=0, column=0, padx=20, pady=10)
        next_button = tk.Button(controls_frame, text="Next")
        next_button.grid(row=0, column=1, padx=20, pady=10)
