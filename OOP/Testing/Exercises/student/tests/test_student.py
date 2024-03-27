from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("John")
        self.student_with_courses = Student('Joe', {
            'a': ['oop'],
            'b': ['adv'],
            'c': ['db']
        })

    def test_init_if_no_courses(self):
        self.assertEqual({}, self.student.courses)

    def test_init_if_some_courses_added(self):
        self.assertEqual({'a': ['oop'], 'b': ['adv'], 'c': ['db']}, self.student_with_courses.courses)

    def test_init(self):
        self.assertEqual('John', self.student.name)
        self.assertEqual('Joe', self.student_with_courses.name)

    def test_if_enroll_func_returns_course_already_added_message(self):
        self.assertEqual("Course already added. Notes have been updated.", self.student_with_courses.enroll('a', 'f'))

    def test_if_note_are_appended_in_notes(self):
        self.student_with_courses.enroll('a', 'f')
        self.assertEqual({'a': ['oop', 'f'], 'b': ['adv'], 'c': ['db']}, self.student_with_courses.courses)

    def test_new_course_with_added_notes(self):
        self.student.enroll('f', ['note_1'], 'Y')
        self.assertEqual({'f': ['note_1']}, self.student.courses)

    def test_new_course_with_no_last_param(self):
        self.student.enroll('f', ['some_note'])
        self.assertEqual({'f': ['some_note']}, self.student.courses)

    def test_func_returns_string(self):
        self.assertEqual("Course and course notes have been added.", self.student.enroll('f', ['note_1'], 'Y'))

    def test_if_add_notes_has_another_info(self):
        self.student_with_courses.enroll('f', ['note_1'], 'ABC')
        self.assertEqual({'a': ['oop'], 'b': ['adv'], 'c': ['db'], 'f': []}, self.student_with_courses.courses)

    def test_if_func_returns_info_for_new_course(self):
        self.assertEqual("Course has been added.", self.student_with_courses.enroll('f', ['note_1'], 'ABC'))

    def test_add_notes_func_if_ok(self):
        self.student_with_courses.add_notes('a', 'basics')
        self.assertEqual(['oop', 'basics'], self.student_with_courses.courses['a'])

    def test_if_add_notes_func_returns_message(self):
        with self.assertRaises(Exception) as exception:
            self.student_with_courses.add_notes('z', 'basics')

        self.assertEqual("Cannot add notes. Course not found.", str(exception.exception))

    def test_leave_course_func_if_ok(self):
        self.student_with_courses.leave_course('a')
        self.assertEqual({'b': ['adv'], 'c': ['db']}, self.student_with_courses.courses)

    def test_leave_course_func_returns_error(self):
        with self.assertRaises(Exception) as exception:
            self.student_with_courses.leave_course('z')

        self.assertEqual("Cannot remove course. Course not found.", str(exception.exception))

if __name__ == '__main__':
    main()