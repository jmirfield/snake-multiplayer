import numpy as np

class Snake:
    def parse_data(data):
        raw = data[1:-1]
        arr = raw.split("/")
        parsed = {}
        for player in arr:
            player_id = player[0:2]
            player_coor = player[2:]
            parsed[player_id] = np.array([x.strip().split(',') for x in player_coor.split(' ')], dtype=int)
        return parsed
