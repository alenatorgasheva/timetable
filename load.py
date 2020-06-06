import codecs
from classes import Subject, Student, Timetable, Group


class Load:
    """Считывание данных"""
    lst_subjects = []
    lst_students = []
    lst_groups = []

    @classmethod
    def ld_subjects(cls, file_name):
        """Загрузка данных о предметах"""
        with codecs.open(file_name, encoding='utf-8') as fl:
            data = fl.readlines()
        for subject in data:
            name, sub_type, teacher = subject.strip().split(';')
            subject = Subject(name, teacher, sub_type)
            cls.lst_subjects.append(subject)

    @classmethod
    def ld_students(cls, file_name):
        """Загрузка данных об учащихся"""
        with codecs.open(file_name, encoding='utf-8') as fl:
            data = fl.readlines()
        for student in data:
            full_name, birthday = student.strip().split(';')
            student = Student(full_name, birthday)
            cls.lst_students.append(student)

    @classmethod
    def ld_timetable(cls, file_name):
        """Загрузка расписания"""
        with codecs.open(file_name, encoding='utf-8') as fl:
            data = fl.readlines()
        tt = Timetable(6, '09:00', 7, 95, 15)
        for lesson in data[1:]:
            day, class_number, subject_id = lesson.strip().split(';')
            subject_id = int(subject_id)
            for subject in cls.lst_subjects:
                if subject.subject_id == subject_id:
                    tt.add_class(day, class_number, subject)
                    break
        group = Group(data[0].strip(), tt)
        cls.lst_groups.append(group)

    @classmethod
    def ld_groups(cls, file_name):
        """Загрузка списка учащихся в группе"""
        with codecs.open(file_name, encoding='utf-8') as fl:
            data = fl.readlines()
        for group_student in data:
            student_id, group_num = group_student.strip().split(';')
            student_id = int(student_id)
            for student in cls.lst_students:
                if student.student_id == student_id:
                    for group in cls.lst_groups:
                        if group.number == group_num:
                            group.add_student(student)
                            break
                    break
