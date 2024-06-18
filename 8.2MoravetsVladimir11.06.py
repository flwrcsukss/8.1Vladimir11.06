# class Teacher:
#     def __init__(self, name, education, exp):
#         self.__name = name
#         self.__education = education
#         self.__exp = exp
#
#     def get_name(self):
#         return self.__name
#
#     def get_education(self):
#         return self.__education
#
#     def get_exp(self):
#         return self.__exp
#
#     def set_exp(self, exp):
#         self.__exp = exp
#
#     def get_teacher_data(self):
#         return f'{self.__name}, образование {self.__education}, опыт работы {self.__exp}'
#
#     def add_mark(self, nameOfStudent, grade):
#         return f'{self.__name} поставил оценку {grade} студенту {nameOfStudent}'
#
#     def remove_mark(self, nameOfStudent, grade):
#         return f'{self.__name} удалил оценку {grade} студенту {nameOfStudent}'
#
#     def give_a_consultation(self, nameOfClass):
#         return f'{self.__name} провел консультацию в классе {nameOfClass}'
#
#
# teacher_1 = Teacher('Иван Петров', 'БГПУ', 4)
# print(teacher_1.get_teacher_data())
# teacher_1.set_exp(6)
# print(teacher_1.get_teacher_data())
# print(teacher_1.add_mark('Дориан Грей', 5))
# print(teacher_1.remove_mark('Родион Раскольников', 4))
# print(teacher_1.give_a_consultation('11А'))
# print()


class Teacher:
    def __init__(self, name, education, exp, discipline):
        self.__name = name
        self.__education = education
        self.__exp = exp
        self.__discipline = discipline
        # self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_exp(self):
        return self.__exp

    def get_discipline(self):
        return self.__discipline

    def set_exp(self, exp):
        self.__exp = exp

    def get_teacher_data(self):
        print(f'{self.__name}, образование {self.__education}, опыт работы {self.__exp}')

    def add_mark(self, nameOfStudent, grade):
        print(f'{self.__name} поставил оценку {grade} студенту {nameOfStudent}')

    def remove_mark(self, nameOfStudent, grade):
        print(f'{self.__name} удалил оценку {grade} студенту {nameOfStudent}')

    def give_a_consultation(self, nameOfClass):
        print(f'{self.__name} провел консультацию в классе {nameOfClass}')


class DisciplineTeacher(Teacher):

    def __init__(self, name, education, exp, discipline, job_title):
        super().__init__(name, education, exp, discipline)
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_exp(self):
        return self.__exp

    def get_discipline(self):
        return super().get_discipline()

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_teacher_data(self):
        super().get_teacher_data()
        return f'Предмет {super().get_discipline()}, должность {self.__job_title}'

    def add_mark(self, nameOfStudent, grade):
        super().add_mark(nameOfStudent, grade)
        return f'Предмет: {super().get_discipline()}'

    def remove_mark(self, nameOfStudent, grade):
        super().remove_mark(nameOfStudent, grade)
        return f'Предмет: {super().get_discipline()}'

    def give_a_consultation(self, nameOfClass):
        super().give_a_consultation(nameOfClass)
        return f'По предмету {super().get_discipline()} как {self.__job_title}'

teacher_2 = DisciplineTeacher('Иван Петров', 'БГПУ', 4, 'Химия', 'Директор')
print(teacher_2.get_teacher_data())
print()
print(teacher_2.add_mark('Вован', 4))
print()
print(teacher_2.remove_mark('Вовандопула', 3))
print()
print(teacher_2.give_a_consultation('10ъ'))