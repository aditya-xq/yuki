from rasa_sdk import ActionExecutionRejection
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT, Action
from rasa.core.slots import Slot
from typing import Dict, Text, Any, List, Union
from Engines import *

import sqlite3
import random

# %%
# conn = sqlite3.connect('master.db')  # Connecting to our db file
# %%

# Get news form action


class GetNews(FormAction):
    def name(self):
        return "get_news"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["topic_news"]  # add GPE later

    def slot_mappings(self):
        return {
            "topic_news": [
                self.from_text(intent=[None, "getNews", "inform"]),
                self.from_entity(entity="topic_news", intent=["getNews"])
            ]
        }

    def validate(self, dispatcher: CollectingDispatcher, tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(
                self.extract_requested_slot(dispatcher, tracker, domain))
            if not slot_values:
                raise ActionExecutionRejection(
                    self.name(), "Failed to validate slot {0} "
                    "with action {1}"
                    "".format(slot_to_fill, self.name()))

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        topic_news = tracker.get_slot("topic_news")
        dispatcher.utter_message("Here is some news I found!")
        data = newsEngine.fetchNews(topic_news)

        for i in range(len(data)):
            output = data[i]['title'] + "\n" + data[i]['url'] + "\n "
            dispatcher.utter_message(output)

        dispatcher.utter_template("utter_confirm_if_service_is_correct",
                                  tracker)
        dispatcher.utter_template("utter_ask_to_tweet", tracker)

        # utter submit template
        return [
            SlotSet("output", output),
            SlotSet("topic_news_temp", topic_news),
            SlotSet("topic_news", None)
        ]


################################################################################################################################
# Action to tweet


class SendTweet(Action):
    def name(self):
        return "send_tweet"

    def run(self, dispatcher, tracker, domain):

        output = tracker.get_slot("output")
        tweet = 'Latest news update: ' + output + ' -- posted by Yuki, the AI #YukiAITweets'

        twitterEngine.doTweet(tweet)
        dispatcher.utter_message(
            random.choice([
                'Hooray! the tweet has been successfully posted',
                'Posted the tweet!', 'Hai! tweet sucessfully posted'
            ]))

        return [SlotSet("output", None)]


#################################################################################################################################


class DeleteLatestTweet(Action):
    def name(self):
        return "delete_latest_tweet"

    def run(self, dispatcher, tracker, domain):
        twitterEngine.deleteLatestTweet()
        dispatcher.utter_message(
            random.choice['Your latest tweet has been deleted',
                          'Deleted your tweet! Careful next time.'])
        return []


#################################################################################################################################
