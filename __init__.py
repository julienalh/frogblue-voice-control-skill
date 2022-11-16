from mycroft import MycroftSkill, intent_file_handler


class FrogblueVoiceControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.voice.frogblue.intent')
    def handle_control_voice_frogblue(self, message):
        self.speak_dialog('control.voice.frogblue')


def create_skill():
    return FrogblueVoiceControl()

