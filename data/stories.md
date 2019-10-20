## deleteTweet flow 1
* deleteTweet
    - utter_ask_to_confirm
* affirm
    - delete_latest_tweet

## deleteTweet flow 2
* deleteTweet
    - utter_ask_to_confirm
* deny
    - utter_reply_to_deny

## bye (general)
* bye
    - utter_end

## thankyou (general)    
* thank_you
    - utter_welcome

## chitchat flow 1 (general)
* chitchat_general
    - utter_reply_chitchat_general

## chitchat flow 2 (identity)
* chitchat_identity
    - utter_reply_chitchat_identity

## greet (general)
* greet
    - utter_hello

## General news flow (deny tweet)
* greet
    - utter_hello
* getNews
    - get_news
    - form{"name": "get_news"}
    - slot{"requested_slot": "topic_news"}
* form: inform{"topic_news": "Robotics"}
    - slot{"topic_news": "Robotics"}
    - form: get_news
    - slot{"topic_news": "Robotics"}
    - slot{"output": "Announcing TechCrunch Robotics & AI on March 3, 2020 at UC Berkeley\nhttp://techcrunch.com/2019/10/14/announcing-techcrunch-robotics-ai-on-march-3-2020-at-uc-berkeley/\n "}
    - slot{"topic_news_temp": "Robotics"}
    - slot{"topic_news": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_end

## General news flow without greet (deny tweet)
* getNews
    - get_news
    - form{"name": "get_news"}
    - slot{"requested_slot": "topic_news"}
* form: inform{"topic_news": "Robotics"}
    - slot{"topic_news": "Robotics"}
    - form: get_news
    - slot{"topic_news": "Robotics"}
    - slot{"output": "Announcing TechCrunch Robotics & AI on March 3, 2020 at UC Berkeley\nhttp://techcrunch.com/2019/10/14/announcing-techcrunch-robotics-ai-on-march-3-2020-at-uc-berkeley/\n "}
    - slot{"topic_news_temp": "Robotics"}
    - slot{"topic_news": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_end

## Direct news flow (deny tweet)
* getNews{"topic_news": "Astronomy"}
    - slot{"topic_news": "Astronomy"}
    - get_news
    - form{"name": "get_news"}
    - slot{"topic_news": "Astronomy"}
    - slot{"topic_news": "Astronomy"}
    - slot{"output": "How Two Nobel Laureates Spotted the First Exoplanet\nhttps://www.wired.com/story/how-two-nobel-laureates-spotted-the-first-exoplanet/\n "}
    - slot{"topic_news_temp": "Astronomy"}
    - slot{"topic_news": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* deny
    - utter_end

## Direct news flow (tweet)
## Direct news flow (deny tweet)
* getNews{"topic_news": "Astronomy"}
    - slot{"topic_news": "Astronomy"}
    - get_news
    - form{"name": "get_news"}
    - slot{"topic_news": "Astronomy"}
    - slot{"topic_news": "Astronomy"}
    - slot{"output": "How Two Nobel Laureates Spotted the First Exoplanet\nhttps://www.wired.com/story/how-two-nobel-laureates-spotted-the-first-exoplanet/\n "}
    - slot{"topic_news_temp": "Astronomy"}
    - slot{"topic_news": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - send_tweet

## General news flow (tweet & delete)
* greet
    - utter_hello
* getNews
    - get_news
    - form{"name": "get_news"}
    - slot{"requested_slot": "topic_news"}
* form: inform{"topic_news": "ISRO"}
    - slot{"topic_news": "ISRO"}
    - form: get_news
    - slot{"topic_news": "ISRO"}
    - slot{"output": "Rocket Report: The Falcon 9 goes for four, Boeing’s big cost-plus deal\nhttps://arstechnica.com/science/2019/10/rocket-report-the-falcon-9-goes-for-four-boeings-big-cost-plus-deal/\n "}
    - slot{"topic_news_temp": "ISRO"}
    - slot{"topic_news": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - send_tweet
* deleteTweet
    - utter_ask_to_confirm
* affirm
    - delete_latest_tweet

## General news flow without greet (tweet)
* getNews
    - get_news
    - form{"name": "get_news"}
    - slot{"requested_slot": "topic_news"}
* form: inform{"topic_news": "ISRO"}
    - slot{"topic_news": "ISRO"}
    - form: get_news
    - slot{"topic_news": "ISRO"}
    - slot{"output": "Rocket Report: The Falcon 9 goes for four, Boeing’s big cost-plus deal\nhttps://arstechnica.com/science/2019/10/rocket-report-the-falcon-9-goes-for-four-boeings-big-cost-plus-deal/\n "}
    - slot{"topic_news_temp": "ISRO"}
    - slot{"topic_news": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - send_tweet

## General news flow without greet (tweet and delete)
* getNews
    - get_news
    - form{"name": "get_news"}
    - slot{"requested_slot": "topic_news"}
* form: inform{"topic_news": "ISRO"}
    - slot{"topic_news": "ISRO"}
    - form: get_news
    - slot{"topic_news": "ISRO"}
    - slot{"output": "Rocket Report: The Falcon 9 goes for four, Boeing’s big cost-plus deal\nhttps://arstechnica.com/science/2019/10/rocket-report-the-falcon-9-goes-for-four-boeings-big-cost-plus-deal/\n "}
    - slot{"topic_news_temp": "ISRO"}
    - slot{"topic_news": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - send_tweet
* deleteTweet
    - utter_ask_to_confirm
* affirm
    - delete_latest_tweet

## General news flow without greet (tweet, delete but deny)
* getNews
    - get_news
    - form{"name": "get_news"}
    - slot{"requested_slot": "topic_news"}
* form: inform{"topic_news": "ISRO"}
    - slot{"topic_news": "ISRO"}
    - form: get_news
    - slot{"topic_news": "ISRO"}
    - slot{"output": "Rocket Report: The Falcon 9 goes for four, Boeing’s big cost-plus deal\nhttps://arstechnica.com/science/2019/10/rocket-report-the-falcon-9-goes-for-four-boeings-big-cost-plus-deal/\n "}
    - slot{"topic_news_temp": "ISRO"}
    - slot{"topic_news": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - send_tweet
* deleteTweet
    - utter_ask_to_confirm
* deny
    - utter_end

