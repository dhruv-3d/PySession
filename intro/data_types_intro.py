'''
Introduction
'''

student_name = 'Name Surname'
std_enroll_no = '201403100910068'
program_enrolled = 'B.Tech, Computer Engg'
program_term_length = 4
year_enrolled = 2014
year_passed_out = 2018
current_Semester = 7
current_class_faculty = 'Prof. Name Surname'
SGPA = 7.30
CGPA = 7.41


student_details = {
    'name': ["Dhruv", "Desai"],
    'enrollment_no': std_enroll_no,
    'enrolled_in': program_enrolled,
    'term_length': 4,
    'enrolled_from': 2014,
    'passed_out': 2018,
    'current_semester': 7,
    'sgpa': SGPA,
    'cgpa': CGPA
}


if __name__ == "__main__": 
    print(student_details['name'])
    for key, value in student_details.items():
        print(key, ": ", value)