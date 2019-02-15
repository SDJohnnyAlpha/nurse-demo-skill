# UPMC Nurse Demo v0.1
# Developer: Stephen Barnes
# Date: February 15th 2019

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

Logger = getLogger(__name__)

class NurseDemoSkill(MycroftSkill):
    def __init__(self):
        super(NurseDemoSkill, self).__init__(name="NurseDemo")

        def initialize(self):

            where_am_i_intent = IntentBuilder("WhereAmIintent").
                require("where.am.i").build()
                self.register_intent(where_am_i_intent, self.handle_where_am_i_intent)
            the_nurse_is_intent = IntentBuilder("TheNurseIsintent").
                require("the.nurse.is").build()self.register_intent(the_nurse_is_intent, self.handle_the_nurse_is_intent)
            the_doctor_is_intent = IntentBuilder("TheDoctorIsintent").
                require("the.doctor.is").build()self.register_intent(the_doctor_is_intent, self.handle_the_doctor_is_intent)
            go_home_intent = IntentBuilder("GoHomeIntent").
                require("go.home").build()self.register_intent(go_home_intent, self.handle_go_home_intent)
            diet_intent = IntentBuilder("DietIntent").
                require("diet").build()self.register_intent(diet_intent, self.handle_diet_intent)
            medication_intent = IntentBuilder("MedicationIntent").
                require("medication")self.register_intent(medication_intent, self.handle_medication_intent)
            doctor_visit_intent = IntentBuilder("DoctorVisitIntent").
                require("doctor.visit").build()self.register_intent(doctor_visit_intent, self.handle_doctor_visit_intent)
    # Following the initialize phase,
    # It is now necessary to define methods that handle each of the Intents

    def handle_where_am_i_intent(self, message):
#        self.speak_dialog("whereami")

#    def handle_the_nurse_is_intent(self, message):
#        self.speak_dialog("whoisthenurse")

#    def handle_the_doctor_is_intent(self, message):
#        self.speak_dialog("whoisthedoctor")

#    def handle_go_home_intent(self, message):
#            self.speak("releaserequest")

#    def handle_diet_intent(self, message):
#        self.speak_dialog("dietupdate")
#
#    def handle_medication_intent(self, message):
#        self.speak_dialog("medicationupdate")

#    def handle_doctor_visit_intent(self, message):
#        self.speak_dialog("doctorroundsupdate")
#    @intent_file_handler('demo.nurse.intent')
#    def handle_demo_nurse(self, message):
#        self.speak_dialog('demo.nurse')

def stop(self):
    pass
def create_skill():
    return NurseDemo()
