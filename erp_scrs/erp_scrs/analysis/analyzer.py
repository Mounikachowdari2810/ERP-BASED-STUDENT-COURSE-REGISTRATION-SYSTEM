import numpy as np
import pandas as pd


def course_popularity(data):
    print("\n📊 Course Popularity:")

    for c in data["courses"].values():
        print(f"{c['name']} → {len(c['enrolled'])} students")


def department_analysis(data):
    print("\n📊 Students per Department:")

    df = pd.DataFrame(data["students"].values())

    if not df.empty:
        print(df["dept"].value_counts())
    else:
        print("No data available")


def average_courses_per_student(data):
    print("\n📊 Average Courses per Student:")

    counts = [len(s["courses"]) for s in data["students"].values()]

    if counts:
        avg = np.mean(counts)
        print(f"Average courses: {avg:.2f}")
    else:
        print("No data available")