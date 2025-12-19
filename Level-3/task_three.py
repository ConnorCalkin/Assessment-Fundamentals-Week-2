'''level three'''

from datetime import date
from abc import ABC, abstractmethod


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

        assessments_of_type = [
            assessment for assessment in self.assessments
            if isinstance(assessment, Assessment.get_assessment_type_from_string(type))]

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

    @staticmethod
    def get_assessment_type_from_string(type_string: str) -> Assessment:
        '''given a valid type string, it returns the associated type'''
        types = {
            "multiple-choice": MultipleChoiceAssessment,
            "technical": TechnicalAssessment,
            "presentation": PresentationAssessment
        }
        if type_string not in types:
            raise ValueError("Invalid Type")
        return types[type_string]

    @staticmethod
    def create_assessment_of_type(type_string: str, name: str, score: float) -> Assessment:
        '''factory method for producing appropriate sub-type'''
        assessment_type = Assessment.get_assessment_type_from_string(
            type_string)
        return assessment_type(name, score)


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


class Question:
    '''stores information related to a quiz question'''

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer

    def is_correct(self) -> bool:
        '''returns whether the answer chosen was correct'''
        return self.chosen_answer == self.correct_answer


class Quiz:
    '''stores data related to a quiz'''

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:
    '''functionality associated with marking a quiz'''

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz

    def mark(self) -> int:
        '''returns the score for the quiz as an integer percentage'''
        num_questions = len(self._quiz.questions)
        if num_questions == 0:
            return 0

        total = 0
        for question in self._quiz.questions:
            if question.is_correct():
                total += 1
        return int((total / num_questions) * 100)

    def generate_assessment(self) -> Assessment:
        '''generates the assessment based on the type of quiz'''
        return Assessment.create_assessment_of_type(self._quiz.type, self._quiz.name, self.mark())


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
