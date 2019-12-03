import requests
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class NavigationSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')



    @intent_handler(IntentBuilder('NavigationIntent').require('NavigationKeyword'))
    def handle_hello_world_intent(self, message):
        """ Skills can log useful information. These will appear in the CLI and
        the skills.log file."""
        
        
        
        url='https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=Madhapur+Police+Station&destinations=Jawaharlal+Nehru+Technological+University+Hyderabad&key=AIzaSyBpfgcCEAI_cnJB2yAtT7xw2m2Ci-e6vc0'

        r = requests.get(url)
        
        json_output = r.json()
        #print(json_output)
        
        output=json_output['rows']

        elements = output[0]['elements']
        distance = elements[0]['distance']
        duration = elements[0]['duration']

        di=distance['text']
        du=duration['text']
        
        
        
        
        
        self.log.info("There are five types of log messages: "
                      "info, debug, warning, error, and exception.")
    self.speak_dialog("navigation.to.home",{"distance":di},{"duration":du})

    def stop(self):
        pass


def create_skill():
    return NavigationSkill()
