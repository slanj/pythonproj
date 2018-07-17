import datetime

class Person(object):
    def __init__(self, name):
        """Create person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        '''return self's last name'''
        return self.lastName

    def setBirthDay(self, month, day, year):
        '''sets self's birthday to birthDate '''
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        '''returns self's current age in days  '''
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically
        less than other's name, and False otherwise """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name """
        return self.name

class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    #sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance)

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = 'In cource ' + self.department + ' we say: '
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak('it is obvious that ' + topic)

class Grades(object):
    '''A mapping from students to a list of grades '''
    def __init__(self):
        '''Create empty grade book '''
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        '''Assumes: student is of type Student
        Add student to the grade book '''
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        '''Assumes: grade is a float
        Add grade to the list of grades for student '''
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        '''Return a list of grades for student '''
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def AllStudents(self):
        '''Return a list of the students in the grade book '''
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

def gradeReport(course):
    '''Assumes: course is of type Grades '''
    report = []
    for s in course.AllStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + '\'s mean is ' + str(average) )
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)

def isStudent(obj):
    return isinstance(obj, Student)


p1 = Person("Mark Zuckerberg")
p1.setBirthDay(5, 14, 84)
p2 = Person("Drew Houston")
p2.setBirthDay(3, 4, 83)
p3 = Person('Bill Gates')
p3. setBirthDay(10, 28, 55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')
p6 = Professor("Tim Berners Lee", "CS")

personList = [p1, p2, p3, p4, p5]
personList.sort()

for item in personList:
    print(item)

tom = UG("Tom", 1777)
print("Tom's class: ", tom.getClass())
print("Tom's type: ", type(tom))
print(isStudent(tom))
print(p6.speak("Awesome!"))

ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

super_grade = Grades()
super_grade.addStudent(g1)
super_grade.addStudent(ug2)
super_grade.addStudent(ug1)
super_grade.addStudent(g2)
super_grade.addStudent(ug4)
super_grade.addStudent(ug3)

super_grade.addGrade(ug1, 42)
super_grade.addGrade(ug2, 55)
super_grade.addGrade(ug3, 35)
super_grade.addGrade(ug4, 33)
super_grade.addGrade(ug1, 76)

print(gradeReport(super_grade))

