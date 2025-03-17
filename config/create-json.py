import json

with open('/Users/chrisgreatens/Workspace/csadlskdfjsdfjkf/config/sports/baseball/1950/1950-bowman.txt', 'r') as file:
    for line in file:
        tmp = line.split(' ', 1)
        card_no = tmp[0]
        tmp = tmp[1].split('-')

        tmp_names = tmp[0].strip().split(',')
        player_names = [name.strip() for name in tmp_names]

        tmp_names = tmp[1].strip().split(',')
        team_names = [name.strip() for name in tmp_names]

        # This just catches RC for rookie cards at the moment, but can expand as needed.
        card_attributes = tmp[2].strip()

        card_title = tmp[3].strip()
        card_rec = {
            "card_no": card_no,
            "card_title": '',
            "player_names": player_names,
            "player_teams": team_names,
            "card_attributes": card_attributes,
            "card_title": card_title
        }
        card_output = json.dumps(card_rec) + ','
        print(card_output)