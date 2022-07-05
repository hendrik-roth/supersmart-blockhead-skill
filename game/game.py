"""Game class"""
import random

from .certificate_generator import CertificateGenerator


class Game:
    def __init__(self, category, question_path):
        self.category = category
        self.path = question_path
        self.questions = self.load_questions()
        self.answers = {}  # e.g. {"<question>": <answer>, "2":...}
        self.asked_questions = {}  # e.g. {"1": <question>, "2":...}
        self.counter = 0

    def load_questions(self) -> list:
        """
        load questions based on category.
        Categories:
        - classic
        - red-light

        :return: questions as list
        :rtype: list
        """
        path = f"{self.path}/questions/en-US"
        q_filename = f"{path}/red-light.txt" if self.category == "red-light" else f"{path}/classic.txt"
        with open(q_filename, "r") as question_file:
            questions = question_file.readlines()
        return questions

    def ask_question(self) -> str:
        """
        ask random question

        :return: question
        :rtype: str
        """
        question = self.questions[random.randint(0, len(self.questions))]
        while question in self.asked_questions:
            question = self.questions[random.randint(0, len(self.questions))]
        self.counter += 1
        self.asked_questions[self.asked_questions.get(self.counter)] = question
        return question

    def insert_answer(self, answer: str):
        """
        Insert answer for a question

        :param answer: answer of question
        """
        self.answers[self.counter] = answer

    def generate_certificate(self):
        generator = CertificateGenerator(self.answers)
