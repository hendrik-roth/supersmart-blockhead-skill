from mycroft import MycroftSkill, intent_file_handler


class SupersmartBlockhead(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('blockhead.supersmart.intent')
    def handle_blockhead_supersmart(self, message):
        self.speak_dialog('blockhead.supersmart')


def create_skill():
    return SupersmartBlockhead()

