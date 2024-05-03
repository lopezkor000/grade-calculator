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
    
    for category in data["category"]:
        current = courseWorkAverage(category)[1]
        weigh = data["category"][category]

        # print(f'\n{category.upper()}: {current:.2f} / {weigh*100:.2f}\n')
        args[0].write(f'\n{category.upper()}: {current:.2f} / {weigh*100:.2f}\n')

        total += current

    return round(total, 2)

def predictGrade(value: float):
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

    return grade

def threeGradeSummary(current_grade: float, *args):
    bareMinimum = predictGrade(60)
    average = predictGrade(current_grade)
    perfect = predictGrade(100)

    args[0].write(f'\nTHREE GRADE SUMMARY:')
    args[0].write(f'\n- 60: {bareMinimum:.2f}\n- average: {average:.2f}\n- 100: {perfect:.2f}\n')
    args[0].write("\n"+"="*20+"\n")

def main():
    directory = "./courses"

    if os.path.exists("./results.txt"):
        os.remove("results.txt")
    
    with open("results.txt", "w") as results:
        for file in os.listdir(directory):
            readData(f'{directory}/{file}')

            # print(f'\n\n{"~"*6}[ {file[:-5]} ]{"~"*6}\n')
            results.write(f'\n\n{"~"*6}[ {file[:-5]} ]{"~"*6}\n')

            current_grade = getCurrentAverage(results)

            # print('-'*20)
            # print(f'Current Grade: {current_grade}')
            # print('-'*20, '\n')
            results.write('-'*20+f'\nCurrent Grade: {current_grade}\n'+'-'*20+'\n')

            threeGradeSummary(current_grade, results)

if __name__ == "__main__":
    main()
