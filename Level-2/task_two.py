'''level two: using polymorphism'''

from datetime import date
from abc import ABC, abstractmethod

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####


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
        if isinstance(assessment, Assessment) is False:
            raise TypeError("You cannot input a non-assessment into the list")

        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        '''returns assessment with the same name as inputted'''
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        '''returns assessments that match the given type'''
        types = {
            "multiple-choice": MultipleChoiceAssessment,
            "technical": TechnicalAssessment,
            "presentation": PresentationAssessment
        }
        if type not in types:
            return ValueError("Invalid Types")

        assessments_of_type = [
            assessment for assessment in self.assessments
            if isinstance(assessment, types[type])]

        return assessments_of_type


class Assessment(ABC):
    '''handles the data for assessments'''

    def __init__(self, name: str, score: float):
        self._validate_score(score)
        self.name = name
        self.score = score

    def _validate_score(self, score: float):
        '''makes sure that the score is between 0 and 100'''
        min_score = 0
        max_score = 100
        if score < min_score or score > max_score:
            raise ValueError("Score must be between 0-100 inclusive")

    @abstractmethod
    def calculate_score(self):
        '''returns the score based on a weighting'''

#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


class MultipleChoiceAssessment(Assessment):
    '''multiple choice question'''

    def calculate_score(self):
        '''returns the score, with a weighting of 70%'''
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    '''technical assessment'''

    def calculate_score(self):
        '''returns the score with a weighing of 100'''
        return self.score


class PresentationAssessment(Assessment):
    '''presentation'''

    def calculate_score(self):
        '''returns the score with a weighting of 60%'''
        return self.score * 0.6


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
