# inheretence

class first:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def prints(self):
        return f"the name is:{self.name} and id is:{self.id}"

class marks(first):
    def __init__(self,name,id,marks):
        super().__init__(name,id)
        self.marks=marks

    def total(self):
        return f"total marks is {self.marks}"

