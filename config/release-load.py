import json
import mariadb
import sys

with open('/Users/chrisgreatens/Workspace/csadlskdfjsdfjkf/config/sports/baseball/1953/1953-bowman-color.json', 'r') as file:
    json_data = json.load(file)

print(json_data['release'])

try:
    conn = mariadb.connect(
        user="sportscards",
        password="",
        host="localhost",
        port=3306,
        database="sportscards"
    )
except mariadb.Error as e:
    print(f"Error connecting to database: {e}")
    sys.exit(1)

cur = conn.cursor()

# See if the set already exists
release_id = -1
try:
    cur.execute("SELECT id FROM releases WHERE release_year = ? AND release_brand = ? AND release_name = ? LIMIT 1",
                (json_data['release']['year'],
                 json_data['release']['brand'],
                 json_data['release']['release_name']))
    for (id) in cur:
        release_id = id[0]
except mariadb.Error as e:
    print(f"Error reading release record into database: {e}")
    sys.exit(1)

# If it doesn't exist, write the release record
if (release_id == -1):
    try:
        cur.execute(
            "INSERT INTO releases (release_year, release_brand, release_name, category_id, subcategory_id, description) VALUES (?,?,?,?,?,?)", 
            (json_data['release']['year'],
            json_data['release']['brand'],
            json_data['release']['release_name'],
            json_data['release']['category'],
            json_data['release']['subcategory'],
            json_data['release']['description']))
    except mariadb.Error as e:
        print(f"Error inserting release record into database: {e}")
        sys.exit(1)
    release_id = cur.lastrowid

set_id = -1
try:
    cur.execute("SELECT id FROM sets WHERE release_id = ? AND set_name = ? AND set_type = ? LIMIT 1",
                (release_id,
                 json_data['set']['set_name'],
                 json_data['set']['set_type']))
    for (id) in cur:
        set_id = id[0]
except mariadb.Error as e:
    print(f"Error reading set record into database: {e}")
    sys.exit(1)

# If it doesn't exist, write the release record
if (set_id == -1):
    try:
        cur.execute(
            "INSERT INTO sets (release_id, set_name, set_type, is_autographed, max_serial_num, description) VALUES (?,?,?,?,?,?)", 
            (release_id,
            json_data['set']['set_name'],
            json_data['set']['set_type'],
            json_data['set']['is_autographed'],
            json_data['set']['max_serial_num'],
            json_data['set']['description']))
    except mariadb.Error as e:
        print(f"Error inserting set record into database: {e}")
        sys.exit(1)
    set_id = cur.lastrowid

# Load the individual cards
cards = json_data['cards']
for card in cards:
    # Find the existing player record or insert one
    card_id = -1
    card_no = card['card_no']
    card_title = card['card_title']
    try:
        cur.execute("SELECT id FROM cards WHERE set_id = ? AND card_no = ? AND card_title = ? LIMIT 1",
            (set_id,
             card_no,
             card_title))
        for (id) in cur:
            card_id = id[0]
    except mariadb.Error as e:
        print(f"Error reading card record from database: {e}")
        sys.exit(1)
    if (card_id == -1):
        try:
            cur.execute("INSERT INTO cards (set_id, card_no, card_title) VALUES (?,?,?)",
            (set_id,
             card_no,
             card_title))
        except mariadb.Error as e:
            print(f"Error inserting card record into database: {e}")
            sys.exit(1)
        card_id = cur.lastrowid

    # Insert into Card/Player Table
    for player_name in card['player_names']:
        # If there is a player on this card
        if player_name:
            player_name = player_name.strip()

            # Find the existing player record or insert one
            player_id = -1

            # Look for the player in the players table
            try:
                cur.execute("SELECT id FROM players WHERE player_name = ? LIMIT 1", (player_name,))
                for (id) in cur:
                    player_id = id[0]
            except mariadb.Error as e:
                print(f"Error reading player record from database: {e}")
                sys.exit(1)
            
            # If the player isn't in the players table, add it
            if (player_id == -1):
                try:
                    cur.execute("INSERT INTO players (player_name) VALUES (?)", (player_name,))
                except mariadb.Error as e:
                    print(f"Error inserting player record into database: {e}")
                    sys.exit(1)
                player_id = cur.lastrowid

            # Add a card/player record, ignore it if it already exists
            # Look for entry in the card/players table
            player_card_id = -1
            try:
                cur.execute("SELECT id FROM card_players WHERE card_id = ? AND player_id = ? LIMIT 1", (card_id,player_id))
                for (id) in cur:
                    player_card_id = id[0]
            except mariadb.Error as e:
                print(f"Error reading card/player record from database: {e}")
                sys.exit(1)
            if player_card_id == -1:
                try:
                    cur.execute(
                        "INSERT INTO card_players (card_id, player_id) VALUES (?,?)", (card_id, player_id))
                except mariadb.Error as e:
                    print(f"Error inserting card player record into database: {e}")
                    sys.exit(1)

    # Insert into Card/Team Table
    for team_name in card['player_teams']:  
        # If there is a team for this card
        if team_name:
            team_name = team_name.strip()
            # Find the existing team record or insert one
            team_id = -1

            # Try to find the team in the database
            try:
                cur.execute("SELECT id FROM teams WHERE team_name = ? LIMIT 1", (team_name,))
                for (id) in cur:
                    team_id = id[0]
            except mariadb.Error as e:
                print(f"Error reading team record from database: {e}")
                sys.exit(1)

            # Team wasn't found in the database, so insert a team record
            if (team_id == -1):
                try:
                    cur.execute("INSERT INTO teams (team_name) VALUES (?)", (team_name,))
                except mariadb.Error as e:
                    print(f"Error inserting team record into database: {e}")
                    sys.exit(1)
                team_id = cur.lastrowid

            # Insert a card/team record, ignore it if it already exists    
            # Try to find the team in the database
            card_team_id = -1
            try:
                cur.execute("SELECT id FROM card_teams WHERE card_id = ? AND team_id = ? LIMIT 1", (card_id,team_id,))
                for (id) in cur:
                    card_team_id = id[0]
            except mariadb.Error as e:
                print(f"Error reading card/teams record from database: {e}")
                sys.exit(1)

            if card_team_id == -1:
                try:
                    cur.execute(
                        "INSERT INTO card_teams (card_id, team_id) VALUES (?,?)", (card_id,team_id))
                except mariadb.Error as e:
                    print(f"Error inserting card team record into database: {e}")
                    sys.exit(1)

# Clean up on successful add of release to the database
cur.close()
conn.commit()