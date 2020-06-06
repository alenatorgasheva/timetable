class Student:
    """Класс учащихся"""
    id = 1
    student_id = property()

    def __init__(self, full_name, birthday):
        """Инициализация"""
        self.__id = Student.id
        Student.id += 1
        self.__full_name = full_name
        self.__birthday = birthday

    def __str__(self):
        """Строковое представление"""
        s = '\n\t{}'.format(self.__full_name)
        return s

    @student_id.getter
    def student_id(self):
        return self.__id


class Subject:
    """Класс учебных дисциплин"""
    id = 1
    subject_id = property()

    def __init__(self, name, teacher, sub_type):
        """Инициализация"""
        self.__id = Subject.id
        Subject.id += 1
        self.__name = name
        self.__teacher = teacher
        self.sub_type = sub_type

    def __str__(self):
        """Строковое представление"""
        s = '{} ({})'.format(self.__name, self.__teacher)
        return s

    @subject_id.getter
    def subject_id(self):
        return self.__id


class Timetable:
    """Класс расписания звонков"""
    days = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА', 'СУББОТА', 'ВОСКРЕСЕНЬЕ']

    def __init__(self, study_days, start_time, count_class, class_len, break_len):
        """Инициализация"""
        self.timetable = Timetable.make_rings(study_days, start_time, count_class, class_len, break_len)

    def __str__(self):
        """Строковое представление"""
        s = ''
        for day in Timetable.days:
            s += '\n\t{}\n'.format(day)
            if day not in self.timetable:
                s += 'Выходной\n'
                continue
            for i in self.timetable[day]:
                s += '{} - {}\t'.format(self.timetable[day][i]['начало'], self.timetable[day][i]['конец'])
                if self.timetable[day][i]['предмет']:
                    s += '{}\n'.format(self.timetable[day][i]['предмет'])
                else:
                    s += '\n'
        return s

    @staticmethod
    def make_rings(study_days, start_time, count_class, class_len, break_len):
        """Создание расписания звонков"""
        rings = {}
        for day in range(study_days):
            rings[Timetable.days[day]] = {}
        for i in range(1, count_class + 1):
            for day in range(study_days):
                rings[Timetable.days[day]][str(i)] = {}
                rings[Timetable.days[day]][str(i)]['начало'] = start_time
                rings[Timetable.days[day]][str(i)]['конец'] = Timetable.plus(start_time, class_len)
                rings[Timetable.days[day]][str(i)]['предмет'] = ''
            start_time = Timetable.plus(start_time, class_len + break_len)
        return rings

    def add_class(self, day, class_number, subject):
        """Добавление предмета в расписание"""
        self.timetable[day][class_number]['предмет'] = subject

    @staticmethod
    def plus(time_0, minutes):
        """Изменение времени на несколько минут"""
        minutes = int(minutes)
        h, m = map(int, time_0.split(':'))
        m += minutes
        h += m // 60
        m = m % 60
        return '{}:{:02d}'.format(h, m)


class Group:
    """Класс групп учащихся"""
    number = property()
    students = property()
    timetable = property()

    def __init__(self, group_number, timetable):
        """Инициализация"""
        self.__group_number = group_number
        self.count_students = 0
        self.__timetable = timetable
        self.__students = []

    def __str__(self):
        """Строковое представление"""
        s = 'Группа {}\n'.format(self.__group_number)
        s += 'Количество учащихся: {}'.format(self.count_students)
        return s

    def __repr__(self):
        """Представление"""
        return self.__group_number

    @number.getter
    def number(self):
        return self.__group_number

    @students.getter
    def students(self):
        """Вывод списка учащихся группы"""
        s = '{}'.format(self)
        for person in self.__students:
            s += '{}'.format(person)
        return s

    @timetable.getter
    def timetable(self):
        """Вывод расписания группы"""
        s = 'Группа {}\n'.format(self.__group_number)
        s += '{}'.format(self.__timetable)
        return s

    def add_student(self, student):
        """Добавление учащегося к группе"""
        self.__students.append(student)
        self.count_students += 1
