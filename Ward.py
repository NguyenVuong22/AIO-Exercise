from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name}, yob = {self._yob}, grade = {self._grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Ward:
    def __init__(self, name: str):
        self.name = name
        self.listpeople = []

    def add_person(self, person: Person):
        self.listpeople.append(person)

    def describe(self):
        for p in self.listpeople:
            p.describe()

    def count_doctor(self):
        count = 0
        for i in self.listpeople:
            if isinstance(i, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.listpeople.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        count1 = 0
        sum_yob = 0
        for i in self.listpeople:
            if isinstance(i, Teacher):
                count1 += 1
                sum_yob += i._yob
        return ((sum_yob)/count1)


student1 = Student(name=" studentA ", yob=2010, grade="7")
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")

doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
assert ward1.count_doctor() == 1
ward1.add_person(doctor2)
ward1.count_doctor()

print("Number of doctors in ward1:", ward1.count_doctor())
print("List of people in ward1:")
ward1.describe()
print("\ nAfter sorting Age of Ward1 people ")
ward1.sort_age()
ward1.describe()

print(f"Average year of birth (teachers): {ward1.compute_average()}")
