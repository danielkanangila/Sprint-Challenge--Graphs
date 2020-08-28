from player import Player


class MazeSolver():
    def __init__(self, player: Player):
        self.player = player

    def dft_traversal_path(self):

        reverse_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

        graph = {}
        starting_room_id = self.player.current_room.id
        traversal_path = []

        # Create a stack to store the possible excape direction
        stack = []

        # Add starting room to the graph without possible directions
        graph[starting_room_id] = {}

        # Get possible exits directions from current room
        exits = self.player.current_room.get_exits()

        print(exits)
