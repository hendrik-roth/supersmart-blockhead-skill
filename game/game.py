"""Game class"""
import random

from .certificate_generator import CertificateGenerator


class Game:
    def __init__(self, category, skill_path):
        self.category = category
        self.path = skill_path
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
        path = f"{self.path}/game/questions/en-US"
        q_filename = f"{path}/red-light.txt" if self.category == "red-light" or self.category == "red light" else f"{path}/classic.txt"
        with open(q_filename, "r") as question_file:
            questions = question_file.readlines()
        return questions

    def ask_question(self) -> str:
        """
        ask random question

        :return: question
        :rtype: str
        """
        question = self.questions[random.randint(0, len(self.questions) - 1)]
        while question in self.asked_questions:
            question = self.questions[random.randint(0, len(self.questions) - 1)]
        self.counter += 1
        self.asked_questions[self.counter] = question
        return question

    def insert_answer(self, answer: str):
        """
        Insert answer for a question

        :param answer: answer of question
        """
        self.answers[self.asked_questions[self.counter]] = answer

    def generate_certificate(self):
        generator = CertificateGenerator(self.answers, self.path)
        path = generator.generate_certificate()
        return path
