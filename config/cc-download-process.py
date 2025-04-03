from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import json
import re

def determine_attribute(text_to_search, attribute):
    found_attribute = False
    found = re.search(attribute, text_to_search)
    if found is not None:
        found_attribute = True
    return found_attribute

def is_team(team_name):
     teams = ['Baltimore Orioles', 'Boston Red Sox', 'Chicago White Sox', 'Chicago Cubs', 'Cincinnati Reds', 'Cleveland Indians', 'Detroit Tigers',
              'Kansas City Athletics', 'Los Angeles Dodgers', 'Milwaukee Braves', 'New York Yankees', 'Philadelphia Phillies', 'Pittsburgh Pirates', 
              'San Francisco Giants', 'St. Louis Cardinals', 'Washington Senators']

     return team_name in teams

def parse_line(line, card_output):
    player_names = ''
    team_names = ''
    is_rookie_card = False
    is_double_printed = False
    is_short_printed = False
    is_all_star = False

    # Get Card No
    tmp = line.split(' ', 1)
    card_no = tmp[0]

    # Is this a checklist? If so, it will have a dash, but the dash is usually the divider between name and team
    print(tmp[1])
    if re.search('Checklist', tmp[1]):
        card_title = tmp[1]
    else:
        # Parse the remainder of the line
        tmp = tmp[1].split('-')
        if len(tmp) == 1:
            # This means that this is not a player card
            print(tmp)
            return
        else:
            tmp_names = tmp[0].strip().split(',')
            player_names = [name.strip() for name in tmp_names]
            if len(player_names) == 1:
                card_title = player_names[0]

            # Find Card Attributes, which are at the end of the team name (typically)
            is_rookie_card = determine_attribute(tmp[1], ' RC')
            if is_rookie_card:
                tmp[1] = re.sub(r" RC", "", tmp[1])

            is_all_star = determine_attribute(tmp[1], ' AS')
            if is_all_star:
                tmp[1] = re.sub(r" AS", "", tmp[1])

            is_double_printed = determine_attribute(tmp[1], ' DP')
            if is_double_printed:
                tmp[1] = re.sub(r" DP", "", tmp[1])

            is_short_printed = determine_attribute(tmp[1], ' SP')
            if is_short_printed:
                tmp[1] = re.sub(r" SP", "", tmp[1])

            tmp_names = tmp[1].strip().split(',')
            team_names = [name.strip() for name in tmp_names]
            if is_team(team_names[0]) == False:
                print('Not a team: ' + line)
                return

    card_rec = {
        "card_no": card_no,
        "card_title": card_title,
        "player_names": player_names,
        "player_teams": team_names,
        "is_rookie_card": is_rookie_card,
        "is_double_printed": is_double_printed,
        "is_short_printed": is_short_printed,
        "is_all_star": is_all_star
    }
    card_output = card_output + json.dumps(card_rec) + ','

# url_to_parse = 'https://www.cardboardconnection.com/1960-fleer-baseball-cards'
url_to_parse = 'https://www.cardboardconnection.com/1960-topps-baseball-cards-2'
try:
    html = urlopen(url_to_parse)
except HTTPError as e:
    print(e)
    exit(1)
except URLError as e:
    print('The server could not be found!')
    exit(1)

identified_cards = ''
bs = BeautifulSoup(html, 'html.parser')
checklist_data = bs.find_all('div', {'class':'tablechecklist'})
for tablechecklist in checklist_data:
    line_to_parse = tablechecklist.get_text()
    cards = line_to_parse.splitlines()
    for card in cards:
        parse_line(card, identified_cards)