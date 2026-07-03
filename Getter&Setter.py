class Student:
    def __init__(self, age):
        self._age = age

    def set_age(self, age):
        if age > 18:
            self._age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self._age


s = Student(18)

s.set_age(25)

print(s.get_age())

s.set_age(9)
print(s.get_age())