from mycroft import MycroftSkill, intent_file_handler

from .game.game import Game
import webbrowser


class SupersmartBlockhead(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('blockhead.supersmart.intent')
    def handle_blockhead_supersmart(self, message):
        want_instructions = self.ask_yesno('want.instructions')
        if want_instructions == 'yes':
            self.speak_dialog('instructions')
        category = self.get_response('get.category')
        skill_path = self.root_dir
        game = Game(category, skill_path)
        for i in range(10):
            question = game.ask_question()
            answer = self.get_response('ask.question', {'question': question})
            game.insert_answer(answer)
        path = game.generate_certificate()
        webbrowser.open(path)
        self.speak_dialog('end.of.game')


def create_skill():
    return SupersmartBlockhead()
