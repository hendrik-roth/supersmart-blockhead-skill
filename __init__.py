from mycroft import MycroftSkill, intent_file_handler

from .game.game import Game


class SupersmartBlockhead(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('blockhead.supersmart.intent')
    def handle_blockhead_supersmart(self, message):
        want_instructions = self.ask_yesno('want.instructions')
        if want_instructions:
            self.speak_dialog('instructions')
        category = self.get_response('get.category')
        path_to_questions = self.file_system
        game = Game(category, path_to_questions)
        for i in range(5):
            question = game.ask_question()
            answer = self.get_response('question', {'question': question})
            game.insert_answer(answer)
        game.generate_certificate()
        self.speak_dialog('end.of.game')


def create_skill():
    return SupersmartBlockhead()
