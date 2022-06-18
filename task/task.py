class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_course(self, course_name):
        if course_name not in self.courses_in_progress:
            self.courses_in_progress.append(course_name)

    def fin_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.finished_courses.append(course_name)
            self.courses_in_progress.remove(course_name)


    def rate_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = "Имя: " + self.name + '\n'
        result += "Фамилия: " + self.surname + '\n'
        all_grades = []
        for i in self.grades:
            all_grades.extend(self.grades[i])
        average = sum(all_grades) / len(all_grades)
        result += 'Средняя оценка за домашние задания: ' + str(average) + '\n'
        result += 'Курсы в процессе изучения: ' + ', '.join(self.courses_in_progress) + '\n'
        result += 'Завершенные курсы: ' + ', '.join(self.finished_courses) + '\n'

        return result
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def course_add(self, course_name):
        self.courses_attached.append(course_name)

 
class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}

    def __str__(self):
        result = "Имя: " + self.name + '\n' + "Фамилия: " + self.surname
        all_grades = []
        for i in self.grades:
            all_grades.extend(self.grades[i])
        average = sum(all_grades) / len(all_grades)
        result += '\n' + 'Средняя оценка за лекции: ' + str(average)
        return result


class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)


    def __str__(self):
        result = "Имя: " + self.name + '\n' + "Фамилия: " + self.surname
        return result
        


    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Compare:
    def _average(unit):
        all_grades = []
        for i in unit.grades:
            all_grades.extend(unit.grades[i])
        if len(all_grades) > 0:
            return sum(all_grades) / len(all_grades)
        else:
            return 0


    def compare(unit_1, unit_2):
        if Compare._average(unit_1) >= Compare._average(unit_2):
            top = unit_1
        else:
            top = unit_2
        return 'Лучший: ' + str(top.name + ' ' + str(top.surname))

    def average_on_course(course, *args):
        units = []
        all_grades = []
        for arg in args:
            units.append(arg)
        for unit in units:
            if course in unit.grades:
                all_grades.extend(unit.grades[course])
        if len(all_grades) > 0:
            return sum(all_grades) / len(all_grades)
        else:
            return 0
        





lector_1 = Lecturer('Vasily', 'Petrov')
lector_2 = Lecturer('Gondar', 'Roshanovitch')
lector_1.course_add('Biology')
lector_1.course_add('Phisical')
lector_1.__str__

student_1 = Student('Ivanka', 'Petrova', 'female')
student_2 = Student('Alex', 'Simonov', 'male')

student_2.add_course('Physical')
student_2.add_course('Anatomy')
student_2.add_course('MAth')
student_2.fin_course('MAth')
student_2.__str__

student_1.add_course('Biology')
student_1.add_course('Physical')
student_1.rate_lector(lector_1, 'Biology', 10)

reviewer_1 = Reviewer('Volodya', 'Maslov')
reviewer_1.course_add('Physical')
reviewer_1.course_add('Biology')
reviewer_1.__str__
reviewer_1.rate_student(student_1, 'Physical', 5)
reviewer_1.rate_student(student_2, 'Physical', 9)
reviewer_1.rate_student(student_2, 'Physical', 3)
reviewer_1.rate_student(student_2, 'Physical', 8)
reviewer_1.rate_student(student_1, 'Biology', 4)



# print(Compare.compare(student_1, student_2))
# print(Compare.compare(lector_1, lector_2))

# print(Compare.average_on_course('Physical', student_1, student_2))
# print(Compare.average_on_course('Physical', lector_1, lector_2))

# print(student_1.grades['Biology'])
# print(student_2.grades['Physical'])