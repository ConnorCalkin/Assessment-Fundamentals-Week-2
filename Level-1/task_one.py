'''level 1: create classes to assess candidates'''
from datetime import date


class Trainee:
    '''handles trainee data'''

    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self) -> int:
        '''returns the age of the trainee in years'''
        days_in_year = 365
        time_difference = date.today() - self.date_of_birth
        age = (time_difference).days // days_in_year
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        '''appends assessment onto assessments list'''
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        '''returns assessment with the same name as inputted'''
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


class Assessment:
    '''handles the data for assessments'''

    def __init__(self, name: str, type: str, score: float):
        self._validate_init(type, score)
        self.name = name
        self.type = type
        self.score = score

    def _validate_init(self, type: str, score: float):
        '''makes sure that the type is valid and score is between 0 and 100'''
        if type not in ["multiple-choice", "technical", "presentation"]:
            raise ValueError("Assessment type is not valid")
        min_score = 0
        max_score = 100
        if score < min_score or score > max_score:
            raise ValueError("Score must be between 0-100 inclusive")


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
