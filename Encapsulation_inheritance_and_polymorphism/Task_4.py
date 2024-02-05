class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

  def rate_lecturer(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
          if course in lecturer.grades:
              lecturer.grades[course] += [grade]
          else:
              lecturer.grades[course] = [grade]
      else:
          return 'Ошибка'

  def average_grade(self):
    grade = 0
    number = 0
    for i in list(self.grades.values()):
      return sum(i)/len(i)


  def __str__(self):
    return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

  def __lt__(self, other_student):
    return self.average_grade() < other_student.average_grade()

  def __eq__(self, other_student):
    return self.average_grade() == other_student.average_grade()

  def __le__(self, other_student):
    return self.average_grade() <= other_student.average_grade()


class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []


class Lecturer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)
      self.grades = {}

  def average_grade(self):
    for i in list(self.grades.values()):
      return sum(i)/len(i)

  def __str__(self):
    return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'

  def __lt__(self, other_lecturer):
    return self.average_grade() < other_lecturer.average_grade()

  def __eq__(self, other_lecturer):
    return self.average_grade() == other_lecturer.average_grade()

  def __le__(self, other_lecturer):
    return self.average_grade() <= other_lecturer.average_grade()



class Reviewer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)

  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

  def __str__(self):
    return f'Имя: {self.name}\nФамилия: {self.surname}'


some_st1 = Student('Some', 'Buddy', 'm')
some_st2 = Student('Random', 'Dude', 'w')
some_lc1 = Lecturer('Cool', 'Teacher')
some_lc2 = Lecturer('Boring', 'Granny')
some_rw1 = Reviewer('Дядя', 'Петя')
some_rw2 = Reviewer('Олег', 'Вещий')

some_st1.courses_in_progress += ['Python']
some_st2.courses_in_progress += ['Python']
some_lc1.courses_attached += ['Python']
some_lc2.courses_attached += ['Python']
some_rw1.courses_attached += ['Python']
some_rw2.courses_attached += ['Python']
some_st1.courses_in_progress += ['Git']
some_st1.finished_courses += ['C++']

some_st1.rate_lecturer(some_lc1, 'Python', 10)
some_st2.rate_lecturer(some_lc2, 'Python', 6)
some_rw1.rate_hw(some_st1, 'Python', 9)
some_rw2.rate_hw(some_st2, 'Python', 8)

print(some_rw1)
print(some_lc1)
print(some_st1)

all_students = [some_st1, some_st2]
all_lecturers = [some_lc1, some_lc2]

def st_average_grade_for_course(all_students, course):
  sum_grade = 0
  number = 0
  for i in all_students:
    if course in i.grades:
      sum_grade += sum(i.grades[course])
      number += len(i.grades[course])
    else:
      'Студент не изучает данный курс'
  return sum_grade / number

def lt_average_grade_for_course(all_lecturers, course):
  sum_grade = 0
  number = 0
  for i in all_lecturers:
    if course in i.grades:
      sum_grade += sum(i.grades[course])
      number += len(i.grades[course])
    else:
      'Лектор не преподаёт данный курс'
  return sum_grade / number

print(st_average_grade_for_course(all_students, 'Python'))
print(lt_average_grade_for_course(all_lecturers, 'Python'))