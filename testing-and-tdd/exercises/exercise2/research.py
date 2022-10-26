
class ResearchSubjects:
    def __init__(self):
        self.collection = []

    def add(self, subject_to_add):
        assert self.find(subject_to_add.identifier) is None, f" Subject {subject_to_add.identifier} already exists"
        self.collection.append(subject_to_add)

    def find(self, identifier):
        return next(filter(lambda s: s.identifier == identifier, self.collection), None)

    def remove(self, identifier):
        self.collection = list(filter(lambda s: s.identifier != identifier, self.collection))

    def update(self, updated_subject):
        self.remove(updated_subject.identifier)
        self.add(updated_subject)


class ResearchSubject:
    def __init__(self, identifier, data):
        self.identifier = identifier
        self.data = data
