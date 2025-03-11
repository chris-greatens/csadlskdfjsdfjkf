import json

with open('/Users/chrisgreatens/Workspace/beego-1/config/sports/baseball/1951/1951-bowman.txt', 'r') as file:
    for line in file:
        tmp = line.split(' ', 1)
        card_no = tmp[0]
        tmp = tmp[1].split('-')
        player_names = tmp[0].strip().split(',')
        team_names = tmp[1].strip().split(',')
        card_title = tmp[2].strip()
        card_rec = {
            "card_no": card_no,
            "card_title": '',
            "player_names": player_names,
            "player_teams": team_names,
            "card_title": card_title
        }
        card_output = json.dumps(card_rec) + ','
        print(card_output)