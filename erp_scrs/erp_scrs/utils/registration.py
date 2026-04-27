def register_course(data, sid, cid):
    # Check student exists
    if sid not in data["students"]:
        raise Exception("Student not found")

    # Check course exists
    if cid not in data["courses"]:
        raise Exception("Course not found")

    student = data["students"][sid]
    course = data["courses"][cid]

    # Check duplicate registration
    if cid in student["courses"]:
        raise Exception("Already registered for this course")

    # Check capacity
    if len(course["enrolled"]) >= course["capacity"]:
        raise Exception("Course is full")

    # Register
    student["courses"].append(cid)
    course["enrolled"].append(sid)


def drop_course(data, sid, cid):
    if sid not in data["students"]:
        raise Exception("Student not found")

    if cid not in data["courses"]:
        raise Exception("Course not found")

    student = data["students"][sid]
    course = data["courses"][cid]

    if cid not in student["courses"]:
        raise Exception("Student not enrolled in this course")

    student["courses"].remove(cid)
    course["enrolled"].remove(sid)