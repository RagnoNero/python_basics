"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

subj = {}
get_value = lambda s: int(s[:s.index('(')]) if '(' in s else 0

with open('file_6.txt', 'r', encoding='utf-8') as file:
    for line in file:
        subject, lecture, practice, lab = line.split()
        subject = subject[:-1]
        lecture = get_value(lecture)
        practice = get_value(practice)
        lab = get_value(lab)
        subj[subject] = lecture + practice + lab
    print(f'Total number of hours per subject: {subj}')
