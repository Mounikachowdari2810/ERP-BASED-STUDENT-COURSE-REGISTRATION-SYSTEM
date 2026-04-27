import matplotlib.pyplot as plt


def plot_course_popularity(data):
    names = []
    counts = []

    for c in data["courses"].values():
        names.append(c["name"])
        counts.append(len(c["enrolled"]))

    if not names:
        print("No data to plot")
        return

    plt.figure()
    plt.bar(names, counts)
    plt.title("Course Popularity")
    plt.xlabel("Courses")
    plt.ylabel("Number of Students")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


def plot_department_distribution(data):
    dept_count = {}

    for s in data["students"].values():
        dept = s["dept"]
        dept_count[dept] = dept_count.get(dept, 0) + 1

    if not dept_count:
        print("No data to plot")
        return

    labels = dept_count.keys()
    sizes = dept_count.values()

    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Department Distribution")
    plt.show()