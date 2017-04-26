import facebook
from .config import facebook_token

def get_user_info(id):
    try:
        graph = facebook.GraphAPI(access_token=facebook_token, version = '2.7')
        r = '/{}'.format(id)
        events = graph.request(r)
        return events
    except facebook.GraphAPIError as error:
        raise error