import datetime
import os


def get_line(lines, pos):
    string = str(lines[pos])
    return string

def find_start(string):
    start_pos = string.find('.') + 2
    return start_pos

def find_end(string):
    end_pos = -1
    start = 0

    for _ in range(3):
        end_pos = string.find('-', start)
        start = end_pos + 1
    return end_pos - 1

def read_file():
    line_list = []
    base_path = os.path.dirname(__file__)
    homework_path = os.path.dirname(os.path.dirname(base_path))
    file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

    with open(file_path, 'r') as data_file:
        for line in data_file.readlines():
            line_list.append(line)
    return line_list

def get_date(line):
    return datetime.datetime.strptime(line[find_start(line): find_end(line)], "%Y-%m-%d %H:%M:%S.%f")


weekdays = {
    0: 'Понедельник',
    1: 'Вторник',
    2: 'Среда',
    3: 'Четверг',
    4: 'Пятница',
    5: 'Суббота',
    6: 'Воскресенье'
}

listed_lines = read_file()

print(get_date(get_line(listed_lines, 0)) + datetime.timedelta(days=7))
print(weekdays[get_date(get_line(listed_lines, 1)).weekday()])
print((datetime.datetime.today() - get_date(get_line(listed_lines, 2))).days)
