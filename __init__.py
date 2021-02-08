from mycroft import MycroftSkill, intent_file_handler


class Hivemind(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hivemind.intent')
    def handle_hivemind(self, message):
        self.speak_dialog('hivemind')


def create_skill():
    return Hivemind()

