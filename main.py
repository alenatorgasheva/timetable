# Project - study
# University timetable

# Developed by A.Torgasheva

from load import Load

print('1 - загрузить данные\n'
      '2 - закончить работу')
choice = input()

if choice == '1':
    Load.ld_subjects('subjects.txt')
    Load.ld_students('students.txt')
    Load.ld_timetable('timetable_19704.1.txt')
    Load.ld_timetable('timetable_19704.2.txt')
    Load.ld_groups('students_groups.txt')
    while True:
        print('-' * 100)
        print('1 - список учащихся\n'
              '2 - расписание\n'
              '3 - список групп\n'
              '4 - выйти')
        choice = input()
        if choice == '1':
            for item in Load.lst_groups:
                print('-' * 100)
                print(item.students)
        elif choice == '2':
            for item in Load.lst_groups:
                print('-' * 100)
                print(item.timetable)
        elif choice == '3':
            for item in Load.lst_groups:
                print('-' * 100)
                print(item)
        elif choice == '4':
            break
