# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "first_custom_actions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Welcome to Custom actions of RASA ft.Python")

        return []


class ActionCovidResponse(Action):

    def name(self) -> Text:
        return "get_covid_results"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get('https://api.covid19india.org/data.json').json()  

        entities = tracker.latest_message['entities']
        state= None

        for e in entities:
            if e['entity']=='state':
                state= e['value']

        message="Please enter India/Tamilnadu/Kerala/Karnataka/Andharapradesh/Maharashtra/Delhi"
        print(state.title())
        if state=="india":
            state="Total"

        for data in response["statewise"]:
            if data["state"] == state.title():
                # message="Active :"+data["active"] +"Confirmed: "+data["confirmed"] + "Recovered: "+data["recovered"] + "Deaths: "+data["deaths"]+"Last Updated Time: "+data["lastupdatedtime"]
                message1="Active :"+data["active"] +"Confirmed: "+data["confirmed"] + "Recovered: "+data["recovered"] 
                message2="Deaths: "+data["deaths"]+"Last Updated Time: "+data["lastupdatedtime"]
                message=message1+message2

        dispatcher.utter_message(text=message)

        return []
