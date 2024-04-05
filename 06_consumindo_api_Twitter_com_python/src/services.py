import tweepy
from typing import Any, Dict, List
from src.secrets import USER_NAME_MONGO, PASSWORD_MONGO
from src.secrets import consumer_key, consumer_secret, acess_token, acess_token_secret
from src.constantes import BRAZIL_WOE_ID
from src.connection import trends_collection


def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]: 
   

    trends = api.trends_place(woe_id)

    return trends[0]["trends"]

def get_trends_from_mongo() -> List[Dict[str, Any]]:
    # Retorna informacao do db para a variavel
    trends =  trends_collection.find({})
    return list(trends)

def save_trends() -> None:

    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(acess_token, acess_token_secret)
    
    api = tweepy.API(auth)
    
    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)       
         