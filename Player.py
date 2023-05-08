import Tile


class Player:
    def __init__(self, x, y, position: Tile.Tile, actions, starting_water_level):
        self.x = x
        self.y = y
        self.position = position
        self.actions = actions
        self.MAX_WATER_LEVEL = starting_water_level
        self.water_level = starting_water_level

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_water_level(self):
        return self.water_level

    def get_actions(self):
        return self.actions

    def change_x_plus(self):
        self.x += 1

    def change_x_minus(self):
        self.x -= 1

    def change_y_plus(self):
        self.y += 1

    def change_y_minus(self):
        self.y -= 1


class WaterCarrier(Player):
    def __init__(self, x, y, position: Tile.Tile, actions, starting_water_level):
        super(WaterCarrier, self).__init__(x, y, position, actions, starting_water_level)

