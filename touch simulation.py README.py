touch simulation.py README.md requirements.txt
class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.performance = 0  # Initial performance score

    def study(self):
        # Simulate studying
        self.performance += 1  # Increment performance
