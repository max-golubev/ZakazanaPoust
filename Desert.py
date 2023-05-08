class Desert:
    def __init__(self, starting_desert_level):
        self.desert_level = starting_desert_level
        self.desert_state = []
        for y in range(5):
            column = []
            for x in range(5):
                column.append(None)
            self.desert_state.append(column)

    def get_desert_state(self):
        return self.desert_state

    def set_desert_state(self, x, y, new_state):
        self.desert_state[y][x] = new_state
