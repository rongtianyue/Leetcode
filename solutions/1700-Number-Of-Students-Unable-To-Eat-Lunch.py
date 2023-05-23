class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        # Checks to see if students are in line
        while students:
            # If student's sandwich preference is matched
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
            else:
                students.append(students.pop(0))
                if students.count(students[0]) == len(students):
                    return len(students)

        return 0