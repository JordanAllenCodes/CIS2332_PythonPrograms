# Jordan Allen
# PSID: 2040697

import csv
from datetime import datetime


class UniversityRoster:
    def __init__(self, item_list):  # get input as list
        self.student_list = item_list

    def print_full(self):  # Be sure to create a directory or file and copy and past that path into line 12
        with open('C:\\Users\\jorda\\OneDrive\\Desktop\\FullRoster.csv', 'w') as file:
            roster_students = self.student_list  # add to list
            roster_keys = sorted(roster_students.keys(), key=lambda x: roster_students[x]['last_name'])
            # sort the keys by taking the last_name identifier as the parameter
            for university_student in roster_keys:  # assign keys with values from input files
                student_id = university_student
                major = roster_students[university_student]['major']
                first_name = roster_students[university_student]['first_name']
                last_name = roster_students[university_student]['last_name']
                student_gpa = roster_students[university_student]['student_gpa']
                graduation_date = roster_students[university_student]['graduation_date']
                disciplinary_action = roster_students[university_student]['disciplinary_action']
                file.write('{},{},{},{},{},{},{}\n'.format(student_id, major, first_name,  # format and print to .csv
                                                           last_name, student_gpa,
                                                           graduation_date, disciplinary_action))

    def print_per_major(self):
        majors = self.student_list  # add to list
        majors_list = []  # create a list for majors
        major_keys = majors.keys()
        for university_student in majors:  # get each student's major
            major_type = majors[university_student]['major']
            if major_type not in majors_list:  # if major not in list then add to list
                majors_list.append(major_type)
        for new_major in majors_list:  # create file for each major and add the major name
            new_major.split()
            file_name = new_major.capitalize() + 'Students.csv'  # Be sure to update the path to your directory line 38
            with open('C:\\Users\\jorda\\OneDrive\\Desktop\\' + file_name, 'w') as file:
                for university_student in major_keys:  # assign keys
                    student_id = university_student
                    last_name = majors[university_student]['last_name']
                    first_name = majors[university_student]['first_name']
                    graduation_date = majors[university_student]['graduation_date']
                    disciplinary_action = majors[university_student]['disciplinary_action']
                    major_type = majors[university_student]['major']
                    if new_major == major_type:  # use the major_type key to match output to correct .csv file
                        file.write('{},{},{},{},{}\n'.format(student_id, last_name, first_name, graduation_date,
                                                             disciplinary_action))

    def print_scholarship_candidates(self):
        scholarship_students = self.student_list  # add to list and sort by student_gpa
        scholarship_keys = sorted(scholarship_students.keys(), key=lambda x: scholarship_students[x]['student_gpa'],
                                  reverse=True)  # use reverse to sort in descending order
        with open('C:\\Users\\jorda\\OneDrive\\Desktop\\ScholarshipCandidates.csv', 'w') \
                as scholarship_file:  # Update Path line 55
            for university_student in scholarship_keys:  # assign keys
                student_id = university_student
                last_name = scholarship_students[university_student]['last_name']
                first_name = scholarship_students[university_student]['first_name']
                major = scholarship_students[university_student]['major']
                student_gpa = scholarship_students[university_student]['student_gpa']
                disciplinary_action = scholarship_students[university_student]['disciplinary_action']
                acceptable = 3.8 < float(student_gpa)  # if student gpa meets standards pass as acceptable
                if acceptable and not disciplinary_action:  # if student acceptable and not checked for dis_action
                    scholarship_file.write(
                        '{},{},{},{},{}\n'.format(student_id, last_name, first_name, major, student_gpa))  # output .csv

    def print_disciplinary_action(self):
        disciplined_students = self.student_list  # add to list and sort by graduation_date
        discipline_keys = sorted(disciplined_students.keys(), key=lambda x: disciplined_students[x]['graduation_date'])
        with open('C:\\Users\\jorda\\OneDrive\\Desktop\\DisciplinedStudents.csv', 'w') \
                as disciplined_file:  # be sure to Update Path line 72
            for university_student in discipline_keys:  # assign keys
                student_id = university_student
                last_name = disciplined_students[university_student]['last_name']
                first_name = disciplined_students[university_student]['first_name']
                graduation_date = disciplined_students[university_student]['graduation_date']
                disciplinary_action = disciplined_students[university_student]['disciplinary_action']
                if disciplinary_action:  # if disciplinary action true output student to .csv file
                    disciplined_file.write('{},{},{},{}\n'.format(student_id, last_name, first_name, graduation_date))


