class Student:
    def __init__(self, sid, name, dept):
        self.sid = sid
        self.name = name
        self.dept = dept
        self.courses = []  # list of course IDs

    def add_course(self, cid):
        if cid not in self.courses:
            self.courses.append(cid)

    def drop_course(self, cid):
        if cid in self.courses:
            self.courses.remove(cid)

    def to_dict(self):
        return {
            "sid": self.sid,
            "name": self.name,
            "dept": self.dept,
            "courses": self.courses
        }