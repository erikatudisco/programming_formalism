
class ResearchSubjects:
    def __init__(self):
        self.collection = {}

    def add(self, subject_to_add):
        assert subject_to_add.identifier not in self.collection, f" Subject {subject_to_add.identifier} already exists"
        self.collection[subject_to_add.identifier]=subject_to_add

    def find(self, identifier):
        return self.collection.get(identifier)

    def remove(self, identifier):
        del self.collection[identifier]

    def update(self, updated_subject):
        self.remove(updated_subject.identifier)
        self.add(updated_subject)


class ResearchSubject:
    def __init__(self, identifier, data):
        self.identifier = identifier
        self.data = data
