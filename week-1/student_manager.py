"""
Your objective is to implement a class Student.
An object of this class records information about one student, such as name, student_id, and courses taken
with relative grades. It also allows to calculate the current GPA of the student.
"""

class Student:

    # This datastore structure is a Python "dictionary" and stores the correspondence between letter grades and points
    # Note: this datastore structure must be the same for all students, so it is declare outside __init__()
    POINTS = {'A+':4.3, 'A0':4.0,'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D0':1.0}


    def __init__(self, student_name, student_id):
        """
        create a new instance of the GPA calculator
        :param student_name: the name of the student
        :param student_id: the ID of the student
        """
        self._student_name = student_name
        self._student_id = student_id
        self._grades = {}                       # a dictionary of courses taken by the student and grades

    def get_student_name(self):
        """
        :return: the name of the student
        """
        return self._student_name
        pass

    def get_student_id(self):
        """
        :return: the id of the student
        """
        return self._student_id
        pass


    def get_gpa(self):
        """
        Calculates and returns the GPA of the student
        :return: the GPA (calculated as the point average of the courses passed by the student
        """
        if self._grades:
            total = 0
            courses_taken = 0
            for i in self._grades:
                total += self.POINTS[self._grades[i]]
                courses_taken += 1
            gpa = total/courses_taken
            return float("{0:.2f}".format(round(gpa,2)))
        else:
            print('No courses taken yet')
            return 0
        pass

    def add_grade(self, course_name, letter):
        """
        adds a new grade for a course passed by the student.
        an error is returned if course_name is already registered
        :param course_name: the name of the course pass
        :param letter: the letter grade achieved
        :return: a confirmation message (an error message  if the course is already registered)
        """
        if course_name in self._grades.keys():
            return (f"Error! {course_name} is already registered!")
        else:
            if letter in self.POINTS.keys():
                self._grades[course_name] = letter
                return (f'Success! {course_name} has been added.')
            else:
                return (f'"{letter}"" is not a valid letter grade!')
        pass

    def print_grades(self):
        """
        prints on the console the list of courses (with grades) passed by the student in a pretty format (which you
        are free to design)
        :return:
        """
        for i in self._grades:
            print(f'Course name: "{i}", Letter grade: "{self._grades[i]}"')
        pass

    def update_grade(self, course_name, letter):
        """
        This method checks if a letter grade is already registered for the course:
        if the a grade is already registered, then the letter grade is updated
        otherwise an error message is returned to the user, something like: "Grade not registered for course_name"
        """
        if course_name in self._grades.keys():
            if letter in self.POINTS.keys():
                self._grades[course_name] = letter
                return (f'Grade for "{course_name}" has been updated successfully!')
            else:
                return (f'"{letter}" is not a valid letter grade!')
        else:
            return (f'Error! Course "{course_name}" is not in grade-book!')    
        pass


    def get_count_of_above_bplus(self):
        """
        This function returns the number of courses passed by a student with a grade equal to or greater than B+
        """
        if self._grades:
            count = 0
            for i in self._grades.values():
                if self.POINTS[i] >= self.POINTS['B+']:
                    count += 1
            return count
        else:
            print('No courses taken yet')
            return 0
        pass

    def is_scholarship_ok(self):
        """
        this function returns a boolean value
        True if the student's GPA is greater than or equal to 3.3
        False otherwise
        :return:
        """
        if self.get_gpa() >= 3.3:
            return True
        else:
            return False
        pass



# ======================= END OF class definition ======================================================================

""" main() to test the implementation"""
if __name__ == '__main__':

    mc = Student("Marco Comuzzi","112235")

    # Add grade -> 'success'
    print(mc.add_grade("Apme","A+"))
    print(mc.add_grade("Math101", "A-"))
    print(mc.add_grade("Biology", "A-"))
    print(mc.add_grade("Chemistry", "A-"))

    # Add grade -> 'error'
    print(mc.add_grade("Italian101","4.3")) # invalid letter grade

    # Update grade -> 'success'
    print(mc.update_grade("Math101","B+"))
    
    # Update grade -> 'error'
    print(mc.update_grade("Uzbekcha101","B+"))# course is not in grade-book -> can't update
    print(mc.update_grade("Math101","4.3")) # invalid letter grade

    #calculate and print GPA
    print("{0} GPA is: {1}".format(mc.get_student_name(), mc.get_gpa()))

    # Above B+
    print(mc.get_count_of_above_bplus()) 

    # Scholarship status
    print(mc.is_scholarship_ok())

    #print grades
    mc.print_grades()

    # COMPLETE TO TEST OTHER METHODS