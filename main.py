import json
import os

def readData(file_name: str) -> dict:
    """
    Takes JSON data and makes a Python dictionary

    returns dict{"category", "course-work"}
    """

    global data

    with open(file_name, "r") as file:
        data = json.load(file)

    return

def courseWorkAverage(category: str) -> tuple:
    """
    This calculates the specified category's average and weighted grade

    returns (average, weighed)
    """

    total = 0

    course_work = data["course-work"][category]
    weight = data["category"][category]

    for item in data["course-work"][category]:
        if item != None:
            total += item
    
    if len(course_work) - course_work.count(None) < 1:
        return (weight*100, weight*100)

    average = total/(len(course_work) - course_work.count(None))
    weighed = average * weight

    return (average, weighed)

def getCurrentAverage(*args) -> float:
    """
    Calculates your current course average, excluding ungraded assignments.

    returns course average
    """
    total = 0

    args[0].write('|Course-Work|Grade|\n|-|-|\n')
    
    for category in data["category"]:
        current = courseWorkAverage(category)[1]
        weigh = data["category"][category]

        args[0].write(f'|{category.upper()}|{current:.2f} / {weigh*100:.2f}|\n')

        total += current

    return round(total, 2)

def letterGrade(grade: float) -> str:
    letter = ""

    if grade < 60:
        letter = "F"
    elif grade < 70:
        letter = "D"
    elif grade < 80:
        letter = "C"
    elif grade < 90:
        letter = "B"
    else:
        letter = "A"

    gpa.append(letter)

    return letter

def predictGrade(value: float) -> float:
    grade = 0
    for category in data["category"]:
        total = 0

        course_work = data["course-work"][category]
        weight = data["category"][category]

        for item in data["course-work"][category]:
            if item != None:
                total += item
            else:
                total += value
        
        if len(course_work) - course_work.count(None) < 1:
            grade += value * weight
            continue

        average = total/(len(course_work))
        weighed = average * weight

        grade += weighed
    
    if grade > 100:
        return 100

    return grade

def threeGradeSummary(current_grade: float, *args):
    bareMinimum = predictGrade(60)
    average = predictGrade(current_grade)
    perfect = predictGrade(100)

    args[0].write(f'\nTHREE GRADE SUMMARY:')
    args[0].write(f'\n- 60: {bareMinimum:.2f}\n- average: {average:.2f}\n- 100: {perfect:.2f}\n')
    args[0].write("\n<br></br>\n")

def writeGradeResults(dir: str, *args):
    results = args[0]
    for file in os.listdir(dir):
        if file == "template.txt":
            continue
        
        readData(f'{dir}/{file}')

        results.write(f'# {file[:-5]}\n')

        # results.write("```")
        current_grade = getCurrentAverage(results)
        # results.write("```")
        
        results.write(f'\n## Current Grade: {current_grade} [{letterGrade(current_grade)}]\n')

        threeGradeSummary(current_grade, results)

        results.write('-'*10+'\n')

def gpaCalculate() -> float:
    total = 0.0

    for letter in gpa:
        if letter == "A":
            total += 4
        if letter == "B":
            total += 3
        if letter == "C":
            total += 2
        if letter == "D":
            total += 1

    return round(total / len(gpa), 3)

def selection(dir: str = "./courses/") -> str:
    years = os.listdir(dir)
    for i, year in enumerate(years):
        if os.path.isdir(dir+year):
            print(f"{i}) {year}")
    year_pick = int(input("\nWhich year: "))
    dir += years[year_pick] + "/"

    print()

    semesters = os.listdir(dir)
    for i, semester in enumerate(semesters):
        if os.path.isdir(dir+semester):
            print(f"{i}) {semester}")
    semester_pick = int(input("\nWhich semester: "))
    dir += semesters[semester_pick] + "/"

    return dir

def main():
    directory = selection()

    if os.path.exists("./results.md"):
        os.remove("results.md")
    
    with open("results.md", "w") as results:
        global gpa
        gpa = []
        writeGradeResults(directory, results)
        results.write(f"# Semester GPA: {gpaCalculate()}")

if __name__ == "__main__":
    main()
