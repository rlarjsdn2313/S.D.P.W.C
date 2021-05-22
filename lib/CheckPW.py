import hcskr

class CheckPW:
    def __init__(self, name, birth, local, school, kind):
        self.name = str(name)
        self.birth = str(birth)
        self.local = str(local)
        self.school = str(school)
        self.kind = str(kind)

    def check(self, password):
        result = hcskr.generatetoken(self.name, self.birth, self.local, self.school, self.kind, str(password))
        return result['error']

