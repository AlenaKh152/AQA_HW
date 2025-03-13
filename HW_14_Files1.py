class Student:
    def __init__(self, name , group, marks):
        self.name = name
        self.group = group
        self.marks = marks

    def __str__(self):
        return f'{self.name}, {self.group}, {self.marks}'


student1 = Student('Tom', 'Group1', [5, 7, 8, 9, 8])
student2 = Student('Kate', 'Group1', [9, 8, 8, 7, 9])
student3 = Student('Bob', 'Group2', [7, 7, 9, 6, 10])
student4 = Student('Mary', 'Group2', [7, 9, 9, 10, 8])
student5 = Student('Lucy', 'Group2', [6, 8, 8, 7, 7])

students = [student1, student2, student3, student4, student5]

with open('C:/Users/Admin/Documents/AQA_HW/students.txt', 'w') as file:
    for student in students:
        file.write(student.__str__() + '\n')

groups = ['Group1', 'Group2']


def count_group_students():
    count_lst = []
    for group in groups:
        count = 0
        for student in students:
            if student.group == group:
                count += 1
        count_lst.append(f'{group}: {count} students.')
    return count_lst


all_students = f'All groups: {len(students)} students.'
group_students = (' ').join(count_group_students())


def average_group_mark():
    average_marks = []
    for group in groups:
        all_marks = []
        for student in students:
            if student.group == group:
                all_marks.extend(student.marks)
        group_average = (sum(all_marks) / len(all_marks))
        average_marks.append(f'{group}: average mark is {round(group_average, 2)}.')
    return average_marks


average = (' ').join(average_group_mark())

with open('C:/Users/Admin/Documents/AQA_HW/students.txt', 'a') as file:
    file.write(all_students + '\n')
    file.write(group_students + '\n')
    file.write(average + '\n')

with open('C:/Users/Admin/Documents/AQA_HW/students.txt', 'r') as file:
    for line in file:
        print(line)
