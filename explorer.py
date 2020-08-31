import random

from player import Player
from room import Room


class Explorer():
    def __init__(self, player: Player):
        self.player = player
        self.reverse_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    def get_traversal_path(self):
        return self.dft(self.player.current_room)

    """
        Recursive call function to explore maze graph
        current_room = starting vertex | default = current player room on initialization
        visited = dict to track all visited room (vertex) | default = empty dict
    """

    def dft(self, room: Room, visited=set(), ):
        # explored_path = log of explored paths | default = empty list
        explored_path = []
        # Add current room's ID to visited. Marked it as visited
        visited.add(room.id)
        # Get all possible exits from current room and loop through
        exits = room.get_exits()
        for _exit in exits:
            # Update current room to be the room in this exit direction
            current_room = room.get_room_in_direction(_exit)
            # Check if this current room has not been visited
            if current_room.id not in visited:
                # explore the new room. Recursive call.
                # Valid path mean, we can move to this direction. Not valid path is dead-end, no room in this direction
                valid_path = self.dft(current_room, visited)
                # Check if returned path is valid. If valid update current_path to include valid path
                if valid_path:
                    current_path = [_exit] + valid_path + \
                        [self.reverse_directions[_exit]]
                # else, update current path and exclude invalid path (backtrack)
                else:
                    current_path = [_exit, self.reverse_directions[_exit]]
                # Add valid and not valid path to explored path and return it
                explored_path = explored_path + current_path
        # return all explored path
        return explored_path
