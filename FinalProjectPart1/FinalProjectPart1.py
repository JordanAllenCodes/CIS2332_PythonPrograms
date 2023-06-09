# Jordan Allen

import csv


class UniversityRoster:
    def __init__(self, item_list):  # get input as list
        self.student_list = item_list

    def print_full(self):  # Be sure to create a directory or file and copy and past that path into line 12
        with open('C:\\Users\\jorda\\OneDrive\\Desktop\\FullRoster.csv', 'w') as file:
            roster_students = self.student_list  # add to list
            roster_keys = sorted(roster_students.keys(), key=lambda x: roster_students[x]['last_name'])
            # sort the keys by taking the last_name identifier as the parameter
            for student in roster_keys:  # assign keys with values from input files
                student_id = student
                major = roster_students[student]['major']
                first_name = roster_students[student]['first_name']
                last_name = roster_students[student]['last_name']
                student_gpa = roster_students[student]['student_gpa']
                graduation_date = roster_students[student]['graduation_date']
                disciplinary_action = roster_students[student]['disciplinary_action']
                file.write('{},{},{},{},{},{},{}\n'.format(student_id, major, first_name,  # format and print to .csv
                                                           last_name, student_gpa,
                                                           graduation_date, disciplinary_action))

    def print_per_major(self):
        majors = self.student_list  # add to list
        majors_list = []  # create a list for majors
        major_keys = majors.keys()
        for student in majors:  # get each student's major
            major_type = majors[student]['major']
            if major_type not in majors_list:  # if major not in list then add to list
                majors_list.append(major_type)
        for new_major in majors_list:  # create file for each major and add the major name
            new_major.split()
            file_name = new_major.capitalize() + 'Students.csv'  # Be sure to update the path to your directory line 38
            with open('C:\\Users\\jorda\\OneDrive\\Desktop\\' + file_name, 'w') as file:
                for student in major_keys:  # assign keys
                    student_id = student
                    last_name = majors[student]['last_name']
                    first_name = majors[student]['first_name']
                    graduation_date = majors[student]['graduation_date']
                    disciplinary_action = majors[student]['disciplinary_action']
                    major_type = majors[student]['major']
                    if new_major == major_type:  # use the major_type key to match output to correct .csv file
                        file.write('{},{},{},{},{}\n'.format(student_id, last_name, first_name, graduation_date,
                                                             disciplinary_action))

    def print_scholarship_candidates(self):
        scholarship_students = self.student_list  # add to list and sort by student_gpa
        scholarship_keys = sorted(scholarship_students.keys(), key=lambda x: scholarship_students[x]['student_gpa'],
                                  reverse=True)  # use reverse to sort in descending order
        with open('C:\\Users\\jorda\\OneDrive\\Desktop\\ScholarshipCandidates.csv', 'w') \
                as scholarship_file:  # Update Path line 55
            for student in scholarship_keys:  # assign keys
                student_id = student
                last_name = scholarship_students[student]['last_name']
                first_name = scholarship_students[student]['first_name']
                major = scholarship_students[student]['major']
                student_gpa = scholarship_students[student]['student_gpa']
                disciplinary_action = scholarship_students[student]['disciplinary_action']
                acceptable = 3.8 < float(student_gpa)  # if student gpa meets standards pass as acceptable
                if acceptable and not disciplinary_action:  # if student acceptable and not checked for dis_action
                    scholarship_file.write(
                        '{},{},{},{},{}\n'.format(student_id, last_name, first_name, major, student_gpa))  # output .csv

    def print_disciplinary_action(self):
        disciplined_students = self.student_list  # add to list and sort by graduation_date
        discipline_keys = sorted(disciplined_students.keys(), key=lambda x: disciplined_students[x]['graduation_date'])
        with open('C:\\Users\\jorda\\OneDrive\\Desktop\\DisciplinedStudents.csv', 'w') \
                as disciplined_file:  # be sure to Update Path line 72
            for student in discipline_keys:  # assign keys
                student_id = student
                last_name = disciplined_students[student]['last_name']
                first_name = disciplined_students[student]['first_name']
                graduation_date = disciplined_students[student]['graduation_date']
                disciplinary_action = disciplined_students[student]['disciplinary_action']
                if disciplinary_action:  # if disciplinary action true output student to .csv file
                    disciplined_file.write('{},{},{},{}\n'.format(student_id, last_name, first_name, graduation_date))


if __name__ == '__main__':
    students = {}  # create dictionary
    input_files = ['C:\\Users\\jorda\\OneDrive\\Desktop\\StudentsMajorsList.csv',
                   'C:\\Users\\jorda\\OneDrive\\Desktop\\GPAList.csv',
                   'C:\\Users\\jorda\\OneDrive\\Desktop\\GraduationDatesList.csv']  # Update path for input .csv files
    for individual_file in input_files:  # instructions for reading the files
        with open(individual_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')  # how to read file
            for line in csv_reader:
                main_student_id = line[0]  # each row contains student id
                if individual_file == input_files[0]:  # first input file and instructions for reading
                    students[main_student_id] = {}  # add student to dictionary
                    main_last_name = line[1]  # reading csv input file 1
                    main_first_name = line[2]  # reading csv input file 1
                    main_major = line[3]  # reading csv input file 1
                    main_disciplinary_action = line[4]  # reading csv input file 1
                    students[main_student_id]['last_name'] = main_last_name  # create identifier
                    students[main_student_id]['first_name'] = main_first_name  # create identifier
                    students[main_student_id]['major'] = main_major  # create identifier
                    students[main_student_id]['disciplinary_action'] = main_disciplinary_action  # create identifier
                elif individual_file == input_files[1]:  # second input file and instructions for reading
                    main_student_gpa = line[1]  # reading csv input file 2
                    students[main_student_id]['student_gpa'] = main_student_gpa  # create identifier
                elif individual_file == input_files[2]:  # third input file and instructions for reading
                    main_graduation_date = line[1]  # reading csv input file 3
                    students[main_student_id]['graduation_date'] = main_graduation_date  # create identifier

    roster = UniversityRoster(students)  # get access to the print functions in the UniversityRoster class.
    # call functions to output .csv files
    roster.print_full()  # output FullRoster .csv
    roster.print_per_major()  # output list per major .csv
    roster.print_scholarship_candidates()  # output ScholarshipCandidates  .csv
    roster.print_disciplinary_action()  # output DisciplinedStudents .csv
