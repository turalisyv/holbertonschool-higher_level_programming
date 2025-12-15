#!/usr/bin/python3
'''
My module document
'''


class CustomObject:
    '''
    My class document
    '''

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        import pickle

        with open(filename, mode="wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        import pickle

        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
            return data

        except Exception:
            return None