if __name__ == '__main__':
    students = {}  # create dictionary
    input_files = ['C:\\Users\\jorda\\OneDrive\\Desktop\\StudentsMajorsList.csv',
                   'C:\\Users\\jorda\\OneDrive\\Desktop\\GPAList.csv',
                   'C:\\Users\\jorda\\OneDrive\\Desktop\\GraduationDatesList.csv']
    # Update path for input .csv files
    global gpa
    global main_student_id
    global main_last_name
    global main_first_name
    global min_gpa
    global max_gpa
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
    roster.print_full()  # output FullRoster .csv
    roster.print_per_major()  # output list per major .csv
    roster.print_scholarship_candidates()  # output ScholarshipCandidates  .csv
    roster.print_disciplinary_action()  # output DisciplinedStudents .csv

    major_types = []  # create list for major types
    uni_student_gpa = []  # create list for gpas
    for student in students:
        search_gpa = students[student]['student_gpa']
        search_major = students[student]['major']
        if search_gpa not in major_types:
            uni_student_gpa.append(search_gpa)
        if search_major not in major_types:
            major_types.append(search_major)

    query_input = None  # create variable for input
    while query_input != 'q':  # while user input is not q, query the user again
        query_input = input("Please enter the desired student(s) major and GPA, or enter 'q' to quit:\n")  # get input
        if query_input == 'q':  # if input is q, end program
            break  # end program
        else:
            query_gpa = None  # variable to hold gpa
            query_major = None  # variable to hold major
            query_input = query_input.split()  # split input to get major and gpa
            wrong_query_input = False  # variable to control wrong user input
            for word in query_input:
                if word in uni_student_gpa:
                    if query_gpa:
                        wrong_query_input = True  # wrong input
                    else:
                        query_gpa = word  # accept gpa
                elif word in major_types:
                    if query_major:
                        wrong_query_input = True  # wrong input
                    else:
                        query_major = word  # accept major
            if not query_gpa or not query_major or wrong_query_input:  # if no values are accepted or wrong input
                print('No such student')  # print no such student
            else:
                keys = students.keys()
                first_gpa = []  # create list for students within .1 of input gpa
                second_gpa = []  # create list for students within .25 0f input gpa
                no_satisfied_gpas = {}  # hold all students not within gpa range
                for student in keys:
                    if students[student]['major'] == query_major:  # if there is a major for the inputted major, proceed
                        today = datetime.now().date()  # get today
                        students_graduation_date = students[student]['graduation_date']  # get graduation dates
                        check_student_graduation_date = datetime.strptime(students_graduation_date, "%m/%d/%Y").date()
                        graduated_student = check_student_graduation_date < today  # scrub graduated students variable
                        min_gpa = float(query_gpa) - .1  # get min gpa requirements
                        max_gpa = float(query_gpa) + .1  # get max gpa requirements
                        second_min_gpa = min_gpa - .15  # get the second min gpa requirements
                        second_max_gpa = max_gpa + .15  # get the second man gpa requirements
                        if max_gpa >= float(students[student]['student_gpa']) >= min_gpa:  # if in range proceed
                            if not graduated_student and not students[student]['disciplinary_action']:  # requirements
                                first_gpa.append((student, students[student]))  # add to first list
                        if second_max_gpa >= float(students[student]['student_gpa']) >= second_min_gpa:  # set range
                            if not graduated_student and not students[student]['disciplinary_action']:  # requirements
                                second_gpa.append((student, students[student]))  # add to second list
                        else:
                            if not graduated_student and not students[student]['disciplinary_action']:
                                no_satisfied_gpas[student] = students[student]  # add to third list

                if first_gpa:  # if in the first_gpa list
                    for i in first_gpa:  # I was not able to get these list to iterate
                        student = first_gpa[0]  # get student
                        main_student_id = student[0]  # get student id
                        main_last_name = student[1]['last_name']  # get last name
                        main_first_name = student[1]['first_name']  # get student first name
                        gpa = student[1]['student_gpa']  # get student gpa
                        print("Your student(s): {}, {}, {}, {}".format(main_student_id, main_first_name,
                                                                       main_last_name, gpa))  # print results

                if second_gpa:  # if in second_gpa list
                    for i in second_gpa:
                        student = second_gpa[1]  # get student
                        main_student_id = student[0]  # get student id
                        main_last_name = student[1]['last_name']  # get student last name
                        main_first_name = student[1]['first_name']  # get student first name
                        gpa = student[1]['student_gpa']  # get student gpa
                        print('You may, also, consider: {}, {}, {}, {}'.format(main_student_id, main_first_name,
                                                                               main_last_name, gpa))  # print results

                    if no_satisfied_gpas:  # go to the remaining gpas within selected major
                        uni_stud_gpa = gpa  # set gpa
                        close_gpas = None  # create variable to hold gpas
                        closest_gpa_difference = None  # create variable to hold gpa difference
                        for student in no_satisfied_gpas:
                            if closest_gpa_difference is None:
                                close_gpas = no_satisfied_gpas[student]  # get the closest gpa to the input
                                closest_gpa_difference = abs(float(uni_stud_gpa) - float(no_satisfied_gpas[student]
                                                                                         ['student_gpa']))
                                main_student_id = student  # set student
                                main_last_name = no_satisfied_gpas[student]['last_name']  # set student last name
                                main_first_name = no_satisfied_gpas[student]['first_name']  # set student first name
                                gpa = no_satisfied_gpas[student]['student_gpa']  # set student gpa
                                continue
                            total_difference = abs(float(uni_stud_gpa) - float(no_satisfied_gpas[student]
                                                                               ['student_gpa']))
                            if total_difference < closest_gpa_difference:  # get the closest gpa to the inputted gpa
                                close_gpas = student
                                closest_gpa_difference = total_difference
                                main_student_id = student
                                main_last_name = no_satisfied_gpas[student]['last_name']
                                main_first_name = no_satisfied_gpas[student]['first_name']
                                gpa = no_satisfied_gpas[student]['student_gpa']
                        print('The closest option is: {}, {}, {}, {}\n'.format(main_student_id, main_first_name,
                                                                               main_last_name, gpa))  # print results
                else:
                    print('No such student')
