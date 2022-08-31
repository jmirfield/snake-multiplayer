import numpy as np

class SnakeController:
    def parse_data(raw_data):
        data = SnakeController.clean_data(raw_data)
        raw_arr = data[1:-1]
        arr = raw_arr.split("/")
        parsed = {}
        for player in arr:
            if player:
                player_id = player[0:2]
                player_coor = player[2:]
                parsed[player_id] = np.array([x.strip().split(',') for x in player_coor.split(' ')], dtype=int)
        return parsed
    
    def clean_data(data):
        i = -1
        while data[i] != "[":
            i -= 1
        return data[i:]
