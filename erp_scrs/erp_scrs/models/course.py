class Course:
    def __init__(self, cid, name, capacity):
        self.cid = cid
        self.name = name
        self.capacity = capacity
        self.enrolled = []  # list of student IDs

    def add_student(self, sid):
        if len(self.enrolled) < self.capacity:
            self.enrolled.append(sid)
        else:
            raise Exception("Course is full")

    def remove_student(self, sid):
        if sid in self.enrolled:
            self.enrolled.remove(sid)

    def to_dict(self):
        return {
            "cid": self.cid,
            "name": self.name,
            "capacity": self.capacity,
            "enrolled": self.enrolled
        }