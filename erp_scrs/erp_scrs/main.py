from storage.json_store import load_data, save_data
from utils.validators import validate_non_empty, validate_int, validate_positive
from utils.registration import register_course, drop_course
from storage.csv_store import export_students, export_courses
from analysis.analyzer import course_popularity, department_analysis, average_courses_per_student
from visual.charts import plot_course_popularity, plot_department_distribution


def add_student(data):
    try:
        sid = validate_non_empty(input("Enter Student ID: "), "Student ID")
        name = validate_non_empty(input("Enter Name: "), "Name")
        dept = validate_non_empty(input("Enter Department: "), "Department")

        if sid in data["students"]:
            print("❌ Student already exists!")
            return

        data["students"][sid] = {
            "sid": sid,
            "name": name,
            "dept": dept,
            "courses": []
        }

        print("✅ Student added!")

    except Exception as e:
        print("❌ Error:", e)


def add_course(data):
    try:
        cid = validate_non_empty(input("Enter Course ID: "), "Course ID")
        name = validate_non_empty(input("Enter Course Name: "), "Course Name")
        capacity = validate_int(input("Enter Capacity: "), "Capacity")
        capacity = validate_positive(capacity, "Capacity")

        if cid in data["courses"]:
            print("❌ Course already exists!")
            return

        data["courses"][cid] = {
            "cid": cid,
            "name": name,
            "capacity": capacity,
            "enrolled": []
        }

        print("✅ Course added!")

    except Exception as e:
        print("❌ Error:", e)


def register(data):
    try:
        sid = input("Enter Student ID: ")
        cid = input("Enter Course ID: ")
        register_course(data, sid, cid)
        print("✅ Registered successfully!")

    except Exception as e:
        print("❌ Error:", e)


def drop(data):
    try:
        sid = input("Enter Student ID: ")
        cid = input("Enter Course ID: ")
        drop_course(data, sid, cid)
        print("✅ Course dropped!")

    except Exception as e:
        print("❌ Error:", e)


def view_data(data):
    print("\n📚 Students:")
    for s in data["students"].values():
        print(s)

    print("\n📘 Courses:")
    for c in data["courses"].values():
        print(c)


def main():
    data = load_data()

    while True:
        print("\n===== ERP COURSE REGISTRATION SYSTEM =====")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Course")
        print("4. Drop Course")
        print("5. View Data")
        print("6. Export to CSV")
        print("7. Analytics")
        print("8. Visualization")
        print("9. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(data)

        elif choice == "2":
            add_course(data)

        elif choice == "3":
            register(data)

        elif choice == "4":
            drop(data)

        elif choice == "5":
            view_data(data)

        elif choice == "6":
            export_students(data)
            export_courses(data)
            print("✅ Exported to CSV!")

        elif choice == "7":
            course_popularity(data)
            department_analysis(data)
            average_courses_per_student(data)

        elif choice == "8":
            plot_course_popularity(data)
            plot_department_distribution(data)

        elif choice == "9":
            save_data(data)
            print("💾 Data saved. Exiting...")
            break

        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()