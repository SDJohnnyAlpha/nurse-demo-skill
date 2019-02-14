from mycroft import MycroftSkill, intent_file_handler


class NurseDemo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('demo.nurse.intent')
    def handle_demo_nurse(self, message):
        self.speak_dialog('demo.nurse')


def create_skill():
    return NurseDemo()

