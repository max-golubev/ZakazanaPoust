import Player
import Items
from enum import Enum


class Direction(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Tile:
    def __init__(self, x, y, starting_sand_level):
        self.sand_level = starting_sand_level
        self.x = x
        self.y = y
        self.technology = None
        self.has_sun_protection = False
        self.is_opened = False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_open(self):
        return self.is_opened

    def get_sand_level(self):
        return self.sand_level

    def open(self):
        self.is_opened = True
        return None

    def remove_sand(self):
        if self.sand_level != 0:
            self.sand_level -= 1

    def has_sun_protection(self):
        return self.has_sun_protection


class NormalTile(Tile):
    def __init__(self, x, y, starting_sand_level, technology: Items.Technology):
        super().__init__(x, y, starting_sand_level)
        self.technology = technology

    def open(self):
        self.is_opened = True
        return self.technology


class ClueTile(Tile):
    def __init__(self, x, y, starting_sand_level,
                 pointed_out_part: Items.Part,
                 pointed_direction: Direction):
        super().__init__(x, y, starting_sand_level)
        self.pointed_part = pointed_out_part
        self.direction = pointed_direction

    def get_direction(self):
        return self.direction


class ShipwreckTile(NormalTile):
    def __init__(self, x, y, starting_sand_level, technology: Items.Technology):
        super().__init__(x, y, starting_sand_level, technology)
        self.needed_parts = Items.Part.get_all_parts()
        self.attached_parts = []

    def attach_part(self, part: Items.Part):
        self.needed_parts.remove(part)
        self.attached_parts.append(part)


class OasisTile(Tile):
    def __init__(self, x, y, starting_sand_level):
        super().__init__(x, y, starting_sand_level)
        self.fill_level = 4

    def refill_water(self, player: Player):
        if self.fill_level != 0:
            if player.water_level < (player.MAX_WATER_LEVEL - 2):
                player.water_level += 2
            elif player.water_level >= (player.MAX_WATER_LEVEL - 2):
                player.water_level = player.MAX_WATER_LEVEL
            self.fill_level -= 1
        else:
            print("Can not refill water because there is none.")


class FatamorganaTile(OasisTile):
    def __init__(self, x, y, starting_sand_level):
        super().__init__(x, y, starting_sand_level)
        self.fill_level = 0


class TunnelTile(NormalTile):
    def __init__(self, x, y, starting_sand_level, technology: Items.Technology):
        super().__init__(x, y, starting_sand_level, technology)
        self.has_sun_protection = True
