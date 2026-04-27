import csv


def export_students(data):
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Student ID", "Name", "Department", "Courses"])

        for s in data["students"].values():
            writer.writerow([
                s["sid"],
                s["name"],
                s["dept"],
                ",".join(s["courses"])
            ])


def export_courses(data):
    with open("courses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Course ID", "Name", "Capacity", "Enrolled Count"])

        for c in data["courses"].values():
            writer.writerow([
                c["cid"],
                c["name"],
                c["capacity"],
                len(c["enrolled"])
            ])