class SubmissionItem:
    def __init__(self, id="", email="", date="", acceptance="", completion="", time="", cost="", file=""):
        self.id = id
        self.email = email
        self.date = date
        self.acceptance = acceptance
        self.completion = completion
        self.time = time
        self.cost = cost
        self.file = file

    def toJson(self):
        in_json = {
            "id": self.id,
            "email": self.email,
            "date": self.date,
            "acceptance": self.acceptance,
            "completion": self.completion,
            "time": self.time,
            "cost": self.cost,
            "file": self.file,
        }

        return in_json
    
    def toJson2(self):
        return self.__dict__