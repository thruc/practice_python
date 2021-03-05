from chessdotcom import import
from chessdotcom import get_leaderboards

def print_lb():
    data = get_leaderboards()
    print(data.json)